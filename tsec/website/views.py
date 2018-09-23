from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .models import Document
from .forms import UploadFileForm

import random
from django.core.mail import send_mail
from .database import data, certif, schreq

schemes = data


@login_required
def index(request):
    context = {}
    context['schemes'] = schemes
    context_new = {}
    for i in range(len(schreq)):
        if isEligible(i+994, request.user):
            print('eligible', i+994)
            context_new[i+994] = 'Eligible'
    #print(context)
            context['schemes'][i+994]['eligible']="Eligible"
    return render(request, 'Catalogue/catalogue.html' , context)

def loginuser(request):
    if request.method == 'POST':
        username = request.POST.get('email','')
        password = request.POST.get('password','')
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                request.session.set_expiry(86400) #sets the exp. value of the session 
                login(request, user) #the user is now logged in
                # print('hi')
                return redirect('index')
        else:
            print('error')
           
            return render(request, 'website/login.html', {'loginerror': 'Login error!'})
                
    return render(request, 'website/login.html' )

def logoutuser(request):
    logout(request)
    return redirect('login')


def signup(request):
    if request.method == 'POST':
        first_name = request.POST.get('fname')
        last_name = request.POST.get('lname')
        password = request.POST.get('password')
        email = request.POST.get('email')

        if len(User.objects.filter(email__exact = email)) != 0:
            return render(request, 'website/signup.html', {'error_message':'A user with the same email id already exists.'})

        # new_user.save()
        request.session.set_expiry(900) #sets the exp. value of the session
        request.session['user'] = {
            'fname': first_name,
            'last_name': last_name,
            'email': email,
            'email': email,
            'password': password

        }
        
        # print('hi')
        rn = random.randint(1000, 9999)
        request.session['verifynum']= rn
        message = """From:  Schemio karan.sheth@somaiya.edu
            
            Subject: Confirm Your Email

            Enter the pin on the website.\n The pin is """+str(rn)+". "
        send_mail('Confirm email', message, 'karan.sheth@somaiya.edu', [email])
        return redirect('verify_email')

    return render(request, 'website/signup.html')

def verify_email(request):
    verifynum = request.session.get('verifynum')
    if verifynum==None:
        return redirect('signup')
    if request.method == 'POST':
        if request.POST.get('verifynum') == str(verifynum):
            email = request.session['user']['email']
            first_name = request.session['user']['fname']
            last_name = request.session['user']['last_name']
            username = email
            password = request.session['user']['password']
            new_user = User.objects.create_user(username, email, password)
            new_user.first_name = first_name
            new_user.last_name = last_name
            new_user.is_active = True
            new_user.save()
            login(request, new_user) #the user is now logged in
            request.session.set_expiry(86400)
            return redirect('index')
        else:
            return render(request, 'website/econf.html', {'invalid': True})
    else:
        return render(request, 'website/econf.html')

    return render(request, 'website/signup.html')

no = 0

def catalogue(request):
    '''e_schemes = []
    for dept in data:
        for sch in data[dept]:
            if isEligible(sch, request.user):
                e_schemes.append(sch)
                print(sch)
        for e in e_schemes:
            print(e)
    return render(request, 'Catalogue/catalogue.html' , {"e_schemes":e_schemes})'''
    return render(request, 'Catalogue/catalogue.html' , {"schemes":schemes})
@login_required
def editprofile(request):
    '''li =['Residence Proof of Husband', 'Electricity Bill', 'Marriage certificate',
     'Property Tax Receipt', 'Identity card issued by Govt or Semi Govt organisations', 'Water Bill',
      'Telephone Bill', 'PAN Card', 'RSBY Card', 'MNREGA Job Card', 'Rent Receipt', 'Aadhaar Card', 'Signature of Applicant',
       'Passport', 'Property Registration Fee', 'Extracts of 7/12 and 8 A/ Rent Receipt', 'Voter List Fee', 'Driving License',
        'Voter ID Card', 'Ration Card', 'Photo of Applicant']'''

    if request.method=='POST':
        allchecked = request.POST.getlist('checks')
        print(allchecked)
        for chk in allchecked:
            if len(request.user.document_set.filter(name__exact = certif[int(chk)]))==0:

                d = Document(name = certif[int(chk)], user = request.user)
                d.save()
                print(d)
        return redirect('editprofile')
    ud = request.user.document_set.all()
    uds = []
    for udoc in ud:
        uds.append(udoc.name)
    print(uds)
    chkd = [False]*len(certif)
    addd =[]
    for i in range(len(certif)):
        if certif[i] in uds:
            addd.append(certif[i])
            chkd[i]=True
    print(chkd)
    return render(request, 'Catalogue/myprofile.html', {'editprofile': True, 'firstname':request.user.first_name ,'lastname':request.user.last_name, 'email':request.user.email , 'li':certif, 'chkd':chkd, 'documents': addd})
   
def isEligible(schid, user):
    '''scheme = Scheme.objects.filter(name__exact = name)
    userdocs = user.doument_set.all()
    scheme docs = scheme.documents.all()'''
    userdocs = user.document_set.all()
    userdocl = []
    for e in userdocs:
        userdocl.append(e.name)
    
    schemereq = schreq[schid - 994]
    # print(schemereq, userdocl)
    # print()
    for r in schemereq:
        if r not in userdocl:
            return False

    return True