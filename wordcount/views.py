from django.http import HttpResponse
from django.shortcuts import render
#def home(request):
#	return HttpResponse("<h1>Hi Ramesh</h1>")

def home(request):
	return render(request,'home.html')

def Aboutus(request):
	return render(request,'Aboutus.html')

def count(request):
	fulltext=request.GET['fulltext']
	words=fulltext.split()
	dictionary={}
	for word in words:
		if word in dictionary:
			#increase
			dictionary[word]+=1
		else:
			#add
			dictionary[word]=1
	return render(request,'count.html',{'fulltext':fulltext,'count':len(words),'dictionary':dictionary.items()})