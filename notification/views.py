import importlib
from django.shortcuts import render, redirect
from notification.models import Notification

def ShowNotification(request):
    user = request.user
    notifications = Notification.objects.filter(user=user).order_by('-date')

    context = {
        'notifications': notifications,

    }
    return render(request, 'notifications/notification.html', context)

def DeleteNotification(request, noti_id):
    user = request.user
    Notification.objects.filter(id=noti_id, user=user).delete()
    return redirect('show-notification')

def load_module_dynamically(module_name, file_path):
    spec = importlib.util.spec_from_file_location(module_name, file_path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module
