import chunk
import random
import sqlite3
import re

import aadhar
from django.contrib import messages
from django.http import request
from django.shortcuts import render,redirect
import testdb
import time
from urllib.parse import urlparse

class client:


    def authcheck(request):
        hitcount=0
        if request.method=="POST":
            hitcount+=1
            usern=request.POST.get("username")
            passd = request.POST.get("lpassword")
            var=testdb.database()
            savepass=var.searchuser(usern) #brings the password
            temp=''
            for i in savepass:
                print(i[0])
                temp+=i[0]

            if temp==passd:
                print("password matched success")
                if var.designation(usern)=="Freelancer":

                    return redirect("freelancerdashboard")
                else:
                    return redirect("jobabout")
            else:
                message="incorrect password"
                messages.error(request, message)
                return render(request, "auth.html")
        elif request.method=="POST" and "forgotpass" in request.POST:
            return render(request,"passreset.html")
        else:
            return render(request, "auth.html")
    def passreset(request):
        if request.method == "POST" and 'check' in request.POST:
            usern = request.POST.get("full-name")

            email = request.POST.get("email")

            var = testdb.database()

            if usern!="" and email!="":
                save=var.searchfrpass(usern)
                if save==False:
                    messages.error(request,"Incorrect username of email")
                    return render(request,"passreset.html")
                elif save!=False:
                    temp = ""
                    for i in save:
                        print(i[0])
                        if  i[0]==email:
                                return redirect("/passverification")
                        else:
                            messages.error(request, "Incorrect Email")
                            return render(request, "passreset.html")
                else:
                    return render(request, "passreset.html")



            else:
                messages.error(request, "Enter Details")
                return render(request, "passreset.html")
        else:
            return render(request, "passreset.html")
    def passverification(request):

        if request.method == "POST" and 'checkpass' in request.POST:
                passd = request.POST.get("passd")
                passv = request.POST.get("passdv")
                if passd != "" and passv != "":
                    if passd == passv:
                        messages.error(request, "password reset is succesfull", {"status": "success"})

                        return redirect("/")
                    else:
                        messages.error(request, "Enter Password correctly ", {"status": "danger"})
                        return render(request, "passreset.html")
                else:
                    return render(request, "passreset.html")

        else:
            return render(request,"passreset.html")


    def devfeedback(request):
        return render(request, "myfeedbacks.html")
    def claims(request,id):
        if request.method=="POST":
            pt=testdb.database()
            data = pt.searchbyid(id)
            li = []
            for i in data:
                 price=i[4]
                 mesg=i[3]
                 randdomn = random.randrange(20, 50, 3)
                 if pt.insertclaims("Ishan.07",price,mesg):
                     return redirect("freelancerdashboard")
                 else:
                    for i in data:
                        dct = {"title": i[1],
                               "message": i[3],
                               "price": i[4],
                               "id": i[0],
                               "cat": i[2],
                               "views": randdomn
                               }
                        li.append(dct)

                        return render(request, "claims.html", {"data": li})
        else:
            pt = testdb.database()
            data = pt.searchbyid(id)
            li = []
            randdomn=random.randrange(20, 50, 3)
            for i in data:
                dct = {"title": i[1],
                       "message": i[3],
                       "price": i[4],
                       "id": i[0],
                       "cat":i[2],
                       "views":randdomn
                       }
                li.append(dct)

                return render(request, "claims.html", {"data": li})





    def registercheck(request):
        if request.method == "POST":
            first_name=request.POST.get('fname')
            Last_name = request.POST.get('lname')
            Username = request.POST.get('uname')
            email = request.POST.get('email')
            passd = request.POST.get('password')
            passdr= request.POST.get('rpassword')
            state= request.POST.get('stt')
            city= request.POST.get('cname')
            phonenumber = request.POST.get('pnumber')
            pincode=request.POST.get('pcode')
            Adhar_number=request.POST.get('anumber')

            designa=request.POST.get('designation')

            params={'fname':first_name,'lname':Last_name,'uname':Username,'email':email,'passd1':passd,'passd2':passdr,'state':state,'city':city,'pincode':pincode,'anumber':Adhar_number,
                    'designation':designa}
            if passd != passdr:
                message='password not matched'
                messages.error(request,message)

                return render(request,'register.html',params)
            else:
                regex = "^[1-9]{1}[0-9]{2}\\s{0,1}[0-9]{3}$"
                p = re.compile(regex)
                if (pincode == ''):
                    message="pincode is blank"
                    messages.error(request, message)

                    return render(request,'register.html',params)
                else:
                    m = re.match(p, pincode)

                    if m is None:
                        message="Invalid Pincode"
                        messages.error(request, message)

                        return render(request,'register.html',params)
                    else:
                        ref=aadhar.validate(Adhar_number)
                        if ref=='Invalid Aadhar Number':
                            messages.error(request,ref)
                            return render(request, 'register.html', params)
                        else:
                            var=testdb.database()
                            valuesr=var.Adddata(LastName=Last_name, FirstName=first_name, UserName=Username, Email=email,
                      Phonenumber=phonenumber, Aadharn=Adhar_number, Password=passd, Pcode=pincode,
                      designation=designa,
                      City=city, State=state)
                            if valuesr==True:
                                messages.success(request,"Data Uploaded")
                                print("Data Uploaded")
                            else:
                                print("Can't upload data")
                            return redirect("/")
        else:
            return render(request, "register.html")






    def cldash(request):
        pt=testdb.database()
        data=pt.showdatacdash()
        li=[]
        for i in data:
            dct={"title":i[1],
                 "message":i[3],
                 "id":i[0]
                 }
            # tple=(i[1],i[3])
            li.append(dct)
        return render(request, "clientdash.html",{"data":li})

    def pricing(request):
        return render(request, "pricing.html")

    def feedback(request):
        if request.method=="POST":
            name=request.POST.get("name")
            emails = request.POST.get("email")
            message = request.POST.get("message")
            t=testdb.database()
            status=t.feedbackadd(name=name,emails=emails,mesg=message)
            if status:

               return redirect("/")
            else:
                return render(request, "feedback.html")

        else:

            return render(request, "feedback.html")
    def aboutus(request):
        return render(request, "about.html")
    def jobstatus(request,id):
        if request.method == "POST":
            messages.error(request,"Assigned")
            pt = testdb.database()
            t = pt.showclaims()
            li = []
            if t is not False:
                for i in t:
                    name = i[0]
                    price = i[1]
                    dict = {
                        "name": name,
                        "price": price,
                        "id": id
                    }
                    li.append(dict)
            return render(request,"projstatus.html",{"data":li})
        else:
            pt=testdb.database()
            t=pt.showclaims()
            li = []
            if t is not False:
                for i in t:
                    name=i[0]
                    price=i[1]
                    dict={
                        "name":name,
                        "price":price,
                        "id":id
                    }
                    li.append(dict)
            return render(request, "projstatus.html",{"data":li})





    def topclients(request):
        return render(request, "topclients.html")

    def removejob(request,id):
        pt = testdb.database()

        if pt.delbyid(id):
            data = pt.showdatacdash()
            li = []
            for i in data:
                dct = {"title": i[1],
                       "message": i[3],
                       "id": i[0]
                       }
                # tple=(i[1],i[3])
                li.append(dct)
            # print(li)
            messages.error(request, " deleted data")
            return render(request, "clientdash.html", {"data": li,"status":"success"})
        else:
            data = pt.showdatacdash()
            li = []
            for i in data:
                dct = {"title": i[1],
                       "message": i[3],
                       "id": i[0]
                       }
                # tple=(i[1],i[3])
                li.append(dct)
            # print(li)
            messages.error(request,"cannot delete data")
            return render(request, "clientdash.html", {"data": li,"status":"danger"})




    def addjob(request):
        return render(request,"addproject.html")
    def jobdatadd(request):
        global myfile
        Jobname=request.POST.get('taskname')
        JobTitle=request.POST.get('Category')
        jobmsg=request.POST.get('message')
        jobprice=request.POST.get('price')

        words = jobmsg.split()
        # Extract URLs from the words using urlparse()
        urls = []
        for word in words:
            parsed = urlparse(word)
            if parsed.scheme and parsed.netloc:
                urls.append(word)
        if len(urls)!=0:
            messages.error(request, "No Url Accepted")


            return render(request, "addproject.html",{"jobname":Jobname,"jobmessage":jobmsg,"status":"danger","price":jobprice})
        else:
            messages.error(request, "No Url detected")
            time.sleep(2)
            pt=testdb.database()

            if pt.Adddatajob(jobname=Jobname,Title=JobTitle,message=jobmsg,price=jobprice):
                print("data job added")
                messages.error(request, "Data Added to Job")

            return render(request, "addproject.html", {"jobname": Jobname, "jobmessage": jobmsg,"status":"success","price":jobprice})


    def developerdash(request):
        pt = testdb.database()
        data = pt.showdatacdash()
        li = []
        for i in data:
            dct = {"title": i[1],
                   "message": i[2],
                   "price":i[4],
                   "id": i[0]
                   }
            li.append(dct)


        return render(request,"devdash.html",{"data":li})








