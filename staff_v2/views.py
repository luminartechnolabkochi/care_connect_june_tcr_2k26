from django.shortcuts import render
from django.contrib.auth.models import User
# Create your views here.
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import authentication,permissions

from staff.models import Doctor
from staff_v2.serializers import DoctorSerializer,UserSerializer

class DoctorListCreateView(APIView):

    authentication_classes =[authentication.BasicAuthentication]

    permission_classes=[permissions.IsAdminUser]


    def get(self,request):

        qs = Doctor.objects.all() #qs=> pynt => serialzer 

        serializer_instance = DoctorSerializer(qs,many=True)

        return Response(data=serializer_instance.data)

    def post(self,request):

        form_data = request.data # pynt=> qs => 

        serializer_instance = DoctorSerializer(data=form_data)

        if serializer_instance.is_valid():

            cleaned_data = serializer_instance.validated_data
            

            Doctor.objects.create(**cleaned_data)

            return Response(data=serializer_instance.validated_data)

        else:

            return Response(data=serializer_instance.errors)





class DoctorRetrieveUpdateDeleteView(APIView):

    authentication_classes =[authentication.BasicAuthentication]

    permission_classes=[permissions.IsAdminUser]


    def get(self,request,pk=None):

        qs = Doctor.objects.get(id=pk) #qs => PYNT 

        serializer_insatnce = DoctorSerializer(qs)

        return Response(data=serializer_insatnce.data)

    def put(self,request,pk=None):

        form_data  = request.data

        serializer_insatance = DoctorSerializer(data=form_data)

        if serializer_insatance.is_valid():

            cleaned_data = serializer_insatance.validated_data

            Doctor.objects.filter(id=pk).update(**cleaned_data)

            return Response(data=serializer_insatance.validated_data)

        else:

            return Response(data=serializer_insatance.errors)




class AdminCreateView(APIView):

    def post(self,request):

        form_data = request.data

        serializer_instance = UserSerializer(data=form_data)

        if serializer_instance.is_valid():

            cleaned_data = serializer_instance.validated_data

            # User.objects.create(**cleaned_data) X password encrypt

            # User.objects.create_user(**cleaned_data) X not an admin user

            User.objects.create_superuser(**cleaned_data)

            return Response(data=serializer_instance.validated_data)

        else:

            return Response(data=serializer_instance.errors)








#turf_booking
#app_turf[id,name,location,phone,fee]
# create
# list
# retrieve
# update
# delete
# Admin => 

