from django.http import HttpResponse,HttpResponseRedirect,JsonResponse
from  django.core.files.storage import FileSystemStorage
from django.shortcuts import redirect,render,get_object_or_404
from django.http import JsonResponse
from urllib.parse import urlencode
from django.utils import timezone
from django.urls import reverse
from django.db.models import Q
from .models import *
import datetime
import os,openai
import pandas as pd
import tensorflow as tf
from keras import backend as K 
from ML.test_disease import predict
from ML import test_crp,test_ftlzr
import requests
import chatbot
import requests


#api calling
def fetch_weather_and_forecast(city, api_key, current_weather_url):
    try:
        response = requests.get(current_weather_url.format(city, api_key)).json()
        response = requests.get(current_weather_url.format(city, api_key)).json()
        print("Response:", response)

        if response['cod'] == '404' and response['message'] == 'city not found':
            error_message = f"City '{city}' not found in the API."
            return None, None  # Return None for both temp and hum

        # Assuming the 'main' and 'weather' keys are present in the response
        temp = round(response['main']['temp'] - 273.15, 2)
        print(temp)
        hum = round(response['main']['humidity'], 2)
        print(hum)
        desc = response['weather'][0]['description']
        print(desc)
        try:
            precip = response['rain']['1h']
            print(precip)
        except:
            precip=0
            print("rainfall value not available")
        print("rainfall:",precip)
        icon = response['weather'][0]['icon']

        return temp, hum,precip

    except requests.exceptions.RequestException as e:
        print("Error:", e)
        error_message = "Error occurred while fetching weather data."
        return None, None  # Return None for both temp and hum
    except KeyError as e:
        error_message = f"Invalid response: Missing key '{e.args[0]}' in the API response."
        return None, None  # Return None for both temp and hum


# basic operation for user and admin
def index(request):
    res1=product.objects.filter(product_type='fertilizer')
    res2=product.objects.filter(product_type='pesticide')
    return render(request,'index.html',{'result1':res1,'result2':res2})

def registration(request):
    return render(request,'registration.html')

def register(request):
    if request.method=='POST':
        a=request.POST.get('name')
        b=request.POST.get('email')
        c=request.POST.get('phone')
        d=request.POST.get('password')
        e=request.POST.get('address')
        ins=reg_user(name=a,email=b,phone=c,password=d,address=e)
        ins.save()
    return render(request,'index.html',{'message1':'Successfully Registered'})

def login(request):
    return render(request,'login.html')

def check_login(request):
    email=request.POST.get('email')
    password=request.POST.get('password')
    if email=='admin@gmail.com' and password=='admin123':
        request.session['admin']='admin'
        return redirect(index)
    elif reg_user.objects.filter(email=email,password=password).exists():
        user=reg_user.objects.get(email=email,password=password)
        if user.password==request.POST['password']:
            request.session['uid']=user.id
            return redirect('index')       
    else:
        return render(request, 'login.html',{'msg':'Invalid email id or Password'})
    

def logout(request):
    session_keys=list(request.session.keys()) 
    for key in session_keys:
        del request.session[key]
    return redirect(index)

def edit_profile(request):
    if request.method=='POST':
        a=request.POST.get('name')
        b=request.POST.get('email')
        c=request.POST.get('phone')
        d=request.POST.get('password')
        e=request.POST.get('address')
        ins=reg_user(name=a,email=b,phone=c,password=d,address=e,id=request.session['uid'])
        ins.save()
    ins=reg_user.objects.get(id=request.session['uid'])
    print("address:",ins.address)
    return render(request,'edit_profile.html',{'res':ins})

#user operations
def get_bot_response(request):
    user_response=request.GET.get('message')
    print("message:",user_response)
    bot_response=chatbot.talk(user_response,"chatbot_model")[0]
    return JsonResponse({'response': str(bot_response)})

def crop_prediction(request):
    return render(request,'crop_prediction.html')

