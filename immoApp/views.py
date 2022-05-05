from django.shortcuts import render

def home(request): 
    return render(request, 'EstateAgency/EstateAgency/index.html')

def about(request):   
    return render(request,'EstateAgency/EstateAgency/about.html' )

def contact(request):     
    return render(request,'EstateAgency/EstateAgency/contact.html' )

def agentSingle(request):         
    return render(request,'EstateAgency/EstateAgency/agent-single.html' )

def agentGrid(request):       
    return render(request,'EstateAgency/EstateAgency/agents-grid.html' ) 

def propertySingle(request):        
    return render(request,'EstateAgency/EstateAgency/property-single.html' )

def propertyGrid(request):          
    return render(request,'EstateAgency/EstateAgency/property-grid.html' )

def blogSingle(request):     
    return render(request,'EstateAgency/EstateAgency/blog-single.html' )

def blogGrid(request):     
    return render(request,'EstateAgency/EstateAgency/blog-grid.html')


# Create your views here.
