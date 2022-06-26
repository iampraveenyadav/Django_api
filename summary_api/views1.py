from django.shortcuts import render
from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser 
from rest_framework import status
import json
from django.http import HttpResponse
from .models import city
from .serializers import dbaseSerializer
from rest_framework.decorators import api_view
import pandas as pd
@api_view(['GET', 'POST', 'DELETE'])
def dbase_name(request):
    if request.method == 'GET':
        cities = city.objects.all()
        
        title = request.GET.get('name', None)
        if title is not None:
            cities = cities.filter(title__icontains=title)
        df = pd.DataFrame.from_records(cities.values())
        print(df.head())
        df=df.head()
        #df=df.to_dict()
        #df=json.dumps(df, indent = 4) 
        cities_serializer = dbaseSerializer(cities, many=True)
        
        #print(df)
        for i in df.to_json(orient = 'records').split(" "):
                            print(i)
        #return JsonResponse(df.to_json(orient = 'records'), safe=False)
        #return HttpResponse(df.to_json(orient = 'records'), content_type="application/json")
        return HttpResponse(df.to_json(orient = 'records'))
 
 
