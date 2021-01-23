from django.shortcuts import redirect
from rest_framework.views import APIView

class google(APIView):
    def get(self,request):
        return redirect("https://www.google.com")
