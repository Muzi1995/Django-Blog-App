# from django.http import HttpResponse

from django.shortcuts import render

# This imports HttpResponse, which is a Django class used to send back raw text (HTML or plain) to the browser.
# Think of it as a package 📦 you send back to the user when they visit your site.


def homepage(request):
    # return HttpResponse("Home Page")
    return render(request, 'home.html')

# Defines a Python function called homepage.
# It takes one argument: request.
# The request object contains everything about what the user is asking for (browser info, URL, data they sent, etc.).
# return HttpResponse("Home Page")
# Sends a response back to the user’s browser.
# In this case, the response is just text: “Home Page”.
# If you visit http://localhost:8000/, this is what you’ll see.


def about(request):
    # return HttpResponse("About")
    return render(request, 'about.html')

# Similar to homepage, this defines another function.
# If someone visits /about/, Django calls this function.
# It returns the text: “About”.
