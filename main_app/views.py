from django.shortcuts import render
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

