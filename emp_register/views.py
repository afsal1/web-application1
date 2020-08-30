from django.shortcuts import render,redirect
#from emp_register.forms import Emp_form
#from .models import User
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.contrib.auth.models import User, auth
from django.contrib.auth.decorators import login_required
from django.views.decorators.cache import cache_control


# Create your views here.

"""def search(request):
    query_string = ''
    found_entries = None
    if ('q' in request.GET) and request.GET['q'].strip():
        query_string = request.GET['q']
        entry_query = utils.get_query(query_string, ['title', 'body',])
        posts = Post.objects.filter(entry_query).order_by('created')
        return render(request, 'search.html', { 'query_string': query_string, 'posts': posts })
    else:
        return render(request, 'search.html', { 'query_string': 'Null', 'found_entries': 'Enter a search term' })"""

"""@login_required(login_url='/user_login')
def admin_login(request):
    user = User.objects.all()
    return render(request,'admin_login.html',{'user':user})"""

# it is the main page for adding a student data
def emp(request):
    
    if request.method == "POST":
        
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        username = request.POST['username']
        password1 = request.POST['password1']
        
        if password1 == password1 :
            if User.objects.filter(username=username).exists():
                messages.info(request,'Username Taken')
                return HttpResponseRedirect(request.path_info)
            elif User.objects.filter(email=email).exists():
                messages.info(request,'Email Taken')
                return HttpResponseRedirect(request.path_info)
            else:
                user = User.objects.create_user(username=username,password=password1,email=email,first_name=first_name,last_name=last_name)
                user.save()
                return redirect(user_login)
            

    else:
            
        return render(request, 'index.html')

"""def admin_login(request):
    form = Emp_form(request.POST)
    if request.method == "POST":
        u_name = request.POST['u_name']
        password = request.POST['password']
        if (u_name == 'assdd' and password == '1234'):
            return render(request, "view.html",{'emp_register': emp_register})
        else:
            print("admin login error")
    else:
        return render(request, 'index.html', {'form': form})"""


#it is for admin view table
@login_required(login_url="/admin_login")
@cache_control(no_cache=True, must_revalidate=True,no_store=True)

def view(request):
    user = User.objects.all()
    if request.method =='POST':
        first_name = request.POST['search']
        users = User.objects.get(first_name=first_name)
        return render(request, 'search.html',{'users':users})
    else:        
        return render(request, "view.html",{'users': user})


@login_required(login_url="/admin_login")
@cache_control(no_cache=True, must_revalidate=True,no_store=True)
def adminlogout(request):
    auth.logout(request)
    
    return render(request, "admin_login.html")


#user view table
@login_required(login_url="/")
@cache_control(no_cache=True, must_revalidate=True,no_store=True)

def user(request):
    user = User.objects.all()

    return render(request, "user.html",{'users': user})
   
#logout
@login_required(login_url="/")
@cache_control(no_cache=True, must_revalidate=True,no_store=True)
def logout(request):
    auth.logout(request)
    return redirect("/")



 
#delete
def delete(request, id):
    user = User.objects.get(id=id)
    user.delete()
    return redirect("/view/")

#

#for administration login
def admin_login(request):
    if request.user.is_authenticated:
        return redirect("/view")
    elif request.method == 'POST':
        username= request.POST.get("username")
        password= request.POST.get("password")
        user = auth.authenticate(username=username,password=password)
        #if user is not None:
        if username=="admin" and password=="admin":
        
            auth.login(request, user)
            return redirect("/view")
        
        else:
            messages.info(request,'invalid credentials')
            return render(request, 'admin_login.html')

    else:
          
        return render(request, 'admin_login.html')

#user login
def user_login(request):
    if request.user.is_authenticated:
        return redirect("/user")
    elif request.method == 'POST':
        username= request.POST.get("username")
        password= request.POST.get("password")
        user = auth.authenticate(username=username,password=password)
        if user is not None:
        
            auth.login(request, user)
            return redirect("/user")
        
        else:
            messages.info(request,'invalid credentials')
            return render(request, 'user_login.html')

    else:
          
        return render(request, 'user_login.html')
        

#edit part
def edit(request, id):
    
    user = User.objects.get(id=id)
    return render(request, "edit.html",{'user': user})
   
#update a students data
def update(request, id):
    user = User.objects.get(id=id)
    if request.method == "POST":
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')
        username = request.POST.get('username')
      
        user.first_name = first_name
        user.last_name = last_name
        user.email = email
        user.username = username
       
        user.save()
        return redirect('/view')

    else:
 
        return render(request, "edit.html",{'user': user})


# def searchb(request):
#     #user = User.objects.all()
#     if request.method =='POST':
#         serch = request.POST['first_name']
#         users = User.objects.filter(first_name=serch)
#         return render(request, 'search.html',{'user':users})

#     else:
#         return redirect('/view')

#to add  student
def add(request):
    
    if request.method == "POST":
        
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        username = request.POST['username']
        password1 = request.POST['password1']
        
        if password1 == password1 :
            if User.objects.filter(username=username).exists():
                messages.info(request,'Username Taken')
                return HttpResponseRedirect(request.path_info)
            elif User.objects.filter(email=email).exists():
                messages.info(request,'Email Taken')
                return HttpResponseRedirect(request.path_info)
            else:
                user = User.objects.create_user(username=username,password=password1,email=email,first_name=first_name,last_name=last_name)
                user.save()
                return redirect(view)
            

    else:
            
        return render(request, 'add.html')



#def user(request):
   # user = User.objects.all()
    return render(request, "user.html",{'user': user})



"""class SearchView():
   
    template_name = 'search.html'log

    context_object_name = 'all_search_results'

    def get_queryset(self):
       result = super(SearchView, self).get_queryset()
       query = self.request.GET.get('search')
       if query:
          postresult = Article.objects.filter(title__contains=query)
          result = postresult
       else:
           result = None
       return result"""