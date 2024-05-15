from django.http import HttpResponse,JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render
import pyodbc

from storedprocedure import settings

# Create your views here.
def home(request):
    return render (request,'index.html')

@csrf_exempt
def accept(request):
    conn_str = (
            "DRIVER={SQL Server Native Client 11.0};SERVER="
            + settings.DATABASES['default']['HOST'] +
            ";DATABASE=" + settings.DATABASES['default']['NAME'] +
            ";UID=" + settings.DATABASES['default']['USER'] +
            ";PWD=" + settings.DATABASES['default']['PASSWORD'] + ";"
        )
    conn = pyodbc.connect(conn_str)
    cursor = conn.cursor()
    cursor.execute('EXEC rithin_test')
    rows = cursor.fetchall()
    conn.close()
    print(rows)
    data = {'k':'rows'}
    return JsonResponse(data)
    