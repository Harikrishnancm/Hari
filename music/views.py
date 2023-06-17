from django.shortcuts import render,redirect
from .models import Song
from django.contrib.auth.models import User,auth
from django.contrib import messages
from django.contrib.auth import login,logout
from django.contrib.auth.decorators import login_required
from django.conf import settings
from django.core.mail import send_mail

# Create your views here.
@login_required(login_url="login")
def index(request):
    query = request.GET.get('search')
    if query:
            print(query)
            allSongs = Song.objects.filter(songname__icontains=query)
    else:
            allSongs = Song.objects.filter()

    if allSongs:
            print(allSongs[0].songname)
            print('loaded')
            context = {"allsongs": allSongs}
            return render(request, 'index.html', context)
    # else:
    #     return redirect('index.html')
    

def playMusic(request,i):
    s=Song.objects.get(id=i)
    print(s.song.url)
    return render(request,"music.html",{"music":s})
    
def next(request,i):
    sng=Song.objects.get(id=(i+1))
    return render(request,"music.html",{"music":sng})
    
def prev(request,i):
    sng=Song.objects.get(id=(i-1))
    return render(request,"music.html",{"music":sng})

        
def register(request):
    if request.method == "POST":
        username=request.POST['username']
        email=request.POST['email']
        pass_word=request.POST['password1']
        c_pass_word=request.POST['confirm_password']
        if pass_word==c_pass_word:
                if User.objects.filter(username=username):
                    messages.info(request,"username already exists")
                    return redirect('register')
                elif User.objects.filter(email=email).exists():
                    messages.info(request,"email taken")  
                    return redirect('register')
                else:
                    user=User.objects.create_user(
                    username=username,
                    email=email,
                    password=pass_word,
                    )
                    user.save()
                    subject = 'WELCOME TO MUSICPLAYER'
                    message = f'{username}, You are Succesfully Registered!!'
                    email_from = settings.EMAIL_HOST_USER
                    recipient_list = [user.email, ]
                    send_mail(subject,message,email_from,recipient_list)
                    print('success')
                    return redirect('login')
        else:  
            return redirect('regiser')
        
    else:
        return render(request,"register.html")
 
    
def login(request):
    if request.method == "POST":
        username=request.POST['username']
        password=request.POST['password']
        user=auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request,user)
            return redirect('index')
        else:
            messages.info(request,"invalid login")
            return redirect('login')
    else:
            # User is authenticated
        return render(request,"login.html")    
    
def signout(request):
    logout(request)
    return redirect('login')          
    
