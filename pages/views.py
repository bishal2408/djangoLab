from django.shortcuts import render,get_object_or_404
from property.models import Property
from query.models import Query
from agent.models import Agent
# Create your views here.
from django.http import HttpResponse

def home(request):
    featured_property = Property.objects.filter(featured=True)[:4]
    latest_property = Property.objects.order_by('id')[:4]
    agents = Property.objects.filter(agent=1)
    return render(request, 'pages/index.html', {
        'featured': featured_property,
        'latest': latest_property,
        'agent_properties': agents
    })

def about(request):
    propertyList = Property.objects.all
    return render(request, 'pages/about.html', {'title': 'Shyam', 'properties': propertyList})

def property_details(request, propertyId):
    property_details = get_object_or_404(Property, pk=propertyId)
    latest_property = Property.objects.order_by('id')[:4]
    context = {
        "property": property_details,
        'latest': latest_property,
    }
    return render(request, 'pages/details.html', context)



def contact(request):
    def sendMessage(request, property_id):
        propertyElement = get_object_or_404(Property, pk=property_id)
        if request.method == 'POST':
            print(request.POST)
            title = request.POST['title']
            name = request.POST['name']
            phone = request.POST['phone']
            email = request.POST['email']
            address = request.POST['address']

            inquiry = Query(
                property=propertyElement,
                title=title,
                name=name,
                phone=phone,
                email=email,
                address=address,
            )
            inquiry.save()
        return render(request, 'pages/MessageSent.html')
