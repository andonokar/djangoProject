from django.http import HttpResponse
from django.shortcuts import render

from recipes.utils.factory import make_recipe


# Create your views here.
def home(request):
    return render(request, 'home.html', context={
        "recipes": [make_recipe() for _ in range(10)]
    })


def recipes(request, id):
    return render(request, 'recipe-view.html', context={
        "recipe": make_recipe(),
        "is_detail_page": True
    })
