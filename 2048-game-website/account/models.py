from django.db import models
from django.contrib.auth.models import AbstractUser
from random import randint

# Create your models here.
class MyUser(AbstractUser):
	phone=models.CharField(max_length=10,null=True)
	#profile_pic = models.ImageField(upload_to = 'profile_pics/', null=True, blank=True)
	class meta:
		verbose_name='MyUser'
class UserOtp(models.Model):
	OTP_PURPOSE_CHOICES = (
       ('FP', 'Forgot Password'),
      ('AA', 'Activate Account'),)
	user = models.ForeignKey(MyUser)
	otp = models.CharField(max_length = 4)
	purpose = models.CharField(max_length = 2, choices = OTP_PURPOSE_CHOICES)
	created_on = models.DateTimeField(auto_now_add = True)
	class Meta:
		unique_together= ['user', 'purpose']	
def create_otp(user=None,purpose=None):
	if not user:
		raise ValueError('invalid arguments')   
	choices=[]
	for user_purpose ,verbose in UserOtp.OTP_PURPOSE_CHOICES:
		choices.append(user_purpose)
	if purpose not in choices:
		raise ValueError('invalid arguments')	
	if UserOtp.objects.filter(user=user,purpose=purpose).exists():
		UserOtpObject=UserOtp.objects.get(purpose=purpose,user=user)
		UserOtpObject.delete()
	otp=randint(1000,9999)
	UserOtpObject=UserOtp.objects.create(user=user,purpose=purpose,otp=otp)
	UserOtpObject.save()
	return otp



