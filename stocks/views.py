from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .models import Client, Company, Company_assets ,IPO ,Demat#,Market

# Create your views here.
def home(request):
        return render(request, 'home.html')


def handleSignup(request):
    if request.method == 'POST':
        username = request.POST['username']
        pass1= request.POST['pass1']
        pass2 = request.POST['pass2']
       

        if len(username) > 10:
            messages.error(request, 'Username more than 10 characters')
            return redirect('home')


        if not username.isalnum():
            messages.error(request, 'Username should only contain letters and numbers')
            return redirect('home')

        if pass1 != pass2 :
            messages.error(request, 'passwords do not match')
            return redirect('home')


        myuser = User.objects.create_user(username,None,pass1)
        myuser.save()
        messages.success(request, 'You account successfully created')
        loginusername = username
        loginpassword = pass1
        
        user = authenticate( username = loginusername, password = loginpassword)

        if user is not None:
            login(request, user)
            messages.success(request, 'Succesfully Logged in')
            return redirect('handle_clientProfile')
        else:
            messages.error(request, 'Invalid Credentials')
            return redirect('home')      
    else:
        return HttpResponse('error 404 - not found')

def handleLogin(request):
    if request.method == 'POST':
        loginusername = request.POST['loginusername']
        loginpassword = request.POST['loginpassword']
        
        user = authenticate( username = loginusername, password = loginpassword)

        if user is not None:
            login(request, user)
            messages.success(request, 'Succesfully Logged in')
            return redirect('home')
        else:
            messages.error(request, 'Invalid Credentials')
            return redirect('home')
        
    else:
        return HttpResponse('error 404 - not found')




def handleLogout(request):
    logout(request)
    messages.success(request, 'Succesfully Logged out')
    return redirect('home')

def handleipoLogin(request):
    if request.method == 'POST':
        loginusername = request.POST['ipologinusername']
        loginpassword = request.POST['ipologinpassword']
        
        user = authenticate( username = loginusername, password = loginpassword)

        if user is not None:
            login(request, user)
            messages.success(request, 'Succesfully Logged in')
            return redirect('home')
        else:
            messages.error(request, 'Invalid Credentials')
            return redirect('home')
        
    else:
        return HttpResponse('error 404 - not found')


def handle_clientProfile(request):
    if request.method == 'POST':
        if request.user.is_authenticated : 
            username = request.user.get_username()
            fname = request.POST['fname']
            lname= request.POST['lname']
            contact = request.POST['contact']
            age = request.POST['age']
            balance = request.POST['balance']
            password = request.POST['password']
            user = authenticate( username = username, password = password)
            if user is not None:
                client = Client(username = username, fname = fname, lname = lname, contact=contact,age=age,balance=balance, password=password)
                client.save()

                

                messages.success(request, 'Succesfully profile completed')
                return redirect('home')
            else:
                messages.success(request, 'password incorrect')
                return redirect('clientprofile.html')
        else: 
            messages.error(request, 'pls sign in')
            return redirect('home')
    else :
        return render(request, 'clientprofile.html')

def handle_addbalance(request):
    if request.method == 'POST':
        if request.user.is_authenticated : 
            username = request.user.get_username()
            amount = request.POST['Amount']
            C = Client.objects.get(username=username)
            C.balance = C.balance + int(amount)
            C.save()
            messages.success(request, 'Succesfully balance added')
            return redirect('home')
        else: 
            messages.error(request, 'pls sign in')
            return redirect('home')


def handle_addIPO(request):
    if request.method == 'POST':
        if request.user.is_authenticated : 
            username = request.user.get_username()
            print(username)
            price = int(request.POST['price'])
            total_shares = int(request.POST['Quantity'])


            print(price,total_shares)
            C = Company.objects.get(username=username)
            try :
                pca = Company_assets.objects.get(company_id=C)

                if pca.price != 0:
                    if pca.price != price :
                        messages.error(request, 'Your entered price should be same as Previous IPO '+str(pca.price))
                        return redirect('home')

                ca = Company_assets(company_id=C,price=price,total_shares=total_shares+pca.total_shares,net_worth=price*(total_shares+pca.total_shares))
                ca.save()
            except :
                ca = Company_assets(company_id=C,price=price,total_shares=total_shares,net_worth=price*(total_shares))
                ca.save()

            cipo = IPO(company_id=C,price=price,remaining=total_shares)
            cipo.save()

            
            messages.success(request, 'Succesfully IPO listed on stock market !!')
            return redirect('home')
        else: 
            messages.error(request, 'pls sign in')
            return redirect('home')


            
    else:
        return render(request, 'clientprofile.html')

