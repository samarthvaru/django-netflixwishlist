from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import *
from .forms import *
from .filters import *
from .decorators import *
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
# Create your views here.


@unauthenticated_user
def registerPage(request):

    form=CreateUserForm()

    if request.method=='POST':
        form=CreateUserForm(request.POST)
        if form.is_valid() :
            user=form.save()

            username=form.cleaned_data.get('username')

            messages.success(request,"Account was created for"+username)
            return redirect('login')

    context={'form':form }
    return render(request,'accounts/register.html',context)






@unauthenticated_user
def loginPage(request):

    if(request.method=='POST'):
        username=request.POST.get('username')
        password=request.POST.get('password')
        user=authenticate(request,username=username,password=password)
        if user is not None:
            login(request,user)
            return redirect('userPage')
        else:
            messages.info(request,'username or password is incorrect')

    context={}
    return render(request,'accounts/login.html',context)


def logoutUser(request):
    logout(request)

    return redirect('login')




@login_required(login_url='login')
def userPage(request):

    orders=request.user.customer.listitem_set.all()
    items=orders.all()
    total_movies=items.count()
    movies_watched=items.filter(note='Watched').count()
    movies_pending=total_movies-movies_watched
    context={'items':items,'total_movies':total_movies,'movies_watched':movies_watched,'movies_pending':movies_pending}
    return render(request,'accounts/userPage.html',context)



@login_required(login_url='login')
def accountSettings(request):
    customer=request.user.customer
    form=UserForm(instance=customer)

    if request.method=='POST':
        form=UserForm(request.POST,request.FILES,instance=customer)
        if form.is_valid():
            form.save()

    context={'form':form}
    return render(request,'accounts/account_settings.html',context)




@login_required(login_url='login')
def listAddPage(request):
    customer=request.user.customer

    form = ListForm(initial={'customer': customer})

    if request.method == 'POST':
        form=ListForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    context={'form':form,'customer':customer}
    return render(request,'accounts/listAdd.html',context)


@login_required(login_url='login')
def updateList(request,pk):


    listitem = ListItem.objects.get(id=pk)
    form = UpdateForm(instance=listitem)
    if request.method == 'POST':
        form = UpdateForm(request.POST, instance=listitem)
        if form.is_valid()==True:

            form.save()
            return redirect('/')

    context = {'form': form}

    return render(request,'accounts/update_form.html',context)


@login_required(login_url='login')
def deleteList(request,pk):
    listitem = ListItem.objects.get(id=pk)
    if request.method == 'POST':
        listitem.delete()
        return redirect('/')

    context = {'item': listitem}
    return render(request, 'accounts/delete.html', context)


@login_required(login_url='login')
def filterList(request):
    customer = request.user.customer
    listItem=customer.listitem_set.all()
    myFilter = ListFilter(request.GET, queryset=listItem)
    item = myFilter.qs
    context={'myFilter':myFilter,'items':item }
    return render(request,'accounts/filterPage.html',context)







