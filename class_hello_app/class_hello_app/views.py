from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

class hello_world(APIView):
    def get(self,request):
        return Response("Hello World",status=status.HTTP_200_OK)
    def post(self,request):
        return Response(request.data,status=status.HTTP_200_OK)