def handle_companyProfile(request):
    if request.method == 'POST':
        if request.user.is_authenticated : 
            username = request.user.get_username()
            company_name = request.POST['company_name']
            email= request.POST['email']
            website = request.POST['website']
            price = request.POST['price']
            total_shares = request.POST['total_shares']
            net_worth = request.POST['net_worth']
            password = request.POST['password']
            user = authenticate( username = username, password = password)
            if user is not None:
                company = Company(username = username,company_name = company_name , email = email, website = website, password=password)
                company.save()
                messages.success(request, 'Succesfully profile completed')
                return redirect('home')
            else:
                messages.success(request, 'password incorrect')
                return redirect('companyprofile.html')
        else: 
            messages.error(request, 'pls sign in')
            return redirect('companyprofile.html')
    else: 
        return render(request, 'companyprofile.html')

def handleipoSignup(request):
    if request.method == 'POST':
        username = request.POST['username']
        pass1= request.POST['pass1']
        pass2 = request.POST['pass2']
       

        if len(username) > 10:
            messages.error(request, 'Username more than 10 characters')
            return redirect('home')


        if not username.isalnum():
            messages.error(request, 'Username should only contain letters and numbers')
            return redirect('home')

        if pass1 != pass2 :
            messages.error(request, 'passwords do not match')
            return redirect('home')


        myuser = User.objects.create_user(username,None,pass1)
        myuser.save()
        messages.success(request, 'You account successfully created')
        loginusername = username
        loginpassword = pass1
        
        user = authenticate( username = loginusername, password = loginpassword)

        if user is not None:
            login(request, user)
            messages.success(request, 'Succesfully Logged in')
            return redirect('handle_companyProfile')
        else:
            messages.error(request, 'Invalid Credentials')
            return redirect('home')      
    else:
        return HttpResponse('error 404 - not found')


def handleProfile(request):
    if request.user.is_authenticated : 
        clients = Client.objects.all()
        companys = Company.objects.all()
        c = 0
        for client in clients:
            if client.username == request.user.get_username():
                user = authenticate( username = request.user.get_username(), password = client.password)
                if user is not None:
                    params = {'currentclient' : client }
                    c = 1
                    return render(request, 'clientprofileview.html', params)                    
                else:
                    pass
            else:
                pass
        if c == 0 : 
            for company in companys:                
                if company.username == request.user.get_username():
                    user = authenticate( username = request.user.get_username(), password = company.password)
                    if user is not None:
                        try: 
                            assests = Company_assets.objects.get(company_id=company)
                            params = {'currentcompany' : company ,'currentcompanyassest' :assests}
                            return render(request, 'companyprofileview.html', params)
                        except:
                            params = {'currentcompany' : company ,'currentcompanyassest' :{}}
                            return render(request, 'companyprofileview.html', params)
                    else:
                        pass
                else:
                    pass
        else:
            pass
    else: 
        messages.error(request, 'pls sign in')
        return redirect('home')

def handleLiveipo(request) :
    if request.user.is_authenticated : 
        ipos = IPO.objects.all()
        parameters = {'ipos':ipos}
        return render(request, 'liveipo.html', parameters)

def handlebuy(request):
    if request.user.is_authenticated : 
        ipo = request.POST['ipo']
        n = request.POST['share']
        print(ipo,n)
        company = Company.objects.get(company_name=ipo)
        ipo = IPO.objects.get(company_id=company)
        ipo.remaining = ipo.remaining - int(n)
        
        client = Client.objects.get(username=request.user.get_username())

        client.balance = client.balance - int(n)*ipo.price

        if ipo.remaining < int(n):
            messages.error(request, 'Please enter valid number of shares !!')
            return redirect('handleLiveipo')

        if client.balance >= 0:

            try :
                demat = Demat.objects.get(c_id=client,company_id=company)
                demat.quantity = demat.quantity + int(n)
            except :
                demat = Demat(c_id=client,company_id=company,quantity=int(n))
            ipo.save()
            demat.save()
            client.save()

            return redirect('handleLiveipo')
        else :
            messages.error(request, 'You Do not have enough balance to complete this transaction!!')
            return redirect('handleLiveipo')
    else: 
        messages.error(request, 'please sign in')
        return redirect('home')


def handleDemat(request):
    if request.user.is_authenticated : 
        demats = Demat.objects.all()
        parameters = {'demats':demats}
        return render(request, 'dematprofile.html', parameters)

