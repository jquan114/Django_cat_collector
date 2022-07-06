from django.shortcuts import render
from django.views.generic.edit import CreateView
from .models import Cat

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
  return render(request, 'cats/detail.html', { 'cat': cat })

#the cud in crud
class CatCreate(CreateView):
  model = Cat
  fields = '__all__'

