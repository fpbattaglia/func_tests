from django.shortcuts import render, redirect
from lists.models import Item
# Create your views here.

def home_page(request):
    if request.method == 'POST':
        Item.objects.create(text=request.POST['item_text'])
        return redirect('/')

    items = Item.objects.all()
    print "no POST here "
    print "item count", len(items)
    return render(request, 'home.html',
        {'items': items})