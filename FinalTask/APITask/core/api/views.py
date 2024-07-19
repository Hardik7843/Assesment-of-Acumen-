# from django.shortcuts import render
# import numpy as np
# import sqlalchemy
# from sqlalchemy import create_engine
# import sqlite3
# from .models import Person
from rest_framework.views import APIView
from rest_framework import status
import pandas as pd
from rest_framework.response import Response 
from rest_framework.decorators import api_view , renderer_classes
from rest_framework.renderers import JSONRenderer, TemplateHTMLRenderer
from user.models import person , company
from .serializer import PersonSerializer
import os
import re

csv_file_path = os.path.join(os.path.dirname(__file__), 'Sample.csv')


@api_view(['GET'])
def show(request):
    data = person.objects.all()
    serialized = PersonSerializer(data , many = True)
    return Response(serialized.data)

@api_view(['POST'])
def add(request):
    serialized = PersonSerializer(data = request.data )
    if serialized.is_valid():
        print(request.data)
        serialized.save()
    return Response(serialized.data)



api_view(['POST'])
def add_companies(request):
    df = pd.read_csv(csv_file_path)
    for index, row in df.iterrows():
        if ( company.objects.filter(name = row['current_company']).exists() == False):
            c = company(
                    name = row['current_company']
            )
            c.save()
            
    return Response("Company Added Successfully!")



@api_view(['POST'])
def add_csv(request):
    df = pd.read_csv(csv_file_path)
    for index, row in df.iterrows():
        email = ""
        # if re.match('^[a-zA-Z]+[0-9]*@[a-zA-Z]+.[a-zA-Z]+$', f"{row['email']}") != None:
        if re.match('^[a-zA-Z]+[0-9]*@[a-zA-Z]*(mail).(com)+$', f"{row['email']}") == None:
            email = "Invalid"
        elif row['email'] == None:
            email = "empty"
        else:
            email = row['email']
        # company_name = company.objects.get(filter = row['current_company'])
        p = person(
                uniqe_id = row['id'],
                email = email,
                url = row['profile_url'],
                # company = company_name
                )
        p.save()
    return Response("Employee Added Successfully")
