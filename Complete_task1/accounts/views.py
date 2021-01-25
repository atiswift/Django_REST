from rest_framework import generics,permissions
from knox.models import AuthToken
from .serializers import UserSerializer,RegistrationSerializer
from rest_framework.response import Response
from .models import User
from django.core.mail import send_mail
from rest_framework.parsers import MultiPartParser,FormParser,FileUploadParser


class Register(generics.GenericAPIView):
    serializer_class = RegistrationSerializer
    parser_classes = (MultiPartParser,FormParser,FileUploadParser)
    def post(self,request,*args,**kwargs):
        serializer = RegistrationSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        #user = serializer.save() #serializer.save method will invoke create method in UserSerializer
        #data = {'email_body': email_body,'to_email':user.email, 'email_subject' : }
        user = User.objects.create_user(
                    username = request.data.get('username',None),
                    email = request.data.get('email',None),
                    password = request.data.get('password',None),
                    file = request.data.get('file',None),
                    date_of_birth = request.data.get('date_of_birth',None),
                    )
        send_mail(
                    'Account Activation',  #subject
                    'Hi '+str(user.username)+', your account has been created.', #message
                    'aditusingh58@gmail.com', #from email
                    (user.email,), #to
                    fail_silently=False)


        return Response({
                            "user":UserSerializer(user,context=self.get_serializer_context()).data,
                            "token":AuthToken.objects.create(user)[1]
                        })


from rest_framework.authtoken.serializers import AuthTokenSerializer
from knox.views import LoginView as KnoxLoginView
from django.contrib.auth import login

class LoginAPI(KnoxLoginView):
    permission_classes = (permissions.AllowAny,)

    def post(self,request,format=None):
        serializer = AuthTokenSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        login(request,user)
        return super(LoginAPI,self).post(request,format=None)




'''
def send_email(data):
    email = EmailMessage(subject=data['email_subject'],body=data['email_body'],to=[data['to_email']])
    email.send()
'''
