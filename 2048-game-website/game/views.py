from django.shortcuts import render,redirect,get_object_or_404
from django.http import HttpResponse,Http404
from django.views.decorators.http import require_GET,require_POST,require_http_methods
from django.contrib.auth.decorators import login_required
@require_GET
@login_required
def base(request):
	return render(request,'game/2048.html')
def play(request)	:
	return render(request,'game/play.html')