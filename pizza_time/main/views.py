from django.shortcuts import render, redirect, HttpResponse


def index(request):
    print('Quick Options')
    return render(request, 'index.html')


def order_new(request):
    print('INSIDE order_new METHOD')
    return render(request, 'order.html')


def order_create(request):
    print('INSIDE order_create METHOD')
    return redirect('/pizza')


def item_new(request):
    print('INSIDE item_new METHOD')
    return render(request, 'order.html')


def item_create(request):
    print('INSIDE item_create METHOD')
    return


def order_favorite(request):
    print('Order FAVORITE selected')
    return render(request, 'order.html')


def order_surprise(request):
    print('Order SURPRISE selected')
    return render(request, 'order.html')


def order_add_item(request):
    print('INSIDE order_add_item METHOD')
    print('request.POST.methood', request.POST['method'])
    print('request.POST.size', request.POST['size'])
    print('request.POST.crust', request.POST['crust'])
    print('request.POST.qty', request.POST['qty'])
    print('request.POST.mushrooms', request.POST['mushrooms'])
    print('request.POST', request.POST)
    return redirect('/pizza/order')


def order_process(request):
    print('Processing order')
    print('request.POST', request.POST)
    return render(request, 'checkout.html')


def order_checkout(request):
    print('Checkout')
    return render(request, 'checkout.html')
