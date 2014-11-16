from django.shortcuts import render
# Create your views here.

def home_page(request):
    ret_item = request.POST.get('item_text', '')
    if ret_item:
        ret_item = "1: " + ret_item

    return render(request, 'home.html',
        {'new_item_text': ret_item})