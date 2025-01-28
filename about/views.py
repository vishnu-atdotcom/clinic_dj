from django.shortcuts import render
from django.views import View

class AboutView(View):
    def get(self, request):
        #print ('haisss')
        return render(request, "about/about.html")
    
class ServicesView(View):
    def get(self,request):
        return render (request,'about/service.html')

class ContactView(View):
    def get(self,request):
        return render (request,'about/contacts.html')