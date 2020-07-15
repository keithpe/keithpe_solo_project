from django.shortcuts import render, redirect, HttpResponse
from login.models import *
from django.contrib import messages
import bcrypt


def index(request):

    return render(request, "login.html")


def register(request):
    return render(request, "register.html")


def registration(request):
    # Process the registration form

    request.session['process'] = request.POST['process']

    errors = User.objects.basic_validator(request.POST)

    if errors:
        # Loop through each key-value pair and make a flash message
        for key, value in errors.items():
            messages.error(request, value)

            # Save form info so we can display it back in the form when we get redirected.
            request.session['first_name'] = request.POST['first_name']
            request.session['last_name'] = request.POST['last_name']
            request.session['alias_name'] = request.POST['alias_name']
            request.session['email'] = request.POST['email']
            request.session['birthday'] = request.POST['birthday']

        # redirect the user back to the form to fix the errors
        return redirect('/register')

    # Use bcrytp to create a hash for this password and store the hashed value into our database
    # with the rest of the user information
    password = request.POST['password']
    pw_hash = bcrypt.hashpw(password.encode(), bcrypt.gensalt()).decode()

    # Create the user record for this new user,
    this_user = User(first_name=request.POST['first_name'],
                     last_name=request.POST['last_name'], alias_name=request.POST['alias_name'], email=request.POST['email'], password=pw_hash, birthday=request.POST['birthday'])

    # And save it.
    this_user.save()

    # Save the first name so we can display it on the success page.
    request.session['userid'] = this_user.id
    request.session['first_name'] = this_user.first_name
    request.session['last_name'] = this_user.last_name
    request.session['alias_name'] = this_user.alias_name

    # Set a session variable to indicate that we've successfully logged in. (access to success page will require it.)
    request.session['status'] = 'success'

    # return redirect('/success')
    return redirect('/pizza')


def login(request):
    # Process the login form
    request.session.flush()

    request.session['process'] = request.POST['process']

    # See if the user email exists in the database
    user = User.objects.filter(email=request.POST['email'])

    # If user array is not empty, then get the first user (0)
    if user:
        logged_user = user[0]

        # Use bcrypt's check_password_hash method, passing the hash from our dataase and password from the form
        if bcrypt.checkpw(request.POST['password'].encode(), logged_user.password.encode()):

            # if we get True after checking the password, we may put the user id in session
            request.session['userid'] = logged_user.id
            request.session['first_name'] = logged_user.first_name
            request.session['last_name'] = logged_user.last_name
            request.session['alias_name'] = logged_user.alias_name
            request.session['invalid_account'] = ''

            # Set a session variable to indicate that we've successfully logged in. (access to success page will require it.)
            request.session['status'] = 'success'

            # return redirect('login/success')
            return redirect('/pizza')
        else:
            request.session['invalid_account'] = 'Username or password is incorrect'
            return redirect('/')

    else:
        request.session['invalid_account'] = 'Username or password is incorrect'

    return redirect('/')


def logout(request):
    # Process the logout
    request.session.flush()
    return redirect('/')


def success(request):
    # Check if the status key exists in the request.session dictionary.
    # If it doesn't or if it's not set to 'success' than we'll redirect to the login page
    # We don't want someone to be able to access this page from their browser UNLESS they successfully login to the server
    if 'status' in request.session:
        if request.session['status'] != 'success':
            request.session.flush()
            return redirect('/')
    else:
        return redirect('/')

    return render(request, 'success.html')


def pizza(request):
    return render(request, 'pizza.html')
