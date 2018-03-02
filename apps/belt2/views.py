from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.messages import get_messages
from models import *
import bcrypt

# Create your views here.
def index(request):
	return render(request, 'belt2/index.html')

def register(request):
	msgs = User.objects.regValidator(request.POST)
	if len(msgs):
		for k,v in msgs.iteritems():
			print k,v
		 	messages.error(request, v, extra_tags=k)
	else:
		hashedpw = bcrypt.hashpw(request.POST['password'].encode(), bcrypt.gensalt())
		User.objects.create(name = request.POST['name'], alias = request.POST['alias'], email=request.POST['email'], password=hashedpw, dob=request.POST['dob'])
		user = User.objects.last()
		request.session['logged_in'] = user.id
		print request.session['logged_in']
		return redirect('/quotes')

	return redirect('/')

def login(request):
	msgs = User.objects.loginValidator(request.POST)
	if len(msgs):
		print msgs
	else:
		user = User.objects.get(email=request.POST['login_email'])
		request.session['logged_in'] = user.id
		return redirect('/quotes')
	
	return redirect('/')

def logout(request):
	request.session.clear()
	return redirect('/')

def quotes(request):
	this_user = User.objects.get(id=request.session['logged_in'])
	context = {'user': this_user, 'my_quotes': this_user.liked_quotes.all(),'quotes': Quote.objects.exclude(liked_users=this_user)}
	return render(request, 'belt2/quotes.html', context)

def add_quote(request):
	msgs = Quote.objects.addValidator(request.POST)
	if len(msgs):
		for k,v in msgs.iteritems():
			print k,v
		 	messages.error(request, v, extra_tags=k)
	else:
		this_user = User.objects.get(id=request.session['logged_in'])
		Quote.objects.create(author=request.POST['author'],message=request.POST['message'], uploader=this_user)
		return redirect('/quotes')
	return redirect('/quotes')

def add_fav(request, id):
	this_quote = Quote.objects.get(id=id)
	this_user = User.objects.get(id=request.session['logged_in'])
	this_user.liked_quotes.add(this_quote)
	return redirect('/quotes')

def rm_fav(request, id):
	this_quote = Quote.objects.get(id=id)
	this_user = User.objects.get(id=request.session['logged_in'])
	this_user.liked_quotes.remove(this_quote)
	return redirect('/quotes')
	
def user(request, id):
	this_user = User.objects.get(id=id)
	return render(request, 'belt2/user.html', {'quotes': this_user.uploaded_quotes.all(), 'count': this_user.uploaded_quotes.count(), 'user': this_user})





