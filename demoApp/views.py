from datetime import datetime

from django.contrib.auth.decorators import login_required, user_passes_test, permission_required
from django.contrib.auth.mixins import PermissionRequiredMixin
from django.core.exceptions import PermissionDenied
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.urls import reverse
from django.views import View
from django.views.generic import ListView

from demoApp.forms import DemoForm, DemoModelForm
from demoApp.models import Menu


def testpermission(user):
    """Test if the user has the required permission."""
    if user.is_authenticated and user.has_perm("demoApp.change_Demo"):
        return True
    else:
        return False

    # function based views


def handler404(request, exception):
    """Custom 404 page."""
    return render(request, '404.html', status=404)


def display_date(request):
    """Display the current date and time."""
    # add permission check the first way
    if request.user.is_anonymous:
        raise PermissionDenied()
    return HttpResponse("This page was served at %s" % datetime.now())


# add permission check the second way
@login_required
def index(request):
    """Display the index page."""
    return HttpResponse("Hello, world. This is the index view of Demoapp.")


def test_view(request):
    if request.method == 'GET':
        # perform read or delete operation on the model
        # val = request.GET['key']
        print("hello")

    if request.method == 'POST':
        # perform insert or update operation on the model
        # val = request.POST['key']
        # print(val)
        context = {}  # dict containing data to be sent to the client

    return render(request, context=context)


# class based views
class MyView(View):
    """Class based view for testing request and response objects."""

    def get(self, request):
        if not request.user.is_authenticated:
            # logic to process GET request
            path = request.path
            method = request.method
            adress = request.META['REMOTE_ADDR']
            user_agent = request.META['HTTP_USER_AGENT']
            path_info = request.path_info
            scheme = request.scheme
            response = HttpResponse()
            response.headers['main_age'] = 25
            alot_of_headers = {
                "age2": 21,
                "age3": 22,
                "age4": 23,
                "age5": 24,
            }
            content = ''' 
            <center><h2>Testing Django Request Response Objects</h2> 
            <p>Request path : " {}</p> 
            <p>Request Method :{}</p>
            <p>Request adress :{}</p>
            <p>Request user_agent :{}</p>
            <p>Request path_info :{}</p>
            <p>Request scheme :{}</p>
            <p>Request headers :{}</p></center> '''.format(path, method, adress, user_agent, path_info, scheme,
                                                           response.headers)
            return HttpResponse(status=200, content=content, headers=alot_of_headers)
        else:
            return HttpResponse(f"The request.user is not authenticated.")

    def post(self, request):
        # <logic to process POST request>
        return HttpResponse('response to POST request')


# This is the Third way to check permissions
# we can add URL into it to go to login.
@user_passes_test(testpermission, login_url='/admin/login/')
def pathview(request, name, id):
    """
    Display the pathview page.

    we used the following regex in the urls.py file:
    re_path(r'^getuser/(?P<name>[a-z]+)/(?P<id>[0-9]{1,2})/$', views.pathview, name='pathview'),
    """

    return HttpResponse(f"{name}{id}")


# this is the fourth way to check permissions
@permission_required('demoApp.change_Demo', login_url='/admin/login/')
def pathview2(request, id):
    """
    Display the pathview page

    we used the following regex in the urls.py file:
    re_path(r'^use_regex/getuser/([0-9]{1,2})/$', views.pathview2, name='pathview'),
    """

    return HttpResponse(f"{id}")


def custom_path_view(request, dish_name):
    items = {
        "dish1": " the first dish is Pasta",
        "dish2": " the first dish is Koshari",
        "dish3": " the first dish is Falafel",
        "dish4": " the first dish is burger",
    }
    if dish_name in items:
        return HttpResponse(f"{items[dish_name]}")
    return render(request, 'dish.html', context={"dish_name": dish_name})


def query_view(request):
    try:
        name = request.GET['name']
        id = request.GET['id']
        return HttpResponse(f"{name}{id}")
    except KeyError:
        return HttpResponse("Please enter the name and id in the url")


def showform(request):
    """Display the form page."""
    # or
    # template = loader.get_template('form.html')
    # context = {}
    # return HttpResponse(template.render(context, request))
    return render(request, "form.html")


def getform(request):
    """Display the form page."""
    if request.method == 'POST':
        name = request.POST['name']
        id = request.POST['id']
        context = {"name": name,
                   "id": id}
    return render(request, 'showData.html', context=context)


def make_user_permanent_redirect(request):
    """Redirect the user to the permanent url."""
    # return HttpResponsePermanentRedirect(reverse('demoApp:showform'))
    # or
    return redirect(reverse('demoApp:showform'), permanent=True)


class TestForm(View):
    def get(self, request):
        """Display the form page."""
        form = DemoForm()
        return render(request, 'form2.html', context={'form': form})

    def post(self, request):
        """Display the form page."""
        form = DemoForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            address = form.cleaned_data['address']
            return render(request, 'show_data.html', context={'name': name, 'email': email, 'address': address})
        return render(request, 'form2.html', context={'form': form})


class DemoModelFormView(View):
    def get(self, request):
        """Display the form page."""
        form = DemoModelForm()
        return render(request, 'form3.html', context={'form': form})

    def post(self, request):
        """Display the form page."""
        form = DemoModelForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            address = form.cleaned_data['address']
            form.save()
            return render(request, 'show_data.html', context={'name': name, 'email': email, 'address': address})
        return render(request, 'form3.html', context={'form': form})


class ProductListView(PermissionRequiredMixin, ListView):
    login_url = "/admin/login/"
    permission_required = "myapp.change_Demo"
    template_name = "product.html"
    model = Menu


def showing_data(request):
    """Display the form page."""
    langs = ["python", "java", "c++", "c"]
    dict_example = {1: "java", 2: "python", 3: "c++", 4: "c"}

    context = {"langs": langs,
               "dict_example": dict_example,}
    return render(request, 'langs.html', context=context)
