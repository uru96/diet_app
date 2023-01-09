from django.shortcuts import render, redirect
from .models import Dish
from .forms import DishForm, DishIngredientsForm

# Create your views here.
# Zrobic inny widok na formularz skladnikowy
# widok ktory kieruje do innego widoku
# czyli nowy url

def dish_entry_view(request):
    if request.method == 'POST':
        dish_form = DishForm(request.POST)
        if dish_form.is_valid():
            print(dish_form.cleaned_data["dish_name"])
            print(dish_form.cleaned_data["dish_time"])
            a = dish_form.cleaned_data["dish_name"]

            # ingredient_form = DishIngredientsForm(initial={'hidden_field': a})
            # return render(request, 'dish-ingredients.html', {'ingredient_form': ingredient_form})
            return redirect('dish_ingredients_view', param=a)
    else:
        zmienna = DishForm()
        return render(request, 'home.html', context={"zmienna": zmienna})

# stworzyc widok skladnikow
def dish_ingredients_view(request, param):
    if request.method == 'POST':
        ingredients_form = DishIngredientsForm(request.POST)
        if ingredients_form.is_valid():
            print(param)
            print("chuj")
            return render(request, 'test.html')
    else:
        print(param)
        print("chuj")
        ingredients_form = DishIngredientsForm()
        return render(request, 'dish-ingredients.html', context={"ingredients_form": ingredients_form})



# def home(request):
#     #zmienna = 'duuuuuuuuuuuupa'
#
#     if request.method == 'POST':
#         # Jak dodalismy najpierw nazwe posilku i pore dnia
#         # czas na dodawanie skladnikow
#         dish_form = DishForm(request.POST)
#         if dish_form.is_valid():
#             print(dish_form.cleaned_data["dish_name"])
#             print(dish_form.cleaned_data["dish_time"])
#
#             if request.method == 'POST':
#                 print("wszedlem w posta")
#             else:
#                 print("nie wszedlem")
#             dish_ingredient_form = DishIngredientsForm()
#
#
#             return render(request, 'home.html', context={"dish_ingredient_form": dish_ingredient_form})
#         dish_ingredient_form = DishIngredientsForm(request.POST)
#         if dish_ingredient_form.is_valid():
#             print(dish_form.cleaned_data["dish_name"])
#             print(dish_form.cleaned_data["dish_time"])
#             print(dish_ingredient_form.cleaned_data["ingredient_name"])
#             print(dish_ingredient_form.cleaned_data["ingredient_weight"])
#             print(dish_ingredient_form.cleaned_data["ingredient_unit"])
#             zmienna = 'sadsadasdasdasdasd'
#             return render(request, 'home.html', context={"dish_ingredient_form": zmienna})
#
#
#             # Jezeli sa poprawne to tworzymy pusty formularz
#             # if request.method == 'POST':
#             #     print("jestem tutaj")
#             #     dish_ingredient_form = DishIngredientsForm(request.POST)
#             #     if dish_ingredient_form.is_valid():
#             #         print(dish_ingredient_form.cleaned_data["ingredient_name"])
#             #         print(dish_ingredient_form.cleaned_data["ingredient_weight"])
#             #         print(dish_ingredient_form.cleaned_data["ingredient_unit"])
#             #         return 'udalo sie'
#             # else:
#             #     dish_ingredient_form = DishIngredientsForm()
#             #     return render(request, 'home.html', context={"dish_ingredient_form": dish_ingredient_form})
#
#
#
#
#
#
#         # zmienna = 'formularz wyslany'
#         # return render(request, 'home.html', context={"zmienna": zmienna} )
#     else:
#         zmienna = DishForm()
#         return render(request, 'home.html', context={"zmienna": zmienna})
#     #
#     # dish = Dish(dish_id=1,
#     #             dish_name="sałatka z kurczakiem i pomarańczą",
#     #             dish_time="śniadanie",
#     #             dish_ingredient="pomarańcza",
#     #             ingredient_weight=200,
#     #             ingredient_unit='g')
#     #
#     # # all objects
#     # obj = Dish.objects.all()
#     # print(obj.__dict__)
#     #
#     # df = pd.DataFrame(obj)
#     # print(df.to_string())
#     # # type of query
#     # # print(type(obj))
#     # # # is iterable?
#     # # for obje in obj:
#     # #     #print(obje)
#     # #     print(obje.dish_ingredient)
#
#     #return render(request, 'home.html', context={"zmienna": zmienna} )