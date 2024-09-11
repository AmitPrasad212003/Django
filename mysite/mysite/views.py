from django.http import HttpResponse,HttpResponseRedirect
from django.shortcuts import render,redirect
from .forms import userForm
from service.models import Service
from news.models import News
from django.core.paginator import Paginator
from django.core.mail import send_mail,EmailMultiAlternatives




def spotify(request):
    return render(request,"index.html")

def marksheet(request):
    if request.method == "POST":
        s1 = eval(request.POST.get('subject1'))
        s2 = eval(request.POST.get('subject2'))
        s3 = eval(request.POST.get('subject3'))
        s4 = eval(request.POST.get('subject4'))
        s5 = eval(request.POST.get('subject5'))

        t = s1+s2+s3+s4+s5
        p = t*100/500
        
        if p>= 80:
            d = "First Division"
        elif p>=60:
            d = "Second Division"
        elif p>= 35:
            d = "Third Division"
        else:
            d = "Fail"
        data = {
            'total' : t,
            'per' : p,
            'div' : d,
        }
        return render(request,"marksheet.html",data)
    return render(request,"marksheet.html")

def calculator(request):
    c =''
    try:
        if request.method == "POST":
            n1 = eval(request.POST.get('num1'))
            n2 = eval(request.POST.get('num2'))
            opr = request.POST.get('opr')
            if opr == "+":
                c = n1 + n2;
            elif opr == "-":
                c = n1 - n2;
            elif opr == "*":
                c = n1 * n2;
            elif opr == "/":
                c = n1 / n2;


    except:
        c = "Invalid opr..."
    print(c)
    return render(request,"calculator.html",{'c':c})
def evenodd(request):
    c = ''
    
    if request.method == "POST":
        if request.POST.get('num1') == "":
            return render(request,"evenodd.html",{'error': True})
        n = eval(request.POST.get('num1'))
        if n%2 == 0:
            c = "Even Number"
        else:
            c = "Odd Number"
    return render(request,"evenodd.html",{'c':c})
def homepage(request):

    # subject = 'testing mail'
    # form_email = 'redrosebap@gmail.com'
    # msg = '<b> Welcome to Mysite </b>'
    # to = 'amit9733481931@gmail.com'

    # main = EmailMultiAlternatives(subject,form_email,msg,[to])
    # main.content_subtype = 'html'
    # main.send()








    
    # send_mail(
    #     'TEsting Mail',
    #     'test test mail check up ',
    #     'redrosebap@gmail.com',
    #     ['amit9733481931@gmail.com'],
    #     fail_silently = False,
    # )










    newsData = News.objects.all();
    serviceData = Service.objects.all()
    if request.method == "GET":
        st = request.GET.get('servicename')
        if st != None:
            serviceData = Service.objects.filter(service_title__icontains = st)
            

    paginator = Paginator(serviceData,2)
    page_number = request.GET.get('page')
    serviceDatafinal = paginator.get_page(page_number)
    totalpage = serviceDatafinal.paginator.num_pages
    # serviceData = Service.objects.all().order_by('service_title') # ascending
    # serviceData = Service.objects.all().order_by('-service_title')[:1] # descending 
    # for a in serviceData:
    #     print(a.service_icon)
    # print(Service)
    
    data = {
        'serviceData' : serviceDatafinal , 
        'newsData' : newsData,  
        'totalpagelist' : [n+1 for n in range(totalpage)],
        'lastpage':totalpage,

    }
    return render(request,"index1.html",data)


def newsDetails(request,slug):
    newsDetails = News.objects.get(news_slug=slug)
    data = {
        'newsDetails':newsDetails
    }
    return render(request,"newsDetails.html",data)















def aboutus(request):
    return HttpResponse("Welcome To MySite !!!!")
def home(request):
    return HttpResponse("<h1>Welcome To MySite  Home Page !!!!</h1>")
def courseDetail(request,courseid):
    return HttpResponse(f"<h1>Welcome To MySite  {courseid} Page !!!!</h1>")
def userfrom(request):
    finalans = 0
    fn = userForm()
    data={'form' : fn}
    try:
        if request.method=="POST":

            # n1 = int(request.GET['num1'])
            # n2 = int(request.GET['num2'])
            # n3 = int(request.GET['num3'])
            # n1 = int(request.GET.get('num1'))
            # n2 = int(request.GET.get('num2'))
            # n3 = int(request.GET.get('num3'))
            n1 = int(request.POST.get('num1'))
            n2 = int(request.POST.get('num2'))
            n3 = int(request.POST.get('num3'))
            print(n1+n2+n3);
            finalans = (n1+n2+n3)
            data = {
                # 'n1': n1,
                # 'n2': n2,
                # 'n3': n3,
                'form' : fn,
                'output':finalans
            }
 
            url = "/homepage/?output={}".format(finalans)
            # return HttpResponseRedirect(url)
            return redirect(url)
    
    except:
        pass
       
    return render(request,"userfrom.html",data)

def submitfrom(request):
    finalans = 0
    data={}
    try:
        if request.method=="POST":

            # n1 = int(request.GET['num1'])
            # n2 = int(request.GET['num2'])
            # n3 = int(request.GET['num3'])
            # n1 = int(request.GET.get('num1'))
            # n2 = int(request.GET.get('num2'))
            # n3 = int(request.GET.get('num3'))
            n1 = int(request.POST.get('num1'))
            n2 = int(request.POST.get('num2'))
            n3 = int(request.POST.get('num3'))
            print(n1+n2+n3);
            finalans = (n1+n2+n3)
            data = {
                'n1': n1,
                'n2': n2,
                'n3': n3,
                'output':finalans
            }

            # url = "/homepage/?output={}".format(finalans)
            # return HttpResponseRedirect(url)
            # return redirect(url)
            return HttpResponse(finalans)
    
    except:
        pass