def predict_crop(request):
    if request.method == 'POST':
        u_id = request.session.get('uid')
        a = request.POST.get('N')
        b = request.POST.get('P')
        c = request.POST.get('K')
        #d = request.POST.get('rainfall')
        #e = request.POST.get('temperature')
        f = request.POST.get('ph')

        # Fetching live weather
        api_key = '542e980ac8d3eb60b88374824f982bb2'
        current_weather_url = 'https://api.openweathermap.org/data/2.5/weather?q={}&appid={}'
        temp,hum, precip = fetch_weather_and_forecast(e, api_key, current_weather_url)

        if temp is None or hum is None:
            return render(request,'error_place.html')
        else:
            temperature = temp
            print(temp)
            humidity = hum
            print(humidity)

        df = pd.DataFrame({'N': [a], 'P': [b], 'K': [c], 'rainfall': [precip], 'temperature': [temperature],
                           'humidity': [humidity], 'ph': [f]})

        result1 = test_crp.test_crop(df)  # Make sure test_crp.test_crop() is defined and returns a valid result

        cus = crop_table(u_id=u_id, N=a, P=b, K=c, temperature=temperature,
                         humidity=humidity, ph=f, rainfall=precip, result=result1)
        cus.save()
        result2 = crop_table.objects.latest('id').id

        return render(request, 'crop_prediction.html', {'res1': result1, 'res2': result2})

def print_crop(request,id):
    res=crop_table.objects.get(id=id)
    return render (request,'print_crop.html',{'result':res})


def ftlzr_sugstn(request,id):
    res=crop_table.objects.get(id=id)
    return render (request,'ftlzr_sugstn.html',{'res2':res})

def ftlzr_prediction(request):
    return render(request,'ftlzr_prediction.html')

def predict_ftlzr(request):
    if request.method=='POST':
        u_id = request.session['uid']
        a=request.POST.get('N')
        b=request.POST.get('K')
        c=request.POST.get('P')
        d=request.POST.get('crop_type')
        df=pd.DataFrame({'N':[a],'K':[b],'P':[c],'Crop Type':[d]})
        print(df)
        result2=test_ftlzr.test_fertilizer(df)
        print(result2)
        cus=ftlzr_table(u_id=u_id, N=a,  K=b, P=c,crop_type=d,  result=result2)
        cus.save()
        result3=ftlzr_table.objects.latest('id').id
    return render(request,'ftlzr_prediction.html',{'res2':result2,'res3':result3})

def print_ftlzr(request,id):
    res=ftlzr_table.objects.get(id=id)
    return render (request,'print_ftlzr.html',{'result':res})

def disease_pred(request):
    return render(request,'plant_disease.html')

def addfile(request):
    if request.method=="POST":
        u_id = request.session['uid']
        file = request.FILES['file']
        try:
            os.remove("media/input/test/test.jpg")
            print("file removed")
        except:
            print("file not removed")
            pass
        fs = FileSystemStorage(location="media/input/test")
        fs.save("test.jpg",file)
        K.clear_session()
        label1,remedies1,pesticides1=predict()
        cus=plant_disease(u_id=u_id,file=file,label=label1,remedies=remedies1,pesticides=pesticides1)
        cus.save()
        selection = plant_disease.objects.latest('id')
    return render(request,'print_disease.html',{'result':selection})

def view_your_fertilizer(request,name):
    shop=product.objects.filter(product_name = name)
    return render(request,'view_your_fertilizer.html',{'result':shop})

def view_ftlzr(request):
    res1=product.objects.filter(product_type='fertilizer')
    res2=product.objects.filter(product_type='pesticide')
    return render(request,'view_ftlzr.html',{'result1': res1,'result2': res2})

def search_products(request):
    if request.method == "POST":
        product_name = request.POST.get('product_name')
        result = product.objects.filter(
            Q(product_type='fertilizer') | Q(product_type='pesticide'),
            product_name__icontains=product_name)
        return render(request, 'search_product.html', {'result': result})
    return redirect(view_ftlzr)

def buy_product(request,id):
    shop=product.objects.get(id=id)
    user=reg_user.objects.get(id=request.session['uid'])
    return render(request,'buy_ftlzr.html',{'result':shop,'result1':user})

def addpurchase(request):
    if request.method=='POST':
        uid= request.session['uid'] 
        #name =request.POST.get('name')
        pr_id=request.POST.get('pr_id')
        quantity=request.POST.get('quantity')
        rate=request.POST.get('rate')
        cardtype=request.POST.get('cardtype')
        cardname=request.POST.get('cardname')
        cardnumber=request.POST.get('cardnumber')
        cvv=request.POST.get('cvv')
        #phone=request.POST.get('phone')
        prod = product.objects.get(id=pr_id)
        product_quantity = int(prod.quantity)
        quantity = int(quantity)

        if product_quantity >= quantity:
            prod.quantity = str(product_quantity - quantity)
            prod.save()
        else:
            return HttpResponse("Insufficient quantity in stock.")
        ins=purchase(uid=uid,pr_id=pr_id,quantity=quantity,rate=rate,
                     cardtype=cardtype,cardname=cardname,cardnumber=cardnumber,
                     cvv=cvv,status='booked')
        ins.save()
        last_added_id = ins.id 
        inv = get_object_or_404(purchase, id=last_added_id)
    return render(request,'invoice.html',{'msg_buy':'You Transaction is successful', 'result': inv,'prod':prod})



