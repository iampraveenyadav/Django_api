from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.parsers import JSONParser 
from rest_framework import status
import json
from django.http import HttpResponse
from .models import UserServicesChtghFinal
from .serializers import UserServicesChtghFinalSerializer
from rest_framework.decorators import api_view
import pandas as pd
from .easygov_operations import *
@api_view(['GET', 'POST', 'DELETE'])
def dbase_name(request):
    if request.method == 'GET':
        cities = UserServicesChtghFinal.objects.all()
        
        title = request.GET.get('name_of_districts', None)
        if title is not None:
            cities = cities.filter(title__icontains=title)
        df = pd.DataFrame.from_records(cities.values())
        #df = cities.values()
        df = Revenue_Report_Service_Wise(df)

        #print(df.head())
        #df=df.head()
        #df=df.to_dict()
        #df=json.dumps(df, indent = 4) 
        #cities_serializer = ApplicationSummaryDistrictsWiseSerializer(cities, many=True)
        
        #print(df)
        #for i in df.to_json(orient = 'records').split(" "):
                            #print(i)
        #return JsonResponse(df.to_json(orient = 'records'), safe=False)
        #return HttpResponse(df.to_json(orient = 'records'), content_type="application/json")
        #return HttpResponse(df.to_json(orient = 'records'))
        return Response(df,template_name=None)

        #json_records = df.reset_index().to_json(orient ='records')
        #data = []
        #data = json.loads(json_records)
        #context = {'d': data}
        #return render(request, 'index.html', context)
        #context = {'d': df.to_json(orient = 'records')}
        #return render(request, 'index.html', context)
 
 
