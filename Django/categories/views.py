from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Category
from .serializers import CategorySerializer


# Create your views here.
@api_view()
def categories(request):
    all_categories = Category.objects.all()
    serializer = CategorySerializer(
        all_categories,
        many=True,
    )
    return Response(
        {
            serializer.data,
        }
    )
