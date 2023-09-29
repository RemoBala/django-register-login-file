from django.shortcuts import render,HttpResponse
from .models import *

# Create your views here.
def index(request):
    """docstring for fname"""
    return render(request,"index.html")




from django.shortcuts import render, redirect
from .forms import PersonForm

def create_person(request):
    if request.method == 'POST':
        form = PersonForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/create')  # Redirect to a success page
            # return HttpResponse('success_page')  
    else:
        form = PersonForm()
    
    return render(request, 'person_form.html', {'form': form})





from .models import User_datas

def register_data(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        confirm_password = request.POST['confirm_password']
        mail = request.POST['email']

        if User_datas.objects.filter(username=username).exists():
            error_message = 'This username  is already registered.'
            return render(request, 'register.html', {'error_message': error_message})
       
        if User_datas.objects.filter(mail=mail).exists():
            error_message = 'This mail address is already registered.'
            return render(request, 'register.html', {'error_message': error_message})

        if password == confirm_password:
            # Create a User_datas object and save it to the database
            user = User_datas(username=username, password=password, mail=mail)
            user.save()

            return redirect('/register')  # Redirect to a success page
        else:
            error_message = 'Passwords do not match.'
            return render(request, 'register.html', {'error_message': error_message})
    else:
        return render(request, 'register.html')




def login_data(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']


        try:
            user = User_datas.objects.get(mail=email, password=password)
        except User_datas.DoesNotExist:
            user = None

        if user is not None:
            # request.session['user_id'] = user.id
            success_message = 'Login successful!'
            return render(request, 'login.html', {'success_message': success_message})
        else:
            error_message = 'Invalid email or password. Please try again.'
            return render(request, 'login.html', {'error_message': error_message})
    else:
        return render(request, 'login.html')



from django.contrib.auth.forms import UserCreationForm
def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/user_login')
    else:
        form = UserCreationForm()
    return render(request, 'register1.html', {'form': form})


from django.contrib.auth import login, authenticate
def user_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None and user.is_staff==0:
            login(request, user)
            print(request.user)
            return redirect('/') 
    
            
    return render(request, 'login1.html')


from django.contrib.auth import logout
def user_logout(request):
    logout(request)
    return redirect('/')


def Admin(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None and user.is_staff:
            login(request, user)
            print(request.user)
            return redirect('/') 
    return render(request, 'login1.html')



# def register(request):
#    if request.method == 'POST':
#         data = request.POST
#         username=data['username']
#         password= data['password1']
#         confirmpassword=data['password2']
#         print(data)
#         try:
#             u_name = User_datas.objects.get(username=username)
#         except:
#             u_name = None
#         if u_name == None:
#             User_datas.objects.create(username=username, password=password,confirmpassword=confirmpassword )
#             return redirect('/')
#         else:
#             msg="already exist email"     
#             return render(request,"login1.html",{"error":msg})  
          
#    return render(request,"register1.html")
    


