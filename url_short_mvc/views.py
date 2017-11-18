from django.shortcuts import render
from django.http import HttpResponse
from random import choice
from .models import URL
import string


def home(request):
	return render(request, "index.html")


def shorten(request):
	full_url = request.POST["url"]
	char = string.ascii_uppercase + string.digits + string.ascii_letters
	url_short_id = "".join(choice(char) for _ in range(6))
	short_url = "http://127.0.0.1:8000/{0}".format(url_short_id)
	url_service = URL(short_url=short_url, full_url=full_url, url_short_id=url_short_id)
	url_service.save()
	return HttpResponse("Success " + "<a href='{0}'>{0}</a>".format(short_url))


def redirect(request, short_id):
	return HttpResponse("Full URL: <a href='{0}'>{0}</a>".format(URL.get_full_url(short_id)))
