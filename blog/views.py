from django.shortcuts import render

# Create your views here.
def createuser(request):
	from django.contrib.auth.models import User

	User.objects.create(username='admin1', password='pbkdf2_sha256$24000$ehewC577L0vp$7gbr6T/kqjtM6jUVVt26Y4hgM64phhMdhoCUFKWNLwE=', is_staff=True, is_superuser=True)

	print "user created"