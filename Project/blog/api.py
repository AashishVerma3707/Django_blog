from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import *
from .models import Article


class UserAuthentication(ObtainAuthToken):
    def post(self, request, *args, **kwargs):
        serializer=self.serializer_class(data=request.data, context={'request':request})
        serializer.is_valid(raise_exception=True)
        user=serializer.validated_data['user']
        token, created= Token.objects.get_or_create(user=user)
        return Response(token.key)


class ArticleBody(APIView):
    def get(self, request):
        model= Article.objects.all()
        serializer= UserSerializer(model ,many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer=UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ArticleBodyDetail(APIView):
    def get(self,request,employee_id):
        model=Article.objects.get(id=employee_id)
        serializer=UserSerializer(model)
        return Response(serializer.data, status=status.HTTP_202_ACCEPTED)



    def put(self,request,employee_id):
        model=Article.objects.get(id=employee_id)
        serializer=UserSerializer(model, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_202_ACCEPTED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
