from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view

from metrolar.models import  Metro 
from metrolar.api.serializers import MetroSerializers



#class views
from rest_framework.views import APIView
from rest_framework.generics import get_object_or_404



@api_view(['GET','POST'])
def metro_list_create_api_view(request): 
    
    if request.method =='GET':
        metrolar = Metro.objects.all() 
        serializer = MetroSerializers(metrolar,many=True  )
        return Response(serializer.data)
    
    elif request.method == 'POST':
        serializer = MetroSerializers(data=request.data, many=True ) 
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status= status.HTTP_201_CREATED)
        return Response(status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET','PUT','DELETE'])
def metro_detail_api_view(request, pk):
    try:
        metro_instance = Metro.objects.get(pk=pk)     
    except Metro.DoesNotExist: 
        return Response(
            {
                'errors':{
                    'code': 404,
                    'message': f'Böyle bir id ({pk}) ile ilgili makale bulunamadı'

                }

            },
            status=status.HTTP_404_NOT_FOUND

        )
    if request.method == 'GET':
        serializer = MetroSerializers(metro_instance) 

        
        return Response(serializer.data)
    elif request.method == 'PUT':
        serializer = MetroSerializers(metro_instance, data=request.data)
        if serializer.is_valid():
            serializer.save()
            
        return Response(status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        metro_instance.delete()  
        return Response(
            {
                'işlem':{
                    'code': 204,
                    'message': f'({pk}) idli metro bilgisi silinmiştir.'

                }

            },
            status = status.HTTP_204_NO_CONTENT
        )


