from django.shortcuts import render
from django.http import HttpResponse
import pyrebase


# # Create your views here.

config = {
'apiKey': "AIzaSyBwW-C_eV_JvPdCsvz_otinNQk0zij_uGc",
'authDomain': "sachack-5a64d.firebaseapp.com",
'databaseURL': "https://sachack-5a64d.firebaseio.com",
'projectId': "sachack-5a64d",
'storageBucket': "sachack-5a64d.appspot.com",
'messagingSenderId': "955699483811",
'appId': "1:955699483811:web:69019444836d98e8641b16",
}
firebase = pyrebase.initialize_app(config)
auth = firebase.auth()

def signIn(request):
    return render(request, "signIn.html")


def postsign(request):
    email=request.POST.get('email')

    passw = request.POST.get("pass")
    try:
        user = auth.sign_in_with_email_and_password(email,passw)
    except:
        message = "invalid cerediantials"
        return render(request,"signIn.html",{"msg":message})

    print(user)
    return render(request, "welcome.html",{"e":email})


def index(request):
    context={
    }
    return render(request, "index.html", context=context)



