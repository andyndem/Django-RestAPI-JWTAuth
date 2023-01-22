from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.http import JsonResponse 
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from django.db.models import Q
from .models import Advocate, Company
from .serializers import AdvocateSerializer, CompanySerializer
from rest_framework import status

# Create your views here.
def home(request):
    data = Advocate.objects.all()
    return render(request, 'base/home.html', {'advocates': data})
# return HttpResponse("Welcome to Andy's Django world!!")

def advocate_details(request, username):
  data = Advocate.objects.get(username=username)
  return render(request, 'base/advocate-detail.html', {'advocate': data})

# def detail(request):
#   products=Product.objects.get(id=product.id)
#   context={'products':products}
#   return render(request,"foodapp/detail.html",context)



@api_view(['GET'])
def endpoints(request):
  data = ['/advocates', 'advocates/:username']
  return Response(data)
  #render (urls 'advocates.html') here


# def movies(request):
#     data = Movie.objects.all()
#     return render(request, 'movies/movies.html', {'movies': data})

# def home(request):
#     return HttpResponse("Home Page")

# def detail(request, id):
#     data = Movie.objects.get(pk=id)
#     return render(request, 'movies/detail.html', {'movie': data})




@api_view(['GET', 'POST'])
# @permission_classes([IsAuthenticated])
def advocate_list(request):
  
  # Handles GET request
  if request.method == 'GET':
    query = request.GET.get('query')
    if query == None:
      query = ''
    advocates = Advocate.objects.filter(Q(username__icontains=query) | Q(bio__icontains=query))
    serializer = AdvocateSerializer(advocates, many=True)
    return Response(serializer.data)
  
   # Handles POST request
  if request.method == 'POST':
    advocate = Advocate.objects.create(
      username = request.data['username'],
      bio = request.data['bio'],
    )
    serializer = AdvocateSerializer(advocate, many=False)
    return Response(serializer.data)


@api_view(['GET', 'PUT', 'DELETE'])
def advocate_detail(request, username):
  advocate = Advocate.objects.get(username=username)
  
  if request.method == 'GET':       
    serializer = AdvocateSerializer(advocate, many=False)
    return Response(serializer.data)
  
  if request.method == 'PUT':  
    advocate.username = request.data['username']
    advocate.bio = request.data['bio']      
    advocate.save() 
    serializer = AdvocateSerializer(advocate, many=False)
    return Response(serializer.data)

  if request.method == 'DELETE':   
    advocate.delete() 
    return Response('User was deleted')
  
@api_view(['GET'])
def companies_list(request):
  companies = Company.objects.all()   
  serializer = CompanySerializer(companies, many=True)
  return Response(serializer.data)

# Class Based Views implementation below

# class AdvocateList(APIView):
#     def get(self, request, format=None):
#         advocates = Advocate.objects.all()
#         serializer = AdvocateSerializer(advocates, many=True)
#         return Response(serializer.data)

#     def post(self, request, format=None):
#         serializer = AdvocateSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

 
# class AdvocateDetail(APIView): 
#   def get_object(self, username, format=None):
#         try:
#             return Advocate.objects.get(username=username)
#         except Advocate.DoesNotExist:
#             raise JsonResponse('Advocate Does Not Exist!!')
  
#   def get(self, request, username, format=None):
#     advocate = self.get_object(username)
#     serializer = AdvocateSerializer(advocate, many=False)
#     return Response(serializer.data)
  
#   def put(self, request, username, format=None):
#     advocate = self.get_object(username)
#     advocate.username = request.data['username']
#     advocate.bio = request.data['bio']     
#     serializer = AdvocateSerializer(advocate, many=False)
#     return Response(serializer.data)
    
#   def delete(self, request, username, format=None):
#     advocate = self.get_object(username)
#     advocate.delete() 
#     return Response('User was deleted')
      
      
      
