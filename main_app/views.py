from django.shortcuts import render
from django.views.generic.edit import CreateView
from .models import Cat
from .forms import FeedingForm
from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView

# Create your views here.
def home(request):
    '''
    this is where we return a repsonse 
    in most cases we would render a template
    '''

    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

# class Cat:  # Note that parens are optional if not inheriting from another class
#   def __init__(self, name, breed, description, age):
#     self.name = name
#     self.breed = breed
#     self.description = description
#     self.age = age


def cats_index(request):
  cats = Cat.objects.all()
  return render(request, 'cats/index.html', { 'cats': cats })

def cats_detail(request, cat_id):
  cat = Cat.objects.get(id=cat_id)
  # instantiate FeedingForm to be rendered in the template
  feeding_form = FeedingForm()
  return render(request, 'cats/detail.html', {
     'cat': cat, 'feeding_form': feeding_form 
    })

def add_feeding(request, cat_id):
    form = FeedingForm(request.POST)
    #validate the form
    if form.is_valid():
        # dont save the form to the db until is
        #h has the cat_id assigned
        new_feeding = form.save(commit=False)
        new_feeding.cat_id = cat_id
        new_feeding.save()
    return redirect('detail',cat_id=cat_id)

#the cud in crud
class CatCreate(CreateView):
  model = Cat
  fields = '__all__'
  success_url='/cats/'


class CatUpdate(UpdateView):
  model = Cat
  # Let's disallow the renaming of a cat by excluding the name field!
  fields = ['breed', 'description', 'age']

class CatDelete(DeleteView):
  model = Cat
  success_url = '/cats/'

