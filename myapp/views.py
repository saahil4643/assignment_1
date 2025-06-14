from rest_framework.response import Response
from rest_framework import generics, permissions
from .models import Message
from django.contrib.auth.decorators import login_required
from .serializers import MessageSerializer
from django.shortcuts import render

from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from .tasks import send_welcome_email



# Public: Anyone can access
class PublicMessageList(generics.ListAPIView):
    serializer_class = MessageSerializer
    permission_classes = []

    def get_queryset(self):
        queryset = Message.objects.filter(is_protected=False)
        return queryset

    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()

        if not queryset.exists():
            # Return a default message when no data exists
            default_data = [{
                "id": 0,
                "content": "This is a default public message",
                "is_protected": False
            }]
            return Response(default_data)

        return super().list(request, *args, **kwargs)

# Protected: Only JWT-authenticated users can access
class ProtectedMessageList(generics.ListAPIView):
    queryset = Message.objects.filter(is_protected=True)
    serializer_class = MessageSerializer
    permission_classes = [permissions.IsAuthenticated]


@login_required
def dashboard(request):
    return render(request, 'dashboard.html')

def register_user(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')

        user = User.objects.create_user(username=username, email=email, password=password)
        user.save()

        send_welcome_email.delay(user.email)

        return redirect('login')
    return render(request, 'register.html')

from django.contrib import messages

def register_user(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')

        if not username or not email or not password:
            messages.error(request, "All fields are required.")
            return redirect('register')

        if User.objects.filter(username=username).exists():
            messages.error(request, "Username already taken.")
            return redirect('register')

        if User.objects.filter(email=email).exists():
            messages.error(request, "Email already registered.")
            return redirect('register')

        user = User.objects.create_user(username=username, email=email, password=password)
        user.save()

        # Send welcome email asynchronously
        send_welcome_email.delay(user.email)

        messages.success(request, "Registration successful. Please login.")
        return redirect('login')

    return render(request, 'register.html')
