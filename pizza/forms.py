from django import forms 
from .models import  Pizza, Size


class PizzaForm1(forms.Form):
    topping1 = forms.CharField(label='Topping 1', max_length=100)
    topping2 = forms.CharField(label='Topping 2', max_length=100)
    #toppings = forms.MultipleChoiceField(choices=[('pep', 'Pepperoni'),('cheese', 'Cheese'), ('mush', 'Mushrooms'), ('olives', 'Olives')], widget=forms.CheckboxSelectMultiple)
    size = forms.ChoiceField(label='Size', choices=[('Small','Small'),('Meddium','Medium'),('Large','Large')])

class PizzaForm(forms.ModelForm):
   
    size = forms.ModelChoiceField(queryset=Size.objects, empty_label=None)
    #image = forms.ImageField()
    class Meta:
        model = Pizza
        fields = ['topping1','topping2','size']
        labels = {"topping1":'Topping 1', 'topping2': 'Topping 2'}
        #widgets = {'topping1':forms.CheckboxSelectMultiple}

class MultiPizzaForm(forms.Form):
    number = forms.IntegerField(min_value=2, max_value=6)
