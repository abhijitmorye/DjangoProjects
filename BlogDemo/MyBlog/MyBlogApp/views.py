from django.shortcuts import render, redirect
from .models import UserData

# Create your views here.


def index(request):
    return render(request, 'MyBlogApp/index.html')



def success(request):
    context = {
        "msg" : "msg"
    }
    return render(request, 'MyBlogApp/success.html', context)



def register(request):
    if request.method == 'POST':
        name = request.POST.get('name',)
        email_id = request.POST.get('email_id',)
        password = request.POST.get('password',)
        phn_number = request.POST.get('phn_number',)
        profileImage = request.FILES['profileImage']
        userData = UserData(name=name, email_id=email_id, password=password, phn_number=phn_number, profileImage=profileImage)
        userData.save()
        context = {
            "msg" : "registeration"
        }
        return render(request, 'MyBlogApp/success.html', context)

    return render(request, 'MyBlogApp/Register.html')




def login_fresh(request):
    return render(request, 'MyBlogApp/login.html')



def login(request):
    if request.method == 'POST':
        user_name = request.POST.get('email_id')
        password = request.POST.get('password')
        if user_name == '' and password == '':
            return render(request, 'MyBlogApp/warning.html')        
        else:
            userData = UserData.objects.get(email_id=user_name)
            if userData.email_id == user_name and userData.password == password:
                request.session['user'] = user_name
                return redirect('/loginsuc/')
            else:
                return render(request, 'MyBlogApp/warning.html')

    return render(request, 'MyBlogApp/login.html')



def warning(request):
    return render(request, 'MyBlogApp/warning.html')



def loginSuccess(request):
    if 'user' in request.session:
        current_user = UserData.objects.get(email_id=request.session['user'])
        context = {
            'user' : current_user
        }
        return render(request, 'MyBlogApp/loginSuc.html', context)
    else:
        return redirect('/login_fresh/')  



def profile(request):
    if 'user' in request.session:
        current_user = UserData.objects.get(email_id=request.session['user'])
        context = {
            'user' : current_user
        }
        return render(request, 'MyBlogApp/profile.html', context)
    else:
        return redirect('/')


def logout(request):
    try:
        del request.session['user']
        return redirect('/')
    except:
        return redirect('/')



def update(request):
    if request.method == "POST":
        if 'user' in request.session:
            #old values
            prev_info = UserData.objects.get(email_id=request.session['user'])
            prev_name = prev_info.name
            prev_email_id = prev_info.email_id
            prev_phn_number = prev_info.phn_number
            prev_profileImage = prev_info.profileImage

            print(prev_profileImage )

            # updated values
            name = request.POST.get('name',)
            email_id = request.POST.get('email_id',)
            phn_number = request.POST.get('phn_number',)

            try:
                profileImage = request.FILES['profileImage']
                prev_info.profileImage = profileImage
                print(profileImage)
            except:
                prev_info.profileImage = prev_profileImage


            if name == '':                
                prev_info.name = prev_name
            else:
                prev_info.name = name
            if email_id == '':
                prev_info.email_id = prev_email_id
            else:
                prev_info.email_id = email_id
            if phn_number == '':
                prev_info.phn_number = prev_phn_number
            else:
                prev_info.phn_number = phn_number           
            prev_info.save()
            return redirect('/profile/')
        
        else:
            return redirect('/')

    if 'user' in request.session:
        #old values
        prev_info = UserData.objects.get(email_id=request.session['user'])
        context = {
            'user' : prev_info
        }
        return render(request, 'MyBlogApp/updateprofile.html', context)
    else:
        return redirect('/')

    
    