def user_purchase_history(request):
    uid = request.session.get('uid')
    if uid is not None:
        # Filter purchases based on 'uid' and order them by 'transaction_date' in descending order
        pur = purchase.objects.filter(uid=uid).order_by('-date')

        # Render the template with the 'result' queryset
        return render(request, 'user_purchase_history.html', {'result': pur})

    # Handle the case when 'uid' is not present in the session (user is not logged in)
    # For example, you can return an HTTP response with an error message.
    return HttpResponse('User not logged in', status=401)



def view_your_pesticide(request,name):
    shop=product.objects.filter(product_name = name)
    return render(request,'view_your_pesticide.html',{'result':shop})






#admin
def view_users(request): 
    users = reg_user.objects.all()
    return render(request, 'view_users.html', {'user': users})

def product1(request):
    return render(request, 'add_product.html')


def view_product(request):
    res1=product.objects.filter(product_type='fertilizer')
    res2=product.objects.filter(product_type='pesticide')
    return render (request,'view_product.html',{'result1':res1,'result2':res2})

def add_product(request):
    if request.method=='POST':
        product_type=request.POST.get('product_type')
        product_name=request.POST.get('product_name')
        crop_type=request.POST.get('crop_type')
        price=request.POST.get('price')
        quantity=request.POST.get('quantity')
        myfile1=request.FILES['image']
        fs1= FileSystemStorage()
        filename1=fs1.save(myfile1.name,myfile1)
        ins=product(product_type=product_type,product_name=product_name,crop_type=crop_type,price=price,quantity=quantity,image=filename1)
        ins.save()
    return redirect(view_product)


def update_product_details(request,id):
    prod=product.objects.get(id=id)
    return render (request,'update_product_details.html',{'result': prod})

def update_product(request,id):
    if request.method=='POST':   
        product_name=request.POST.get('product_name')
        crop_type=request.POST.get('crop_type')
        price=request.POST.get('price')
        quantity=request.POST.get('quantity')
        myfile1=request.FILES['image']
        fs1= FileSystemStorage()
        filename1=fs1.save(myfile1.name,myfile1)
        ins=product(product_name=product_name,crop_type=crop_type,price=price,quantity=quantity,image=filename1,id=id)
        ins.save()
    return redirect(view_product)

def delete_product_details(request,id):
    prod=product.objects.get(id=id)
    prod.delete()
    return redirect(view_product)


def purchase_history(request):
    purchases = purchase.objects.all().order_by('-date')
    return render(request, 'view_purchase.html', {'result': purchases})


def update_status(request, id):
    try:
        sel = get_object_or_404(purchase, id=id)
        if sel.status == 'booked':
            sel.status = 'shipped'
        else:
            sel.status = 'delivered'
        sel.save()
        return redirect('purchase_history')  # Redirect without the app namespace
    except purchase.DoesNotExist:
        return HttpResponse('Purchase not found.', status=404)
    except Exception as e:
        return HttpResponse(f'An error occurred: {str(e)}', status=500)





def report_user(request):
    users = reg_user.objects.all()
    return render(request, 'report_user.html', {'user': users})

def report_crop(request):
    users = crop_table.objects.all()
    return render(request, 'report_crop.html', {'user': users})

def report_fertilizer(request):
    users = ftlzr_table.objects.all()
    return render(request, 'report_fertilizer.html', {'user': users})

def report_product(request):
    users = product.objects.all()
    return render(request, 'report_product.html', {'user': users})

def report_transaction(request):
    users = purchase.objects.all()
    return render(request, 'report_transaction.html', {'user': users})

def date_range(request):
    if request.method == 'POST':
        start_date_str = request.POST.get('start_date')
        end_date_str = request.POST.get('end_date')
    transactions = purchase.objects.filter(date__range=[start_date_str, end_date_str])
    return render(request, 'date_range_report.html', {'transactions': transactions})

