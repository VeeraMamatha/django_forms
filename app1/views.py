from django.shortcuts import render
from app1.models import *
from django.http import HttpResponse
from app1.forms import *

# Create your views here.
def djtopic(request):
    ETFO=topic_form()
    d={'etfo':ETFO}
    if request.method=='POST':
        TFDO=topic_form(request.POST)
        if TFDO.is_valid():
            tn=TFDO.cleaned_data['topic_name']
            to=Topic.objects.get_or_create(topic_name=tn)[0]
            to.save()
            return HttpResponse('topic table is created')
        
        else:
            return HttpResponse('data is not valid')


    return render(request,'topicforms.html',d)




def djwebpage(request):
    EWFO=webpage_form()
    d={'ewfo':EWFO}
    if request.method=='POST':
        WFDO=webpage_form(request.POST)
        if WFDO.is_valid():
            tn=WFDO.cleaned_data['topic_name']
            to=Topic.objects.get(topic_name=tn)
            n=WFDO.cleaned_data['name']
            u=WFDO.cleaned_data['url']
            e=WFDO.cleaned_data['email']
            w=Webpage.objects.get_or_create(topic_name=to,name=n,url=u,email=e)[0]
            w.save()
            return HttpResponse('webpage table is created')
        else:
            return HttpResponse('webpage is not valid')
    return render(request,'webpageforms.html',d)


def djaccessrecord(request):
    EAFO=accessrecord_form()
    d={'eafo':EAFO}
    if request.method=='POST':
        AFDO=accessrecord_form(request.POST)
        if AFDO.is_valid():
            n=AFDO.cleaned_data['name']
            ao=Webpage.objects.get(pk=n)
            d=AFDO.cleaned_data['date']
            au=AFDO.cleaned_data['author']
            a=AccessRecord.objects.get_or_create(name=ao,date=d,author=au)[0]
            a.save()
            return HttpResponse('accessrecord table is created')
        else:
            return HttpResponse('not created')



    return render(request,'accessrecordsforms.html',d)
