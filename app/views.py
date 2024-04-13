from django.shortcuts import render, redirect
from .models import Message, Photo
from .forms import MessageForm, PhotoForm

def home(request):
    photo_form = PhotoForm()  # 기본값으로 초기화
    message_form = MessageForm()  # 기본값으로 초기화

    if request.method == 'POST':
        if 'upload_photo' in request.POST:
            photo_form = PhotoForm(request.POST, request.FILES)
            if photo_form.is_valid():
                photo_form.save()
                return redirect('home')
        elif 'post_message' in request.POST:
            message_form = MessageForm(request.POST, request.FILES)
            if message_form.is_valid():
                message_form.save()
                return redirect('home')
    else:
        # 이 부분은 이제 제거해도 됩니다. 이미 위에서 초기화했기 때문입니다.
        pass

    messages = Message.objects.all()
    photos = Photo.objects.all()
    return render(request, 'home.html', {
        'photo_form': photo_form,
        'message_form': message_form,
        'messages': messages,
        'photos': photos
    })

