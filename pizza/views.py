from django.shortcuts import render
from .forms import PizzaForm, MultiPizzaForm
from django.forms import formset_factory
from .models import Pizza

# Create your views here.
def home(request):
    return render(request, 'pizza/home.html')

def order(request):
    #form = PizzaForm()
    multiple_form = MultiPizzaForm()
    if request.method=="POST":
        filled_form = PizzaForm(request.POST)
        if filled_form.is_valid():
            created_pizza = filled_form.save()
            created_pizza_pk = created_pizza.id
            note = f"Thanks for ordering! Your {filled_form.cleaned_data['size']} {filled_form.cleaned_data['topping1']} and {filled_form.cleaned_data['topping2']} pizza is on its way"
            filled_form.cleaned_data['topping1']
            filled_form.cleaned_data['topping2']
            filled_form = PizzaForm()
        else:
            created_pizza_pk = None
            note = 'Your pizza order was not created. Please try again.'
        return render(request, 'pizza/order.html', {'pizzaform': filled_form, 'note': note, 'multiple_form': multiple_form, 'created_pizza_pk': created_pizza_pk})
    else:
        form = PizzaForm()
        return render(request, 'pizza/order.html', {'pizzaform': form, 'multiple_form': multiple_form})
    
def pizzas(request):
    #form = PizzaForm()
    if request.method=="POST":
        filled_form = MultiPizzaForm(request.POST)
        if filled_form.is_valid():
            note = f"Thanks for ordering! Your {filled_form.cleaned_data['size']} {filled_form.cleaned_data['topping1']} and {filled_form.cleaned_data['topping2']} pizza is on its way"
        return render(request, 'pizza/order.html', {'pizzaform': PizzaForm(), 'note': note})
    else:
        return render(request, 'pizza/order.html', {'pizzaform': PizzaForm()})
    
def pizzas(request):
    print(request)
    number_of_pizzas = 2
    filled_multiple_pizza_form = MultiPizzaForm(request.GET)
    if filled_multiple_pizza_form.is_valid():
        number_of_pizzas = filled_multiple_pizza_form.cleaned_data["number"]
    PizzaFormSet = formset_factory(PizzaForm, extra=number_of_pizzas)
    formset = PizzaFormSet()
    if request.method == "POST":
        filled_formset = PizzaFormSet(request.POST)
        if filled_formset.is_valid():
            filled_formset.save()
            for form in filled_formset:
                print(form.cleaned_data['topping1'])

            note = 'Pizzas have been ordered'
        else:
            note = 'Order was not created, please try again'
        return render(request, 'pizza/pizzas.html', {'note': note, 'formset': formset})
    else:
        return render(request, 'pizza/pizzas.html', {'formset': formset})
    

def edit_order(request, pk):
    pizza = Pizza.objects.get(pk=pk)
    form = PizzaForm(instance=pizza)
    note = ""
    if request.method == 'POST':
        filled_form = PizzaForm(request.POST, instance=pizza)
        if filled_form.is_valid():
            filled_form.save()
            form = filled_form
            note = 'Order has been updated'
    return render(request, 'pizza/edit_order.html', {'pizzaform': form, 'pizza': pizza, 'note': note})

    