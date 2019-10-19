from django.shortcuts import render,redirect,get_object_or_404
from django.http import HttpResponse,Http404
from django.views.decorators.http import require_GET,require_POST,require_http_methods
from django.core.urlresolvers import reverse
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout
from django.contrib.auth.decorators import login_required
from .forms import loginform , forgetpasswordform,resetform,signupform,changepasswordform
from .models import create_otp,MyUser,UserOtp
from django.core.mail import EmailMultiAlternatives
from django.template import loader
from django.conf import settings
@require_http_methods(['GET','POST'])
def login(request)	:
	if request.user.is_authenticated():
		return redirect(reverse('home',kwargs={'id':request.user.id}))
	username=request.POST.get('username','')	
	password=request.POST.get('password','')
	if request.method=='GET':
		f=loginform()
		return render(request,'account/login.html',{'form':f})
	else:
		f=loginform(request.POST)
		if not f.is_valid():
			return render(request,'account/login.html',{'form':f})
		else:	
			user=f.authenticated_user
			auth_login(request,user)
			return redirect(reverse('home',kwargs={'id':user.id}))
@require_GET
@login_required				
def home(request,id):
	if request.user.is_authenticated():
		return render(request,'game/2048.html')
	else:
		return redirect(reverse('login'))
@require_GET			
def logout(request)	:
	if request.user.is_authenticated():
		auth_logout(request)	
	return redirect(reverse('login'))
def forgetpassword(request):
	if request.user.is_authenticated():
		return redirect(reverse('home',kwargs={'id':request.user.id}))
	if (request.method=='GET'):
		f=forgetpasswordform()
		return render(request,'account/forget.html',{'f':f})
	if(request.method=='POST')	:
		f=forgetpasswordform(request.POST)
		if not f.is_valid():
			return render(request,'account/forget.html',{'f':f})
		else:
			username=f.cleaned_data['username']
			user=MyUser.objects.get(username=username)
			otp=create_otp(user,'FP')
			email_body_context = { 'u' : user, 'otp' : otp}
			body = loader.render_to_string('account/forgot_password.txt', email_body_context)
			message = EmailMultiAlternatives("Reset Password", body, settings.EMAIL_HOST_USER, [user.email])
			message.send()
			return render(request,'account/emailsent.html',{'u':user}) 
def reset(request,id=None,otp=None):
	if (request.method=='GET'):
		if request.user.is_authenticated():
			return redirect('home',{'id':id})
		user=MyUser.objects.get(id=id)	
		if 	not user :
			raise Http404
		if  UserOtp.objects.filter(user=user,otp=otp).exists():

			userobject=UserOtp.objects.get(user=user,otp=otp)
			userobject.delete()
			f=resetform()
			return render(request,'account/reset.html',{'f':f,'uid':id,'otp':otp})
		else:
			raise Http404
	if(request.method=='POST')		:
		if request.user.is_authenticated():
			return redirect('home',{'id':id})
		f=resetform(request.POST)
		if not f.is_valid():
			user=MyUser.objects.get(id=id)
			return render(request,'account/reset.html',{'f':f,'uid':id,'otp':otp})
		else:
			user=MyUser.objects.get(id=id)
		if not user:
			raise Http404
		else:
			password=f.cleaned_data['newpassword']
			user.set_password(password)
			user.save()
			return render(request,'account/passwordchanged.html',{'u':user})
@require_http_methods(['GET','POST'])
def signup(request):
	if request.user.is_authenticated():
		return redirect('home',{'id':request.user.id})	
	if (request.method=='GET')	:
		f=signupform()
		return render(request,'account/signup.html',{'f':f})
	if (request.method=='POST')	:
		f=signupform(request.POST,request.FILES)
		if not f.is_valid():
			return render(request,'account/signup.html',{'f':f})
		userobj=f.save(commit=False)	
		userobj.is_active=False
		userobj.set_password(f.cleaned_data['confirmpassword'])
		userobj.save()

		username=f.cleaned_data['username']
		user=MyUser.objects.get(username=username)
		otp=create_otp(user,'AA')
		email_body_context = { 'u' : user, 'otp' : otp}
		body = loader.render_to_string('account/activation.txt', email_body_context)
		message = EmailMultiAlternatives("Reset Password", body, settings.EMAIL_HOST_USER, [user.email])
		message.send()
		return render(request,'account/emailsent.html',{'u':user})
@require_GET		
def activate(request,id=None,otp=None)	:
	if request.user.is_authenticated():
		return redirect('home',{'id':request.user.id})
	user=get_object_or_404(MyUser,id=id)
	if user and not UserOtp.objects.filter(user=user,otp=otp,purpose='AA').exists():
		raise Http404('invalid OTP')
	otpobj=UserOtp.objects.get(user=user,otp=otp,purpose='AA')
	otpobj.delete()
	user.is_active=True
	user.save()
	return render(request,'account/activated.html',{'u':user})
@require_http_methods(['GET','POST'])	
@login_required
def change(request):
	if (request.method=='GET'):
		f=changepasswordform()
		return render(request,'account/changepassword.html',{'f':f})

	if(request.method=='POST')	:
		f=changepasswordform(request.POST,user=request.user)
		if not f.is_valid():
			return render(request,'account/changepassword.html',{'f':f})
		else:
			user=request.user
			user.set_password(f.cleaned_data['new_password'])
			user.save()
			auth_logout(request)
			return render(request,'account/passwordchanged.html')
			
				





        	


	


