from django import forms
from .models import MyUser
from django.contrib.auth import authenticate
class loginform(forms.Form):
	username=forms.CharField(max_length=100)
	password=forms.CharField(widget=forms.PasswordInput,max_length=100)
	def __init__(self,*args,**kwargs):
		self.authenticated_user=None
		super(loginform,self).__init__(*args,**kwargs)
	def clean_username(self):
		username=self.cleaned_data.get('username','')
		if MyUser.objects.filter(username=username).count()!=1:
			raise forms.ValidationError('Invalid username')
		return username
	def clean(self):
		username=self.cleaned_data.get('username','')		
		password=self.cleaned_data.get('password','')
		user=authenticate(username=username,password=password)
		if username and password and not user:
			raise forms.ValidationError('Invalid username or password')
		self.authenticated_user=user
		if user and (user.is_active==False):
			raise forms.ValidationError('user is inactive')
		return self.cleaned_data
class forgetpasswordform(forms.Form):
	username=forms.CharField(max_length=100)
	def clean_username(self):
		username=self.cleaned_data.get('username','')
		if username and MyUser.objects.filter(username=username).count()!=1	:
			raise forms.ValidationError('Invalid username')
		return self.cleaned_data['username']
class resetform(forms.Form)		:
	newpassword=forms.CharField(widget=forms.PasswordInput)
	confirmpassword=forms.CharField(widget=forms.PasswordInput) 
	def clean(self):
		if not (self.cleaned_data['newpassword']==self.cleaned_data['confirmpassword']):
			raise forms.ValidationError('new password and confirm password doesnot match')
		else:
			return self.cleaned_data	
class signupform(forms.ModelForm):
	password=forms.CharField(widget=forms.PasswordInput)
	confirmpassword=forms.CharField(widget=forms.PasswordInput)
	def clean_username(self):
		if MyUser.objects.filter(username=self.cleaned_data['username']).exists():
			raise forms.ValidationError('User already excists')
		return self.cleaned_data['username']
	def clean_email(self):
		email=self.cleaned_data.get('email')
		if not email:
			raise forms.ValidationError('requires email')
		if MyUser.objects.filter(email=email).exists():
			raise forms.ValidationError('This email is already registered')	
		email=self.cleaned_data['email']	
		return email
	def clean(self)		:
		passwd=self.cleaned_data.get('password','')
		confirmpasswd=self.cleaned_data.get('confirmpassword','')
		if (passwd==confirmpasswd):
			return self.cleaned_data
		raise forms.ValidationError('passwords doenot match')
	class Meta:
		model=MyUser
		fields=['username','first_name','last_name','phone','email']
class changepasswordform(forms.Form)		:
	current_password=forms.CharField(widget=forms.PasswordInput)
	new_password=forms.CharField(widget=forms.PasswordInput)
	confirm_password=forms.CharField(widget=forms.PasswordInput)
	def __init__(self,*args,**kwargs):
		self.user=kwargs.pop('user','')
		super(changepasswordform,self).__init__(*args,**kwargs)
	def clean_current_password(self):
		username=self.user.username
		password=self.cleaned_data['current_password']
		tuser=authenticate(username=username,password=password)
		if not tuser:
			raise forms.ValidationError('Invalid Password')
		return self.cleaned_data	

	def clean(self)	:
		passwd=self.cleaned_data.get('password','')
		confirmpasswd=self.cleaned_data.get('confirmpassword','')
		if (passwd==confirmpasswd):
			return self.cleaned_data
		raise forms.ValidationError('passwords doenot match')





