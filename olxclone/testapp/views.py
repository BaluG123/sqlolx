from django.shortcuts import render,get_object_or_404,redirect
from testapp.models import Item
from django.core.paginator import Paginator,PageNotAnInteger,EmptyPage
from testapp import forms
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required
def item_list_view(request):
    if "q" in request.GET:
        q=request.GET['q']
        item_list=Item.objects.filter(item_name__icontains=q)
    else:
        item_list=Item.objects.all()
    paginator=Paginator(item_list,8)
    page_number=request.GET.get('page')
    try:
        item_list=paginator.page(page_number)
    except PageNotAnInteger:
        item_list=paginator.page(1)
    except EmptyPage:
        item_list=paginator.page(paginator.num_pages)
    return render(request,'testapp/item_list.html',{'item_list':item_list})

def item_detail_view(request,item,year,month,day):
    item=get_object_or_404(Item,item_name=item,uploaded__year=year,uploaded__month=month,uploaded__day=day)
    return render(request,'testapp/item_detail.html',{'item':item})

def item_ormview(request):
    itemsb5=Item.objects.filter(price__lt=5000)
    paginator=Paginator(itemsb5,8)
    page_number=request.GET.get('page')
    try:
        itemsb5=paginator.page(page_number)
    except PageNotAnInteger:
        itemsb5=paginator.page(1)
    except EmptyPage:
        itemsb5=paginator.page(paginator.num_pages)
    return render(request,'testapp/itemb5.html',{'itemsb5':itemsb5})

def item_ormview1(request):
    itemsa5=Item.objects.filter(price__gte=5000)
    return render(request,'testapp/itema5.html',{'itemsa5':itemsa5})

def Item_addview(request):
    form=forms.CreateForm()
    if request.method=='POST':
        form=forms.CreateForm(request.POST,request.FILES or None)
        if form.is_valid():
            form.save(commit=True)
        return redirect('/home')
    return render(request,'testapp/create.html',{'form':form})

def Signup_view(request):
    form=forms.SignUpform()
    if request.method=='POST':
        form=forms.SignUpform(request.POST)
        if form.is_valid():
            user=form.save()
            user.set_password(user.password)
            user.save()
        return HttpResponseRedirect('/accounts/login')
    return render(request,'testapp/signup.html',{'form':form})

def logout_view(request):
    return render(request,'testapp/logout.html')
