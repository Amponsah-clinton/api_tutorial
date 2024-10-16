from rest_framework.response import Response
from rest_framework.decorators import api_view
from item.models import items
from .serializers import itemserializers

@api_view(["GET"])
def getData(request):
    item = items.objects.all()
    serializer = itemserializers(item, many= True) 
    return Response(serializer.data)


#create an endpoint
@api_view(["POST"]) 
def addItem(request):
    serializer = itemserializers(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response()