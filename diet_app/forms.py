from django import forms


class DishForm(forms.Form):
    dish_name = forms.CharField(max_length=200)
    dish_time = forms.CharField(max_length=200)


class DishIngredientsForm(forms.Form):
    ingredient_name = forms.CharField(max_length=200)
    ingredient_weight = forms.IntegerField()
    ingredient_unit = forms.CharField(max_length=200)
