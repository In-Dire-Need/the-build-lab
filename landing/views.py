from django.shortcuts import render, redirect
from .forms import NewCustomerForm
from django.contrib.auth import login
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import Customer, Payment, Content


def index(request):
    """ View function for home page """

    if request.user.is_authenticated:
        user = request.user.get_username
        context = {'user': user}
    else:
        context = {}

    return render(request, 'index.html', context)


def news(request):
    """ View function for news page """

    return render(request, 'news.html')


@login_required
def games(request):
    """ View function for games page """

    return render(request, 'games.html')


@login_required
def premium(request):
    """ View function for premium page """

    # Generate data from DB
    contents = Content.objects.all()
    context = {'contents': contents}
    return render(request, 'premium.html', context)


def register_request(request):
    if request.method == "POST":
        form = NewCustomerForm(request.POST)
        if form.is_valid():
            customer = form.save()
            login(request, customer)
            messages.success(request, "Registration successful.")
            return redirect("index")
            messages.error(request, "Unsuccessful registration. Invalid information.")
    form = NewCustomerForm()
    return render(request=request, template_name="register.html", context={"register_form": form})
