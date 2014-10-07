import json
from django.contrib import messages
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.core.mail import EmailMultiAlternatives
from django.core.urlresolvers import reverse
from django.http import HttpResponse, HttpResponseForbidden, HttpResponseRedirect
from django.shortcuts import render, redirect, render_to_response
from django.template import RequestContext
from django.views.decorators.csrf import csrf_exempt
from love import settings
from squish import forms
from squish.forms import EmailUserCreationForm, DocumentForm
from squish.models import Document


def home(request):
    return render(request, 'index.html')


# def logout(request):
#     return render(request, 'registration/logout.html')

@login_required
def profile(request):
    return render(request, 'profile.html')


def register(request):
    if request.method == 'POST':
        form = EmailUserCreationForm(request.POST)

        if form.is_valid():
            # form.save()
            # data = json.loads(request.body)
            # user = User.objects.create(
            #     user_first_name=data['first_name'],
            #     user_last_name=data['last_name'],
            #     user_username=data['username'],
            #     user_email=data['email'],
            #     user_pasword1=data['password1'],
            #     user_password2=data['password2'],
            #     )
            # user = form.save()
            messages.info(request, 'Thanks for registering, you\'re now logged in.)')
            # user = authenticate(username=request.POST['username'],
            #                     password=request.POST['password'])
            user = User.objects.create_user(
                form.cleaned_data['first_name'],
                form.cleaned_data['last_name'],
                form.cleaned_data['username'],
                form.cleaned_data['email'],
            )
            user.email_user("Welcome!", "Thank you for signing up for our website.")
            text_content = 'Thank you for signing up for our website, {}'.format(user.username)
            html_content = '<h2>Thanks {} {} for signing up!</h2> <div>I hope you enjoy using our site. ' \
                           'You registered at {}.</div>'.format(user.first_name, user.last_name, user.date_joined)
            msg = EmailMultiAlternatives("Welcome!", text_content, settings.DEFAULT_FROM_EMAIL, [user.email])
            msg.attach_alternative(html_content, "text/html")
            msg.send()
            return redirect("profile")
    else:
        form = EmailUserCreationForm()

    return render(request, "registration/register.html", {
        'form': form,
    })
    # if request.method == 'POST':
    #     form = UserCreationForm(request.POST)
    #     if form.is_valid():
    #         form.save()
    #         return redirect('profile')
    #     else:
    #         form = UserCreationForm
    #     return render(request, "registration/register.html", {
    #         'form': form
    #     })


@csrf_exempt
def pay(request):
    return render(request, 'registration/payments.html')

@login_required()
def upload(request):
    # Handle file upload
    if request.method == 'POST':
        form = DocumentForm(request.POST, request.FILES)
        if form.is_valid():
            newdoc = Document(docfile = request.FILES['docfile'])
            newdoc.save()

            # Redirect to the document list after POST
            return HttpResponseRedirect(reverse('squish.views.profile'))
    else:
        form = DocumentForm()  # A empty, unbound form

    # Load documents for the list page
    documents = Document.objects.all()

    # Render list page with the documents and the form
    return render_to_response(
        'profile.html',
        {'documents': documents, 'form': form},
        context_instance=RequestContext(request)
    )

##### Snir example
# @login_required()
# def upload_pic(request):
#     if request.method == 'POST':
#         form = ImageUploadForm(request.POST, request.FILES)
#         if form.is_valid():
#             m = ExampleModel.objects.get(pk=image_id)
#             m.model_pic = form.cleaned_data['image']
#             m.save()
#             return HttpResponse('image upload success')
#     return HttpResponseForbidden('allowed only via POST')


def user_login(request):
    # Like before, obtain the context for the user's request.
    context = RequestContext(request)

    # If the request is a HTTP POST, try to pull out the relevant information.
    if request.method == 'POST':
        data = json.loads(request.body)
        user = User.objects.create(
            user_name=data['username'],
            user_password=data['password'],

        )
        # Gather the username and password provided by the user.
        # This information is obtained from the login form.
        username = request.POST['username']
        password = request.POST['password']

        # Use Django's machinery to attempt to see if the username/password
        # combination is valid - a User object is returned if it is.
        user = authenticate(username=username, password=password)

        # If we have a User object, the details are correct.
        # If None (Python's way of representing the absence of a value), no user
        # with matching credentials was found.
        if user:
            # Is the account active? It could have been disabled.
            if user.is_active:
                # If the account is valid and active, we can log the user in.
                # We'll send the user back to the homepage.
                login(request, user)
                return HttpResponseRedirect('profile')
            else:
                # An inactive account was used - no logging in!
                return HttpResponse("Your Sparq account is disabled.")
        else:
            # Bad login details were provided. So we can't log the user in.
            print "Invalid login details: {0}, {1}".format(username, password)
            return HttpResponse("Invalid login details supplied.")

    # The request is not a HTTP POST, so display the login form.
    # This scenario would most likely be a HTTP GET.
    else:
        # No context variables to pass to the template system, hence the
        # blank dictionary object...
        return render_to_response('registration/login.html', {}, context)
