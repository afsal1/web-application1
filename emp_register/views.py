from django.shortcuts import render,redirect
from emp_register.forms import Emp_form
from emp_register.models import Emp_register


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


def emp(request):
    if request.method == "POST":
        form = Emp_form(request.POST)
        if form.is_valid():
            try:
                form.save()
                return redirect('/view')
            except:
                pass

    else:
        form = Emp_form()

    return render(request, 'index.html', {'form': form})

def view(request):
    emp_register = Emp_register.objects.all()
    return render(request, "view.html",{'emp_register': emp_register})


def delete(request, id):
    emp_register = Emp_register.objects.get(id=id)
    emp_register.delete()
    return redirect("/view/")



def edit(request, id):
    
    emp_register = Emp_register.objects.get(id=id)
    return render(request, "edit.html",{'emp_register': emp_register})
   

def update(request, id):

    #form = Emp_form(request.POST)
    #print(form)
    emp_reg = Emp_register.objects.get(id=id)
    #emp_register.f= form

    emp_reg.save()
    return render(request, "view.html",{'emp_register': emp_reg})
   

def add(request):
    if request.method == "POST":
        form = Emp_form(request.POST)
        if form.is_valid():
            try:
                form.save()
                return redirect('/view')
            except:
                pass

    else:
        form = Emp_form()

    return render(request, 'index.html', {'form': form})


def user(request):
    emp_register = Emp_register.objects.all()
    return render(request, "user.html",{'emp_register': emp_register})



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