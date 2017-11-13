from django.shortcuts import render, HttpResponse, redirect
from django.utils.crypto import get_random_string


def index(request):
	context = {
		'unique' : get_random_string(length = 12, allowed_chars='ACTG')
	}
	return render(request, 'randWord/index.html', context)


def refresh(request):
	if request.method == "POST":
		if 'counterforgame' in request.session:
			request.session['counterforgame'] += 1
			return redirect('/')
		else:
			request.session['counterforgame'] = 1
			return redirect('/')
	else:
		return redirect ('/')
# Create your views here.
