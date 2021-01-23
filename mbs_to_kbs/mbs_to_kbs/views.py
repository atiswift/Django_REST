from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

class func(APIView):
    def get(self,request):
        return Response("Enter data to Convert from Mbs to Kbs :")
    def post(self,request):
        obj = request.data
        if type(obj) == int:
            return Response(obj*1024)
        else:
            return Response("Please enter an integer : ",status=status.HTTP_400_BAD_REQUEST)
