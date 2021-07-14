from django.shortcuts import render
from django.http import HttpResponse

DATA = {
    'omlet': {
        'яйца, шт': 2,
        'молоко, л': 0.1,
        'соль, ч.л.': 0.5,
    },
    'pasta': {
        'макароны, г': 0.3,
        'сыр, г': 0.05,
    },
    'buter': {
        'хлеб, ломтик': 1,
        'колбаса, ломтик': 1,
        'сыр, ломтик': 1,
        'помидор, ломтик': 1,
    },
    # можете добавить свои рецепты ;)
}


def calculator_recipes_view(request, recipe):
    servings = request.GET.get("servings", 1)
    context = {
        'recipe': {a: b * servings for a, b in DATA.get(recipe).items()},
    }
    print(context)
    print(servings)
    return render(request, 'calculator/index.html', context)

