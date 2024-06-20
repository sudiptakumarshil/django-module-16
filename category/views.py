from django.shortcuts import render,redirect
from category.forms import CategoryForm
from django.contrib import messages

# Create your views here.
def add_category(request):
    if request.method == 'POST':
        category_form = CategoryForm(request.POST)
        if category_form.is_valid():
            category_form.save()
            messages.success(request, 'Category saved successfully!')
            return redirect('category.add')

    form = CategoryForm
    return render(request,'add_category.html',{'form':form})