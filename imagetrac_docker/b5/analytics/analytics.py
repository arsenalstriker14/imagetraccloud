from django.shortcuts import render, redirect, render_to_response, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect, HttpResponseBadRequest, JsonResponse
from imagetrac_docker.b5.models import *
from imagetrac_docker.b5.forms import *
from django.template import Context, RequestContext
from django.db.models import Q, Count

# from django_pandas.io import read_frame

date = datetime.date.today()

def getCurrMonth(date):
        date = str(date)
        y = str(date[2:4])
        m = str(date[5:7])
        d = str(date[-2:])
        return m,y

datelist = getCurrMonth(date)
cmonth = datelist[0] 
if cmonth == '12':
    nmonth = '01'
else:
    nmonth = str(int(cmonth) + 1)
if len(nmonth) == 1:
    nmonth = "0" + nmonth

if cmonth == '01':
    lmonth = '12'
else:
    lmonth = str(int(cmonth) - 1)
if len(lmonth) == 1:
    lmonth = "0" + lmonth

if nmonth == '12':
    fmonth = '01'
else:
    fmonth = str(int(nmonth) + 1)
if len(fmonth) == 1:
    fmonth = "0" + fmonth

cyear = datelist[1]

def analytics(request):

    ilinks = []
    oplinks = []
    overlinks = []


    precords = Product.objects.count()
    countrecords = (Product.objects.filter(confirmed_placed__icontains="Jun").count() * 5)
    junintrecords = (Product.objects.filter(Q(first__exact='t') & Q(first_date__istartswith='06') & (Q(desc__icontains="NIKE") | Q(desc__icontains="UA") | Q(desc__icontains="UNDER"))).exclude(ad_date__isnull=False).exclude(confirmed_placed__isnull=True).exclude(confirmed_placed='').exclude(studio_out__isnull=False).count() * 5)
    # classrecords = Buyers.objects.all().order_by('buyer')
    classrecords = Buyers.objects.annotate(num_products=Count('product'))
    studioproducts = Product.objects.filter(studio_out__isnull=False).count()
    processedproducts = Product.objects.filter(confirmed_placed__isnull=False).count()
    vendorproducts = Product.objects.exclude(received_other__isnull=True).exclude(received_other__exact='').exclude(received_other__exact='None').count()

    #current month records
    cmthallrecords = ProcessedFiles.objects.filter(upload_date__istartswith=cmonth).count()
    cmthEMrecords = ProcessedFiles.objects.filter(Q(upload_date__istartswith=cmonth) & Q(processor__exact='eyemagic')).count()
    cmthEMfiles = ProcessedFiles.objects.filter(Q(upload_date__istartswith=cmonth) & Q(processor__exact='eyemagic'))
    cmthINTfiles = ProcessedFiles.objects.filter(upload_date__istartswith=cmonth).exclude(processor__exact='eyemagic')
    cmthEM_WEBrecords = ProcessedFiles.objects.filter(Q(upload_date__istartswith=cmonth) & Q(processor__exact='eyemagic')).exclude(filename__icontains='.eps').exclude(filename__icontains='.tif').count()
    cmthEM_PRINTrecords = ProcessedFiles.objects.filter(Q(upload_date__istartswith=cmonth) & Q(processor__exact='eyemagic') & (Q(filename__icontains='.eps') | Q(filename__icontains='.tif'))).count()
    cmthINTrecords = ProcessedFiles.objects.filter(upload_date__istartswith=cmonth).exclude(processor__exact='eyemagic').count()
    cmthINT_WEBrecords = ProcessedFiles.objects.filter(upload_date__istartswith=cmonth).exclude(processor__exact='eyemagic').exclude(filename__icontains='.eps').exclude(filename__icontains='.tif').count()
    cmthINT_PRINTrecords = ProcessedFiles.objects.filter(Q(upload_date__istartswith=cmonth) & (Q(filename__icontains='.eps') | Q(filename__icontains='.tif'))).exclude(processor__exact='eyemagic').count() 
    cmthCVS = ProcessedFiles.objects.values('sku').distinct()
    cmthCVSrecords = cmthCVS.filter(upload_date__istartswith=cmonth).count()
    cmthINTCVSrecords = cmthCVS.filter(upload_date__istartswith=cmonth).exclude(processor__exact='eyemagic').count()
    cmthEMCVSrecords = cmthCVS.filter(Q(upload_date__istartswith=cmonth) & Q(processor__exact='eyemagic')).count()

    #archival month records
    janallrecords = ProcessedFiles.objects.filter(upload_date__istartswith="01").count()
    janEMrecords = ProcessedFiles.objects.filter(Q(upload_date__istartswith="01") & Q(processor__exact='eyemagic')).count()
    janEMfiles = ProcessedFiles.objects.filter(Q(upload_date__istartswith="01") & Q(processor__exact='eyemagic'))
    janINTfiles = ProcessedFiles.objects.filter(upload_date__istartswith="01").exclude(processor__exact='eyemagic')
    janEM_WEBrecords = ProcessedFiles.objects.filter(Q(upload_date__istartswith="01") & Q(processor__exact='eyemagic')).exclude(filename__icontains='.eps').exclude(filename__icontains='.tif').count()
    janEM_PRINTrecords = ProcessedFiles.objects.filter(Q(upload_date__istartswith="01") & Q(processor__exact='eyemagic') & (Q(filename__icontains='.eps') | Q(filename__icontains='.tif'))).count()
    janINTrecords = ProcessedFiles.objects.filter(upload_date__istartswith="01").exclude(processor__exact='eyemagic').count()
    janINT_WEBrecords = ProcessedFiles.objects.filter(upload_date__istartswith="01").exclude(processor__exact='eyemagic').exclude(filename__icontains='.eps').exclude(filename__icontains='.tif').count()
    janINT_PRINTrecords = ProcessedFiles.objects.filter(Q(upload_date__istartswith="01") & (Q(filename__icontains='.eps') | Q(filename__icontains='.tif'))).exclude(processor__exact='eyemagic').count() 
    janCVS = ProcessedFiles.objects.values('sku').distinct()
    janCVSrecords = janCVS.filter(upload_date__istartswith="01").count()
    janINTCVSrecords = janCVS.filter(upload_date__istartswith="01").exclude(processor__exact='eyemagic').count()
    janEMCVSrecords = janCVS.filter(Q(upload_date__istartswith="01") & Q(processor__exact='eyemagic')).count()

    feballrecords = ProcessedFiles.objects.filter(upload_date__istartswith="02").count()
    febEMrecords = ProcessedFiles.objects.filter(Q(upload_date__istartswith="02") & Q(processor__exact='eyemagic')).count()
    febEMfiles = ProcessedFiles.objects.filter(Q(upload_date__istartswith="02") & Q(processor__exact='eyemagic'))
    febINTfiles = ProcessedFiles.objects.filter(upload_date__istartswith="02").exclude(processor__exact='eyemagic')
    febEM_WEBrecords = ProcessedFiles.objects.filter(Q(upload_date__istartswith="02") & Q(processor__exact='eyemagic')).exclude(filename__icontains='.eps').exclude(filename__icontains='.tif').count()
    febEM_PRINTrecords = ProcessedFiles.objects.filter(Q(upload_date__istartswith="02") & Q(processor__exact='eyemagic') & (Q(filename__icontains='.eps') | Q(filename__icontains='.tif'))).count()
    febINTrecords = ProcessedFiles.objects.filter(upload_date__istartswith="02").exclude(processor__exact='eyemagic').count()
    febINT_WEBrecords = ProcessedFiles.objects.filter(upload_date__istartswith="02").exclude(processor__exact='eyemagic').exclude(filename__icontains='.eps').exclude(filename__icontains='.tif').count()
    febINT_PRINTrecords = ProcessedFiles.objects.filter(Q(upload_date__istartswith="02") & (Q(filename__icontains='.eps') | Q(filename__icontains='.tif'))).exclude(processor__exact='eyemagic').count() 
    febCVS = ProcessedFiles.objects.values('sku').distinct()
    febCVSrecords = febCVS.filter(upload_date__istartswith="02").count()
    febINTCVSrecords = febCVS.filter(upload_date__istartswith="02").exclude(processor__exact='eyemagic').count()
    febEMCVSrecords = febCVS.filter(Q(upload_date__istartswith="02") & Q(processor__exact='eyemagic')).count()

    marallrecords = ProcessedFiles.objects.filter(upload_date__istartswith="03").count()
    marEMrecords = ProcessedFiles.objects.filter(Q(upload_date__istartswith="03") & Q(processor__exact='eyemagic')).count()
    marEMfiles = ProcessedFiles.objects.filter(Q(upload_date__istartswith="03") & Q(processor__exact='eyemagic'))
    marINTfiles = ProcessedFiles.objects.filter(upload_date__istartswith="03").exclude(processor__exact='eyemagic')
    marEM_WEBrecords = ProcessedFiles.objects.filter(Q(upload_date__istartswith="03") & Q(processor__exact='eyemagic')).exclude(filename__icontains='.eps').exclude(filename__icontains='.tif').count()
    marEM_PRINTrecords = ProcessedFiles.objects.filter(Q(upload_date__istartswith="03") & Q(processor__exact='eyemagic') & (Q(filename__icontains='.eps') | Q(filename__icontains='.tif'))).count()
    marINTrecords = ProcessedFiles.objects.filter(upload_date__istartswith="03").exclude(processor__exact='eyemagic').count()
    marINT_WEBrecords = ProcessedFiles.objects.filter(upload_date__istartswith="03").exclude(processor__exact='eyemagic').exclude(filename__icontains='.eps').exclude(filename__icontains='.tif').count()
    marINT_PRINTrecords = ProcessedFiles.objects.filter(Q(upload_date__istartswith="03") & (Q(filename__icontains='.eps') | Q(filename__icontains='.tif'))).exclude(processor__exact='eyemagic').count() 
    marCVS = ProcessedFiles.objects.values('sku').distinct()
    marCVSrecords = marCVS.filter(upload_date__istartswith="03").count()
    marINTCVSrecords = marCVS.filter(upload_date__istartswith="03").exclude(processor__exact='eyemagic').count()
    marEMCVSrecords = marCVS.filter(Q(upload_date__istartswith="03") & Q(processor__exact='eyemagic')).count()

    aprallrecords = ProcessedFiles.objects.filter(upload_date__istartswith="04").count()
    aprEMrecords = ProcessedFiles.objects.filter(Q(upload_date__istartswith="04") & Q(processor__exact='eyemagic')).count()
    aprEMfiles = ProcessedFiles.objects.filter(Q(upload_date__istartswith="04") & Q(processor__exact='eyemagic'))
    aprINTfiles = ProcessedFiles.objects.filter(upload_date__istartswith="04").exclude(processor__exact='eyemagic')
    aprEM_WEBrecords = ProcessedFiles.objects.filter(Q(upload_date__istartswith="04") & Q(processor__exact='eyemagic')).exclude(filename__icontains='.eps').exclude(filename__icontains='.tif').count()
    aprEM_PRINTrecords = ProcessedFiles.objects.filter(Q(upload_date__istartswith="04") & Q(processor__exact='eyemagic') & (Q(filename__icontains='.eps') | Q(filename__icontains='.tif'))).count()
    aprINTrecords = ProcessedFiles.objects.filter(upload_date__istartswith="04").exclude(processor__exact='eyemagic').count()
    aprINT_WEBrecords = ProcessedFiles.objects.filter(upload_date__istartswith="04").exclude(processor__exact='eyemagic').exclude(filename__icontains='.eps').exclude(filename__icontains='.tif').count()
    aprINT_PRINTrecords = ProcessedFiles.objects.filter(Q(upload_date__istartswith="04") & (Q(filename__icontains='.eps') | Q(filename__icontains='.tif'))).exclude(processor__exact='eyemagic').count() 
    aprCVS = ProcessedFiles.objects.values('sku').distinct()
    aprCVSrecords = aprCVS.filter(upload_date__istartswith="04").count()
    aprINTCVSrecords = aprCVS.filter(upload_date__istartswith="04").exclude(processor__exact='eyemagic').count()
    aprEMCVSrecords = aprCVS.filter(Q(upload_date__istartswith="04") & Q(processor__exact='eyemagic')).count()

    mayallrecords = ProcessedFiles.objects.filter(upload_date__istartswith="05").count()
    mayEMrecords = ProcessedFiles.objects.filter(Q(upload_date__istartswith="05") & Q(processor__exact='eyemagic')).count()
    mayEMfiles = ProcessedFiles.objects.filter(Q(upload_date__istartswith="05") & Q(processor__exact='eyemagic'))
    mayINTfiles = ProcessedFiles.objects.filter(upload_date__istartswith="05").exclude(processor__exact='eyemagic')
    mayEM_WEBrecords = ProcessedFiles.objects.filter(Q(upload_date__istartswith="05") & Q(processor__exact='eyemagic')).exclude(filename__icontains='.eps').exclude(filename__icontains='.tif').count()
    mayEM_PRINTrecords = ProcessedFiles.objects.filter(Q(upload_date__istartswith="05") & Q(processor__exact='eyemagic') & (Q(filename__icontains='.eps') | Q(filename__icontains='.tif'))).count()
    mayINTrecords = ProcessedFiles.objects.filter(upload_date__istartswith="05").exclude(processor__exact='eyemagic').count()
    mayINT_WEBrecords = ProcessedFiles.objects.filter(upload_date__istartswith="05").exclude(processor__exact='eyemagic').exclude(filename__icontains='.eps').exclude(filename__icontains='.tif').count()
    mayINT_PRINTrecords = ProcessedFiles.objects.filter(Q(upload_date__istartswith="05") & (Q(filename__icontains='.eps') | Q(filename__icontains='.tif'))).exclude(processor__exact='eyemagic').count() 
    mayCVS = ProcessedFiles.objects.values('sku').distinct()
    mayCVSrecords = mayCVS.filter(upload_date__istartswith="05").count()
    mayINTCVSrecords = mayCVS.filter(upload_date__istartswith="05").exclude(processor__exact='eyemagic').count()
    mayEMCVSrecords = mayCVS.filter(Q(upload_date__istartswith="05") & Q(processor__exact='eyemagic')).count()


    junallrecords = ProcessedFiles.objects.filter(upload_date__istartswith="06").count()
    junEMrecords = ProcessedFiles.objects.filter(Q(upload_date__istartswith="06") & Q(processor__exact='eyemagic')).count()
    junEMfiles = ProcessedFiles.objects.filter(Q(upload_date__istartswith="06") & Q(processor__exact='eyemagic'))
    junINTfiles = ProcessedFiles.objects.filter(upload_date__istartswith="06").exclude(processor__exact='eyemagic')
    junEM_WEBrecords = ProcessedFiles.objects.filter(Q(upload_date__istartswith="06") & Q(processor__exact='eyemagic')).exclude(filename__icontains='.eps').exclude(filename__icontains='.tif').count()
    junEM_PRINTrecords = ProcessedFiles.objects.filter(Q(upload_date__istartswith="06") & Q(processor__exact='eyemagic') & (Q(filename__icontains='.eps') | Q(filename__icontains='.tif'))).count()
    junINTrecords = ProcessedFiles.objects.filter(upload_date__istartswith="06").exclude(processor__exact='eyemagic').count()
    junINT_WEBrecords = ProcessedFiles.objects.filter(upload_date__istartswith="06").exclude(processor__exact='eyemagic').exclude(filename__icontains='.eps').exclude(filename__icontains='.tif').count()
    junINT_PRINTrecords = ProcessedFiles.objects.filter(Q(upload_date__istartswith="06") & (Q(filename__icontains='.eps') | Q(filename__icontains='.tif'))).exclude(processor__exact='eyemagic').count() 
    junCVS = ProcessedFiles.objects.values('sku').distinct()
    junCVSrecords = junCVS.filter(upload_date__istartswith="06").count()
    junINTCVSrecords = junCVS.filter(upload_date__istartswith="06").exclude(processor__exact='eyemagic').count()
    junEMCVSrecords = junCVS.filter(Q(upload_date__istartswith="06") & Q(processor__exact='eyemagic')).count()


    julallrecords = ProcessedFiles.objects.filter(upload_date__istartswith="07").count()
    julEMrecords = ProcessedFiles.objects.filter(Q(upload_date__istartswith="07") & Q(processor__exact='eyemagic')).count()
    julEMfiles = ProcessedFiles.objects.filter(Q(upload_date__istartswith="07") & Q(processor__exact='eyemagic'))
    julINTfiles = ProcessedFiles.objects.filter(upload_date__istartswith="07").exclude(processor__exact='eyemagic')
    julEM_WEBrecords = ProcessedFiles.objects.filter(Q(upload_date__istartswith="07") & Q(processor__exact='eyemagic')).exclude(filename__icontains='.eps').exclude(filename__icontains='.tif').count()
    julEM_PRINTrecords = ProcessedFiles.objects.filter(Q(upload_date__istartswith="07") & Q(processor__exact='eyemagic') & (Q(filename__icontains='.eps') | Q(filename__icontains='.tif'))).count()
    julINTrecords = ProcessedFiles.objects.filter(upload_date__istartswith="07").exclude(processor__exact='eyemagic').count()
    julINT_WEBrecords = ProcessedFiles.objects.filter(upload_date__istartswith="07").exclude(processor__exact='eyemagic').exclude(filename__icontains='.eps').exclude(filename__icontains='.tif').count()
    julINT_PRINTrecords = ProcessedFiles.objects.filter(Q(upload_date__istartswith="07") & (Q(filename__icontains='.eps') | Q(filename__icontains='.tif'))).exclude(processor__exact='eyemagic').count() 
    julCVS = ProcessedFiles.objects.values('sku').distinct()
    julCVSrecords = julCVS.filter(upload_date__istartswith="07").count()
    julINTCVSrecords = julCVS.filter(upload_date__istartswith="07").exclude(processor__exact='eyemagic').count()
    julEMCVSrecords = julCVS.filter(Q(upload_date__istartswith="07") & Q(processor__exact='eyemagic')).count()

    augallrecords = ProcessedFiles.objects.filter(upload_date__istartswith="08").count()
    augEMrecords = ProcessedFiles.objects.filter(Q(upload_date__istartswith="08") & Q(processor__exact='eyemagic')).count()
    augEMfiles = ProcessedFiles.objects.filter(Q(upload_date__istartswith="08") & Q(processor__exact='eyemagic'))
    augINTfiles = ProcessedFiles.objects.filter(upload_date__istartswith="08").exclude(processor__exact='eyemagic')
    augEM_WEBrecords = ProcessedFiles.objects.filter(Q(upload_date__istartswith="08") & Q(processor__exact='eyemagic')).exclude(filename__icontains='.eps').exclude(filename__icontains='.tif').count()
    augEM_PRINTrecords = ProcessedFiles.objects.filter(Q(upload_date__istartswith="08") & Q(processor__exact='eyemagic') & (Q(filename__icontains='.eps') | Q(filename__icontains='.tif'))).count()
    augINTrecords = ProcessedFiles.objects.filter(upload_date__istartswith="08").exclude(processor__exact='eyemagic').count()
    augINT_WEBrecords = ProcessedFiles.objects.filter(upload_date__istartswith="08").exclude(processor__exact='eyemagic').exclude(filename__icontains='.eps').exclude(filename__icontains='.tif').count()
    augINT_PRINTrecords = ProcessedFiles.objects.filter(Q(upload_date__istartswith="08") & (Q(filename__icontains='.eps') | Q(filename__icontains='.tif'))).exclude(processor__exact='eyemagic').count() 
    augCVS = ProcessedFiles.objects.values('sku').distinct()
    augCVSrecords = augCVS.filter(upload_date__istartswith="08").count()
    augINTCVSrecords = augCVS.filter(upload_date__istartswith="08").exclude(processor__exact='eyemagic').count()
    augEMCVSrecords = augCVS.filter(Q(upload_date__istartswith="08") & Q(processor__exact='eyemagic')).count()

    sepallrecords = ProcessedFiles.objects.filter(upload_date__istartswith="09").count()
    sepEMrecords = ProcessedFiles.objects.filter(Q(upload_date__istartswith="09") & Q(processor__exact='eyemagic')).count()
    sepEMfiles = ProcessedFiles.objects.filter(Q(upload_date__istartswith="09") & Q(processor__exact='eyemagic'))
    sepINTfiles = ProcessedFiles.objects.filter(upload_date__istartswith="09").exclude(processor__exact='eyemagic')
    sepEM_WEBrecords = ProcessedFiles.objects.filter(Q(upload_date__istartswith="09") & Q(processor__exact='eyemagic')).exclude(filename__icontains='.eps').exclude(filename__icontains='.tif').count()
    sepEM_PRINTrecords = ProcessedFiles.objects.filter(Q(upload_date__istartswith="09") & Q(processor__exact='eyemagic') & (Q(filename__icontains='.eps') | Q(filename__icontains='.tif'))).count()
    sepINTrecords = ProcessedFiles.objects.filter(upload_date__istartswith="09").exclude(processor__exact='eyemagic').count()
    sepINT_WEBrecords = ProcessedFiles.objects.filter(upload_date__istartswith="09").exclude(processor__exact='eyemagic').exclude(filename__icontains='.eps').exclude(filename__icontains='.tif').count()
    sepINT_PRINTrecords = ProcessedFiles.objects.filter(Q(upload_date__istartswith="09") & (Q(filename__icontains='.eps') | Q(filename__icontains='.tif'))).exclude(processor__exact='eyemagic').count() 
    sepCVS = ProcessedFiles.objects.values('sku').distinct()
    sepCVSrecords = sepCVS.filter(upload_date__istartswith="09").count()
    sepINTCVSrecords = sepCVS.filter(upload_date__istartswith="09").exclude(processor__exact='eyemagic').count()
    sepEMCVSrecords = sepCVS.filter(Q(upload_date__istartswith="09") & Q(processor__exact='eyemagic')).count()

    octallrecords = ProcessedFiles.objects.filter(upload_date__istartswith="10").count()
    octEMrecords = ProcessedFiles.objects.filter(Q(upload_date__istartswith="10") & Q(processor__exact='eyemagic')).count()
    octEMfiles = ProcessedFiles.objects.filter(Q(upload_date__istartswith="10") & Q(processor__exact='eyemagic'))
    octINTfiles = ProcessedFiles.objects.filter(upload_date__istartswith="10").exclude(processor__exact='eyemagic')
    octEM_WEBrecords = ProcessedFiles.objects.filter(Q(upload_date__istartswith="10") & Q(processor__exact='eyemagic')).exclude(filename__icontains='.eps').exclude(filename__icontains='.tif').count()
    octEM_PRINTrecords = ProcessedFiles.objects.filter(Q(upload_date__istartswith="10") & Q(processor__exact='eyemagic') & (Q(filename__icontains='.eps') | Q(filename__icontains='.tif'))).count()
    octINTrecords = ProcessedFiles.objects.filter(upload_date__istartswith="10").exclude(processor__exact='eyemagic').count()
    octINT_WEBrecords = ProcessedFiles.objects.filter(upload_date__istartswith="10").exclude(processor__exact='eyemagic').exclude(filename__icontains='.eps').exclude(filename__icontains='.tif').count()
    octINT_PRINTrecords = ProcessedFiles.objects.filter(Q(upload_date__istartswith="10") & (Q(filename__icontains='.eps') | Q(filename__icontains='.tif'))).exclude(processor__exact='eyemagic').count() 
    octCVS = ProcessedFiles.objects.values('sku').distinct()
    octCVSrecords = octCVS.filter(upload_date__istartswith="10").count()
    octINTCVSrecords = octCVS.filter(upload_date__istartswith="10").exclude(processor__exact='eyemagic').count()
    octEMCVSrecords = octCVS.filter(Q(upload_date__istartswith="10") & Q(processor__exact='eyemagic')).count()

    novallrecords = ProcessedFiles.objects.filter(upload_date__istartswith="11").count()
    novEMrecords = ProcessedFiles.objects.filter(Q(upload_date__istartswith="11") & Q(processor__exact='eyemagic')).count()
    novEMfiles = ProcessedFiles.objects.filter(Q(upload_date__istartswith="11") & Q(processor__exact='eyemagic'))
    novINTfiles = ProcessedFiles.objects.filter(upload_date__istartswith="11").exclude(processor__exact='eyemagic')
    novEM_WEBrecords = ProcessedFiles.objects.filter(Q(upload_date__istartswith="11") & Q(processor__exact='eyemagic')).exclude(filename__icontains='.eps').exclude(filename__icontains='.tif').count()
    novEM_PRINTrecords = ProcessedFiles.objects.filter(Q(upload_date__istartswith="11") & Q(processor__exact='eyemagic') & (Q(filename__icontains='.eps') | Q(filename__icontains='.tif'))).count()
    novINTrecords = ProcessedFiles.objects.filter(upload_date__istartswith="11").exclude(processor__exact='eyemagic').count()
    novINT_WEBrecords = ProcessedFiles.objects.filter(upload_date__istartswith="11").exclude(processor__exact='eyemagic').exclude(filename__icontains='.eps').exclude(filename__icontains='.tif').count()
    novINT_PRINTrecords = ProcessedFiles.objects.filter(Q(upload_date__istartswith="11") & (Q(filename__icontains='.eps') | Q(filename__icontains='.tif'))).exclude(processor__exact='eyemagic').count() 
    novCVS = ProcessedFiles.objects.values('sku').distinct()
    novCVSrecords = novCVS.filter(upload_date__istartswith="11").count()
    novINTCVSrecords = novCVS.filter(upload_date__istartswith="11").exclude(processor__exact='eyemagic').count()
    novEMCVSrecords = novCVS.filter(Q(upload_date__istartswith="11") & Q(processor__exact='eyemagic')).count()


    decallrecords = ProcessedFiles.objects.filter(upload_date__istartswith="12").count()
    decEMrecords = ProcessedFiles.objects.filter(Q(upload_date__istartswith="12") & Q(processor__exact='eyemagic')).count()
    decEMfiles = ProcessedFiles.objects.filter(Q(upload_date__istartswith="12") & Q(processor__exact='eyemagic'))
    decINTfiles = ProcessedFiles.objects.filter(upload_date__istartswith="12").exclude(processor__exact='eyemagic')
    decEM_WEBrecords = ProcessedFiles.objects.filter(Q(upload_date__istartswith="12") & Q(processor__exact='eyemagic')).exclude(filename__icontains='.eps').exclude(filename__icontains='.tif').count()
    decEM_PRINTrecords = ProcessedFiles.objects.filter(Q(upload_date__istartswith="12") & Q(processor__exact='eyemagic') & (Q(filename__icontains='.eps') | Q(filename__icontains='.tif'))).count()
    decINTrecords = ProcessedFiles.objects.filter(upload_date__istartswith="12").exclude(processor__exact='eyemagic').count()
    decINT_WEBrecords = ProcessedFiles.objects.filter(upload_date__istartswith="12").exclude(processor__exact='eyemagic').exclude(filename__icontains='.eps').exclude(filename__icontains='.tif').count()
    decINT_PRINTrecords = ProcessedFiles.objects.filter(Q(upload_date__istartswith="12") & (Q(filename__icontains='.eps') | Q(filename__icontains='.tif'))).exclude(processor__exact='eyemagic').count() 
    decCVS = ProcessedFiles.objects.values('sku').distinct()
    decCVSrecords = decCVS.filter(upload_date__istartswith="12").count()
    decINTCVSrecords = decCVS.filter(upload_date__istartswith="12").exclude(processor__exact='eyemagic').count()
    decEMCVSrecords = decCVS.filter(Q(upload_date__istartswith="12") & Q(processor__exact='eyemagic')).count()




    #year to date records
    ytdallrecords = ProcessedFiles.objects.filter(upload_date__iendswith=cyear).count()
    ytdEMrecords = ProcessedFiles.objects.filter(Q(upload_date__iendswith=cyear) & Q(processor__exact='eyemagic')).count()
    ytdINTrecords = ProcessedFiles.objects.filter(upload_date__iendswith=cyear).exclude(processor__exact='eyemagic').count()
    ytdEMfiles = ProcessedFiles.objects.filter(Q(upload_date__iendswith=cyear) & Q(processor__exact='eyemagic'))
    ytdINTfiles = ProcessedFiles.objects.filter(upload_date__iendswith=cyear).exclude(processor__exact='eyemagic')
    ytdEM_WEBrecords = ProcessedFiles.objects.filter(Q(upload_date__iendswith=cyear) & Q(processor__exact='eyemagic')).exclude(filename__icontains='.eps').exclude(filename__icontains='.tif').count()
    ytdEM_PRINTrecords = ProcessedFiles.objects.filter(Q(upload_date__iendswith=cyear) & Q(processor__exact='eyemagic') & (Q(filename__icontains='.eps') | Q(filename__icontains='.tif'))).count()
    ytdINTrecords = ProcessedFiles.objects.filter(upload_date__iendswith=cyear).exclude(processor__exact='eyemagic').count()
    ytdINT_WEBrecords = ProcessedFiles.objects.filter(upload_date__iendswith=cyear).exclude(processor__exact='eyemagic').exclude(filename__icontains='.eps').exclude(filename__icontains='.tif').count()
    ytdINT_PRINTrecords = ProcessedFiles.objects.filter(Q(upload_date__iendswith=cyear) & (Q(filename__icontains='.eps') | Q(filename__icontains='.tif'))).exclude(processor__exact='eyemagic').count() 
    ytdCVS = ProcessedFiles.objects.values('sku').distinct()
    ytdCVSrecords = cmthCVS.filter(upload_date__iendswith=cyear).count()
    ytdINTCVSrecords = cmthCVS.filter(upload_date__iendswith=cyear).exclude(processor__exact='eyemagic').count()
    ytdEMCVSrecords = cmthCVS.filter(Q(upload_date__iendswith=cyear) & Q(processor__exact='eyemagic')).count()


    show_results = True
    if 'query' in request.GET:
        show_results = True

        query = request.GET['query'].strip()

        if query == "dupes":
            for record in cmthEMfiles:
                for item in cmthINTfiles:
                    if item.filename == record.filename:
                        overlinks.append(item)

        elif query == "internal":
            form = PostsearchForm({'query' : query})
            ilinks = ProcessedFiles.objects.all().exclude(processor__iexact='eyemagic')

        elif query:
            form = PostsearchForm({'query' : query})
            oplinks = ProcessedFiles.objects.filter(processor__iexact=query)
            # skulinks = Product.objects.filter( Q(sku__iexact=query) | Q(sku_ns__iexact=query) )
            # imagelinks = ThumbWebfiles.objects.filter(sku__iexact=query)
            # buylinks = Product.objects.filter(buyer__icontains=query)


    if len(ilinks) >= 1:
        oplinks = ProcessedFiles.objects.all().exclude(processor__iexact='eyemagic')
        tmp = "test/analytics.html"
        variables = RequestContext(request, {'form':form, 'oplinks': oplinks, 'cmthEMfiles': cmthEMfiles, 'cmthINTfiles': cmthINTfiles, 'precords': precords, 'classrecords': classrecords, 'cmthallrecords': cmthallrecords, 
            'cmthEMCVSrecords': cmthEMCVSrecords, 'cmthINTCVSrecords': cmthINTCVSrecords, 'cmthEMrecords': cmthEMrecords, 'cmthEM_WEBrecords': cmthEM_WEBrecords, 'cmthEM_PRINTrecords': cmthEM_PRINTrecords, 'cmthINTrecords': cmthINTrecords, 
            'cmthINT_WEBrecords': cmthINT_WEBrecords, 'cmthINT_PRINTrecords': cmthINT_PRINTrecords, 'ytdallrecords': ytdallrecords, 'ytdEMrecords': ytdEMrecords, 'ytdINTrecords': ytdINTrecords, 'ytdEM_WEBrecords': ytdEM_WEBrecords, 
            'ytdEM_PRINTrecords': ytdEM_PRINTrecords, 'ytdINT_WEBrecords': ytdINT_WEBrecords, 'ytdINT_PRINTrecords': ytdINT_PRINTrecords, 'ytdCVSrecords': ytdCVSrecords, 'ytdEMCVSrecords': ytdEMCVSrecords, 'ytdINTCVSrecords': ytdINTCVSrecords, 
            'studioproducts': studioproducts, 'processedproducts': processedproducts, 'vendorproducts': vendorproducts, 'janEMfiles': janEMfiles, 'janINTfiles': janINTfiles, 'janallrecords': janallrecords, 
            'janEMCVSrecords': janEMCVSrecords, 'janINTCVSrecords': janINTCVSrecords, 'janEMrecords': janEMrecords, 'janEM_WEBrecords': janEM_WEBrecords, 'janEM_PRINTrecords': janEM_PRINTrecords, 'janINTrecords': janINTrecords, 
            'janINT_WEBrecords': janINT_WEBrecords, 'janINT_PRINTrecords': janINT_PRINTrecords,'febEMfiles': febEMfiles, 'febINTfiles': febINTfiles, 'feballrecords': feballrecords, 
            'febEMCVSrecords': febEMCVSrecords, 'febINTCVSrecords': febINTCVSrecords, 'febEMrecords': febEMrecords, 'febEM_WEBrecords': febEM_WEBrecords, 'febEM_PRINTrecords': febEM_PRINTrecords, 'febINTrecords': febINTrecords, 
            'febINT_WEBrecords': febINT_WEBrecords, 'febINT_PRINTrecords': febINT_PRINTrecords, 'marEMfiles': marEMfiles, 'marINTfiles': marINTfiles, 'marallrecords': marallrecords, 
            'marEMCVSrecords': marEMCVSrecords, 'marINTCVSrecords': marINTCVSrecords, 'marEMrecords': marEMrecords, 'marEM_WEBrecords': marEM_WEBrecords, 'marEM_PRINTrecords': marEM_PRINTrecords, 'marINTrecords': marINTrecords, 
            'marINT_WEBrecords': marINT_WEBrecords, 'marINT_PRINTrecords': marINT_PRINTrecords, 'aprEMfiles': aprEMfiles, 'aprINTfiles': aprINTfiles, 'aprallrecords': aprallrecords, 
            'aprEMCVSrecords': aprEMCVSrecords, 'aprINTCVSrecords': aprINTCVSrecords, 'aprEMrecords': aprEMrecords, 'aprEM_WEBrecords': aprEM_WEBrecords, 'aprEM_PRINTrecords': aprEM_PRINTrecords, 'aprINTrecords': aprINTrecords, 
            'aprINT_WEBrecords': aprINT_WEBrecords, 'aprINT_PRINTrecords': aprINT_PRINTrecords,'mayEMfiles': mayEMfiles, 'mayINTfiles': mayINTfiles, 'mayallrecords': mayallrecords, 'mayEMCVSrecords': mayEMCVSrecords, 'mayINTCVSrecords': mayINTCVSrecords, 'mayEMrecords': mayEMrecords, 'mayEM_WEBrecords': mayEM_WEBrecords, 'mayEM_PRINTrecords': mayEM_PRINTrecords, 'mayINTrecords': mayINTrecords, 
            'mayINT_WEBrecords': mayINT_WEBrecords, 'mayINT_PRINTrecords': mayINT_PRINTrecords, 'junEMfiles': junEMfiles, 'junINTfiles': junINTfiles, 'junallrecords': junallrecords, 
            'junEMCVSrecords': junEMCVSrecords, 'junINTCVSrecords': junINTCVSrecords, 'junEMrecords': junEMrecords, 'junEM_WEBrecords': junEM_WEBrecords, 'junEM_PRINTrecords': junEM_PRINTrecords, 'junINTrecords': junINTrecords, 
            'junINT_WEBrecords': junINT_WEBrecords, 'junINT_PRINTrecords': junINT_PRINTrecords, 'julEMfiles': julEMfiles, 'julINTfiles': julINTfiles, 'julallrecords': julallrecords, 
            'julEMCVSrecords': julEMCVSrecords, 'julINTCVSrecords': julINTCVSrecords, 'julEMrecords': julEMrecords, 'julEM_WEBrecords': julEM_WEBrecords, 'julEM_PRINTrecords': julEM_PRINTrecords, 'julINTrecords': julINTrecords, 
            'julINT_WEBrecords': julINT_WEBrecords, 'julINT_PRINTrecords': julINT_PRINTrecords,'augEMfiles': augEMfiles, 'augINTfiles': augINTfiles, 'augallrecords': augallrecords, 
            'augEMCVSrecords': augEMCVSrecords, 'augINTCVSrecords': augINTCVSrecords, 'augEMrecords': augEMrecords, 'augEM_WEBrecords': augEM_WEBrecords, 'augEM_PRINTrecords': augEM_PRINTrecords, 'augINTrecords': augINTrecords, 
            'augINT_WEBrecords': augINT_WEBrecords, 'augINT_PRINTrecords': augINT_PRINTrecords, 'sepEMfiles': sepEMfiles, 'sepINTfiles': sepINTfiles, 'sepallrecords': sepallrecords, 
            'sepEMCVSrecords': sepEMCVSrecords, 'sepINTCVSrecords': sepINTCVSrecords, 'sepEMrecords': sepEMrecords, 'sepEM_WEBrecords': sepEM_WEBrecords, 'sepEM_PRINTrecords': sepEM_PRINTrecords, 'sepINTrecords': sepINTrecords, 
            'sepINT_WEBrecords': sepINT_WEBrecords, 'sepINT_PRINTrecords': sepINT_PRINTrecords, 'octEMfiles': octEMfiles, 'octINTfiles': octINTfiles, 'octallrecords': octallrecords, 
            'octEMCVSrecords': octEMCVSrecords, 'octINTCVSrecords': octINTCVSrecords, 'octEMrecords': octEMrecords, 'octEM_WEBrecords': octEM_WEBrecords, 'octEM_PRINTrecords': octEM_PRINTrecords, 'octINTrecords': octINTrecords, 
            'octINT_WEBrecords': octINT_WEBrecords, 'octINT_PRINTrecords': octINT_PRINTrecords,'novEMfiles': novEMfiles, 'novINTfiles': novINTfiles, 'novallrecords': novallrecords, 'novEMCVSrecords': novEMCVSrecords, 'novINTCVSrecords': novINTCVSrecords, 'novEMrecords': novEMrecords, 'novEM_WEBrecords': novEM_WEBrecords, 'novEM_PRINTrecords': novEM_PRINTrecords, 'novINTrecords': novINTrecords, 
            'novINT_WEBrecords': novINT_WEBrecords, 'novINT_PRINTrecords': novINT_PRINTrecords, 'decEMfiles': decEMfiles, 'decINTfiles': decINTfiles, 'decallrecords': decallrecords, 
            'decEMCVSrecords': decEMCVSrecords, 'decINTCVSrecords': decINTCVSrecords, 'decEMrecords': decEMrecords, 'decEM_WEBrecords': decEM_WEBrecords, 'decEM_PRINTrecords': decEM_PRINTrecords, 'decINTrecords': decINTrecords, 
            'decINT_WEBrecords': decINT_WEBrecords, 'decINT_PRINTrecords': decINT_PRINTrecords })
        return render_to_response(tmp, variables)


    elif len(overlinks) >= 1:

        tmp = "test/analytics.html"
        variables = RequestContext(request, {'form':form, 'overlinks': overlinks, 'cmthEMfiles': cmthEMfiles, 'cmthINTfiles': cmthINTfiles, 'precords': precords, 'classrecords': classrecords, 'cmthallrecords': cmthallrecords, 
            'cmthEMCVSrecords': cmthEMCVSrecords, 'cmthINTCVSrecords': cmthINTCVSrecords, 'cmthEMrecords': cmthEMrecords, 'cmthEM_WEBrecords': cmthEM_WEBrecords, 'cmthEM_PRINTrecords': cmthEM_PRINTrecords, 'cmthINTrecords': cmthINTrecords, 
            'cmthINT_WEBrecords': cmthINT_WEBrecords, 'cmthINT_PRINTrecords': cmthINT_PRINTrecords, 'ytdallrecords': ytdallrecords, 'ytdEMrecords': ytdEMrecords, 'ytdINTrecords': ytdINTrecords, 'ytdEM_WEBrecords': ytdEM_WEBrecords, 
            'ytdEM_PRINTrecords': ytdEM_PRINTrecords, 'ytdINT_WEBrecords': ytdINT_WEBrecords, 'ytdINT_PRINTrecords': ytdINT_PRINTrecords, 'ytdCVSrecords': ytdCVSrecords, 'ytdEMCVSrecords': ytdEMCVSrecords, 'ytdINTCVSrecords': ytdINTCVSrecords, 
            'studioproducts': studioproducts, 'processedproducts': processedproducts, 'vendorproducts': vendorproducts, 'janEMfiles': janEMfiles, 'janINTfiles': janINTfiles, 'janallrecords': janallrecords, 
            'janEMCVSrecords': janEMCVSrecords, 'janINTCVSrecords': janINTCVSrecords, 'janEMrecords': janEMrecords, 'janEM_WEBrecords': janEM_WEBrecords, 'janEM_PRINTrecords': janEM_PRINTrecords, 'janINTrecords': janINTrecords, 
            'janINT_WEBrecords': janINT_WEBrecords, 'janINT_PRINTrecords': janINT_PRINTrecords,'febEMfiles': febEMfiles, 'febINTfiles': febINTfiles, 'feballrecords': feballrecords, 
            'febEMCVSrecords': febEMCVSrecords, 'febINTCVSrecords': febINTCVSrecords, 'febEMrecords': febEMrecords, 'febEM_WEBrecords': febEM_WEBrecords, 'febEM_PRINTrecords': febEM_PRINTrecords, 'febINTrecords': febINTrecords, 
            'febINT_WEBrecords': febINT_WEBrecords, 'febINT_PRINTrecords': febINT_PRINTrecords, 'marEMfiles': marEMfiles, 'marINTfiles': marINTfiles, 'marallrecords': marallrecords, 
            'marEMCVSrecords': marEMCVSrecords, 'marINTCVSrecords': marINTCVSrecords, 'marEMrecords': marEMrecords, 'marEM_WEBrecords': marEM_WEBrecords, 'marEM_PRINTrecords': marEM_PRINTrecords, 'marINTrecords': marINTrecords, 
            'marINT_WEBrecords': marINT_WEBrecords, 'marINT_PRINTrecords': marINT_PRINTrecords, 'aprEMfiles': aprEMfiles, 'aprINTfiles': aprINTfiles, 'aprallrecords': aprallrecords, 
            'aprEMCVSrecords': aprEMCVSrecords, 'aprINTCVSrecords': aprINTCVSrecords, 'aprEMrecords': aprEMrecords, 'aprEM_WEBrecords': aprEM_WEBrecords, 'aprEM_PRINTrecords': aprEM_PRINTrecords, 'aprINTrecords': aprINTrecords, 
            'aprINT_WEBrecords': aprINT_WEBrecords, 'aprINT_PRINTrecords': aprINT_PRINTrecords, 'mayEMfiles': mayEMfiles, 'mayINTfiles': mayINTfiles, 'mayallrecords': mayallrecords, 
            'mayEMCVSrecords': mayEMCVSrecords, 'mayINTCVSrecords': mayINTCVSrecords, 'mayEMrecords': mayEMrecords, 'mayEM_WEBrecords': mayEM_WEBrecords, 'mayEM_PRINTrecords': mayEM_PRINTrecords, 'mayINTrecords': mayINTrecords, 
            'mayINT_WEBrecords': mayINT_WEBrecords, 'mayINT_PRINTrecords': mayINT_PRINTrecords,'junEMfiles': junEMfiles, 'junINTfiles': junINTfiles, 'junallrecords': junallrecords, 
            'junEMCVSrecords': junEMCVSrecords, 'junINTCVSrecords': junINTCVSrecords, 'junEMrecords': junEMrecords, 'junEM_WEBrecords': junEM_WEBrecords, 'junEM_PRINTrecords': junEM_PRINTrecords, 'junINTrecords': junINTrecords, 
            'junINT_WEBrecords': junINT_WEBrecords, 'junINT_PRINTrecords': junINT_PRINTrecords, 'julEMfiles': julEMfiles, 'julINTfiles': julINTfiles, 'julallrecords': julallrecords, 
            'julEMCVSrecords': julEMCVSrecords, 'julINTCVSrecords': julINTCVSrecords, 'julEMrecords': julEMrecords, 'julEM_WEBrecords': julEM_WEBrecords, 'julEM_PRINTrecords': julEM_PRINTrecords, 'julINTrecords': julINTrecords, 
            'julINT_WEBrecords': julINT_WEBrecords, 'julINT_PRINTrecords': julINT_PRINTrecords, 'augEMfiles': augEMfiles, 'augINTfiles': augINTfiles, 'augallrecords': augallrecords, 
            'augEMCVSrecords': augEMCVSrecords, 'augINTCVSrecords': augINTCVSrecords, 'augEMrecords': augEMrecords, 'augEM_WEBrecords': augEM_WEBrecords, 'augEM_PRINTrecords': augEM_PRINTrecords, 'augINTrecords': augINTrecords, 
            'augINT_WEBrecords': augINT_WEBrecords, 'augINT_PRINTrecords': augINT_PRINTrecords, 'sepEMfiles': sepEMfiles, 'sepINTfiles': sepINTfiles, 'sepallrecords': sepallrecords, 
            'sepEMCVSrecords': sepEMCVSrecords, 'sepINTCVSrecords': sepINTCVSrecords, 'sepEMrecords': sepEMrecords, 'sepEM_WEBrecords': sepEM_WEBrecords, 'sepEM_PRINTrecords': sepEM_PRINTrecords, 'sepINTrecords': sepINTrecords, 
            'sepINT_WEBrecords': sepINT_WEBrecords, 'sepINT_PRINTrecords': sepINT_PRINTrecords,'octEMfiles': octEMfiles, 'octINTfiles': octINTfiles, 'octallrecords': octallrecords, 
            'octEMCVSrecords': octEMCVSrecords, 'octINTCVSrecords': octINTCVSrecords, 'octEMrecords': octEMrecords, 'octEM_WEBrecords': octEM_WEBrecords, 'octEM_PRINTrecords': octEM_PRINTrecords, 'octINTrecords': octINTrecords, 
            'octINT_WEBrecords': octINT_WEBrecords, 'octINT_PRINTrecords': octINT_PRINTrecords, 'novEMfiles': novEMfiles, 'novINTfiles': novINTfiles, 'novallrecords': novallrecords, 
            'novEMCVSrecords': novEMCVSrecords, 'novINTCVSrecords': novINTCVSrecords, 'novEMrecords': novEMrecords, 'novEM_WEBrecords': novEM_WEBrecords, 'novEM_PRINTrecords': novEM_PRINTrecords, 'novINTrecords': novINTrecords, 
            'novINT_WEBrecords': novINT_WEBrecords, 'novINT_PRINTrecords': novINT_PRINTrecords, 'decEMfiles': decEMfiles, 'decINTfiles': decINTfiles, 'decallrecords': decallrecords, 
            'decEMCVSrecords': decEMCVSrecords, 'decINTCVSrecords': decINTCVSrecords, 'decEMrecords': decEMrecords, 'decEM_WEBrecords': decEM_WEBrecords, 'decEM_PRINTrecords': decEM_PRINTrecords, 'decINTrecords': decINTrecords, 
            'decINT_WEBrecords': decINT_WEBrecords, 'decINT_PRINTrecords': decINT_PRINTrecords })
        return render_to_response(tmp, variables)



    elif len(oplinks) >= 1:

        tmp = "test/analytics.html"
        variables = RequestContext(request, {'form':form, 'oplinks': oplinks, 'cmthEMfiles': cmthEMfiles, 'cmthINTfiles': cmthINTfiles, 'precords': precords, 'classrecords': classrecords, 'cmthallrecords': cmthallrecords, 
            'cmthEMCVSrecords': cmthEMCVSrecords, 'cmthINTCVSrecords': cmthINTCVSrecords, 'cmthEMrecords': cmthEMrecords, 'cmthEM_WEBrecords': cmthEM_WEBrecords, 'cmthEM_PRINTrecords': cmthEM_PRINTrecords, 'cmthINTrecords': cmthINTrecords, 
            'cmthINT_WEBrecords': cmthINT_WEBrecords, 'cmthINT_PRINTrecords': cmthINT_PRINTrecords, 'ytdallrecords': ytdallrecords, 'ytdEMrecords': ytdEMrecords, 'ytdINTrecords': ytdINTrecords, 'ytdEM_WEBrecords': ytdEM_WEBrecords, 
            'ytdEM_PRINTrecords': ytdEM_PRINTrecords, 'ytdINT_WEBrecords': ytdINT_WEBrecords, 'ytdINT_PRINTrecords': ytdINT_PRINTrecords, 'ytdCVSrecords': ytdCVSrecords, 'ytdEMCVSrecords': ytdEMCVSrecords, 'ytdINTCVSrecords': ytdINTCVSrecords, 
            'studioproducts': studioproducts, 'processedproducts': processedproducts, 'vendorproducts': vendorproducts, 'janEMfiles': janEMfiles, 'janINTfiles': janINTfiles, 'janallrecords': janallrecords, 
            'janEMCVSrecords': janEMCVSrecords, 'janINTCVSrecords': janINTCVSrecords, 'janEMrecords': janEMrecords, 'janEM_WEBrecords': janEM_WEBrecords, 'janEM_PRINTrecords': janEM_PRINTrecords, 'janINTrecords': janINTrecords, 
            'janINT_WEBrecords': janINT_WEBrecords, 'janINT_PRINTrecords': janINT_PRINTrecords,'febEMfiles': febEMfiles, 'febINTfiles': febINTfiles, 'feballrecords': feballrecords, 
            'febEMCVSrecords': febEMCVSrecords, 'febINTCVSrecords': febINTCVSrecords, 'febEMrecords': febEMrecords, 'febEM_WEBrecords': febEM_WEBrecords, 'febEM_PRINTrecords': febEM_PRINTrecords, 'febINTrecords': febINTrecords, 
            'febINT_WEBrecords': febINT_WEBrecords, 'febINT_PRINTrecords': febINT_PRINTrecords, 'marEMfiles': marEMfiles, 'marINTfiles': marINTfiles, 'marallrecords': marallrecords, 
            'marEMCVSrecords': marEMCVSrecords, 'marINTCVSrecords': marINTCVSrecords, 'marEMrecords': marEMrecords, 'marEM_WEBrecords': marEM_WEBrecords, 'marEM_PRINTrecords': marEM_PRINTrecords, 'marINTrecords': marINTrecords, 
            'marINT_WEBrecords': marINT_WEBrecords, 'marINT_PRINTrecords': marINT_PRINTrecords, 'aprEMfiles': aprEMfiles, 'aprINTfiles': aprINTfiles, 'aprallrecords': aprallrecords, 
            'aprEMCVSrecords': aprEMCVSrecords, 'aprINTCVSrecords': aprINTCVSrecords, 'aprEMrecords': aprEMrecords, 'aprEM_WEBrecords': aprEM_WEBrecords, 'aprEM_PRINTrecords': aprEM_PRINTrecords, 'aprINTrecords': aprINTrecords, 
            'aprINT_WEBrecords': aprINT_WEBrecords, 'aprINT_PRINTrecords': aprINT_PRINTrecords, 'mayEMfiles': mayEMfiles, 'mayINTfiles': mayINTfiles, 'mayallrecords': mayallrecords, 
            'mayEMCVSrecords': mayEMCVSrecords, 'mayINTCVSrecords': mayINTCVSrecords, 'mayEMrecords': mayEMrecords, 'mayEM_WEBrecords': mayEM_WEBrecords, 'mayEM_PRINTrecords': mayEM_PRINTrecords, 'mayINTrecords': mayINTrecords, 
            'mayINT_WEBrecords': mayINT_WEBrecords, 'mayINT_PRINTrecords': mayINT_PRINTrecords,'junEMfiles': junEMfiles, 'junINTfiles': junINTfiles, 'junallrecords': junallrecords, 
            'junEMCVSrecords': junEMCVSrecords, 'junINTCVSrecords': junINTCVSrecords, 'junEMrecords': junEMrecords, 'junEM_WEBrecords': junEM_WEBrecords, 'junEM_PRINTrecords': junEM_PRINTrecords, 'junINTrecords': junINTrecords, 
            'junINT_WEBrecords': junINT_WEBrecords, 'junINT_PRINTrecords': junINT_PRINTrecords, 'julEMfiles': julEMfiles, 'julINTfiles': julINTfiles, 'julallrecords': julallrecords, 
            'julEMCVSrecords': julEMCVSrecords, 'julINTCVSrecords': julINTCVSrecords, 'julEMrecords': julEMrecords, 'julEM_WEBrecords': julEM_WEBrecords, 'julEM_PRINTrecords': julEM_PRINTrecords, 'julINTrecords': julINTrecords, 
            'julINT_WEBrecords': julINT_WEBrecords, 'julINT_PRINTrecords': julINT_PRINTrecords,'augEMfiles': augEMfiles, 'augINTfiles': augINTfiles, 'augallrecords': augallrecords, 
            'augEMCVSrecords': augEMCVSrecords, 'augINTCVSrecords': augINTCVSrecords, 'augEMrecords': augEMrecords, 'augEM_WEBrecords': augEM_WEBrecords, 'augEM_PRINTrecords': augEM_PRINTrecords, 'augINTrecords': augINTrecords, 
            'augINT_WEBrecords': augINT_WEBrecords, 'augINT_PRINTrecords': augINT_PRINTrecords, 'sepEMfiles': sepEMfiles, 'sepINTfiles': sepINTfiles, 'sepallrecords': sepallrecords, 
            'sepEMCVSrecords': sepEMCVSrecords, 'sepINTCVSrecords': sepINTCVSrecords, 'sepEMrecords': sepEMrecords, 'sepEM_WEBrecords': sepEM_WEBrecords, 'sepEM_PRINTrecords': sepEM_PRINTrecords, 'sepINTrecords': sepINTrecords, 
            'sepINT_WEBrecords': sepINT_WEBrecords, 'sepINT_PRINTrecords': sepINT_PRINTrecords, 'octEMfiles': octEMfiles, 'octINTfiles': octINTfiles, 'octallrecords': octallrecords, 
            'octEMCVSrecords': octEMCVSrecords, 'octINTCVSrecords': octINTCVSrecords, 'octEMrecords': octEMrecords, 'octEM_WEBrecords': octEM_WEBrecords, 'octEM_PRINTrecords': octEM_PRINTrecords, 'octINTrecords': octINTrecords, 
            'octINT_WEBrecords': octINT_WEBrecords, 'octINT_PRINTrecords': octINT_PRINTrecords, 'novEMfiles': novEMfiles, 'novINTfiles': novINTfiles, 'novallrecords': novallrecords, 
            'novEMCVSrecords': novEMCVSrecords, 'novINTCVSrecords': novINTCVSrecords, 'novEMrecords': novEMrecords, 'novEM_WEBrecords': novEM_WEBrecords, 'novEM_PRINTrecords': novEM_PRINTrecords, 'novINTrecords': novINTrecords, 
            'novINT_WEBrecords': novINT_WEBrecords, 'novINT_PRINTrecords': novINT_PRINTrecords,'decEMfiles': decEMfiles, 'decINTfiles': decINTfiles, 'decallrecords': decallrecords, 
            'decEMCVSrecords': decEMCVSrecords, 'decINTCVSrecords': decINTCVSrecords, 'decEMrecords': decEMrecords, 'decEM_WEBrecords': decEM_WEBrecords, 'decEM_PRINTrecords': decEM_PRINTrecords, 'decINTrecords': decINTrecords, 
            'decINT_WEBrecords': decINT_WEBrecords, 'decINT_PRINTrecords': decINT_PRINTrecords  })
        return render_to_response(tmp, variables)

    # elif len(reportlinks) >= 1:
    #     records = Product.objects.filter(Q(first__exact='t') & Q(first_date__istartswith='01') & (Q(desc__icontains="NIKE") | Q(desc__icontains="UA") | Q(desc__icontains="UNDER"))).exclude(ad_date__isnull=False).exclude(confirmed_placed__isnull=True).exclude(confirmed_placed='').exclude(studio_out__isnull=False)
    #     workrecords = Product.objects.filter(Q(ad_date__istartswith='01') & (Q(received_other__isnull=False) | Q(first__iexact='t')))
    #     default_dict = {'user': user, 'myrecords': myrecords, 'boxrecords': boxrecords, 'records': records, 'watchrecords': watchrecords, 'allwatchrecords': allwatchrecords, 'workrecords': workrecords, 'cgrecords': cgrecords, 'tmrecords': tmrecords, 'form': form}
    #     z = default_dict.copy()
    #     z.update(boxdict)
    #     return render_to_response('list_template.html', z, context_instance=RequestContext(request))


    else:
        form = PostsearchForm()
        tmp = "test/analytics.html"
        variables = RequestContext(request, {'form':form, 'cmthEMfiles': cmthEMfiles, 'cmthINTfiles': cmthINTfiles, 'precords': precords, 'classrecords': classrecords, 'cmthallrecords': cmthallrecords, 
            'cmthEMCVSrecords': cmthEMCVSrecords, 'cmthINTCVSrecords': cmthINTCVSrecords, 'cmthEMrecords': cmthEMrecords, 'cmthEM_WEBrecords': cmthEM_WEBrecords, 'cmthEM_PRINTrecords': cmthEM_PRINTrecords, 'cmthINTrecords': cmthINTrecords, 
            'cmthINT_WEBrecords': cmthINT_WEBrecords, 'cmthINT_PRINTrecords': cmthINT_PRINTrecords, 'ytdallrecords': ytdallrecords, 'ytdEMrecords': ytdEMrecords, 'ytdINTrecords': ytdINTrecords, 'ytdEM_WEBrecords': ytdEM_WEBrecords, 
            'ytdEM_PRINTrecords': ytdEM_PRINTrecords, 'ytdINT_WEBrecords': ytdINT_WEBrecords, 'ytdINT_PRINTrecords': ytdINT_PRINTrecords, 'ytdCVSrecords': ytdCVSrecords, 'ytdEMCVSrecords': ytdEMCVSrecords, 'ytdINTCVSrecords': ytdINTCVSrecords, 
            'studioproducts': studioproducts, 'processedproducts': processedproducts, 'vendorproducts': vendorproducts, 'janEMfiles': janEMfiles, 'janINTfiles': janINTfiles, 'janallrecords': janallrecords, 
            'janEMCVSrecords': janEMCVSrecords, 'janINTCVSrecords': janINTCVSrecords, 'janEMrecords': janEMrecords, 'janEM_WEBrecords': janEM_WEBrecords, 'janEM_PRINTrecords': janEM_PRINTrecords, 'janINTrecords': janINTrecords, 
            'janINT_WEBrecords': janINT_WEBrecords, 'janINT_PRINTrecords': janINT_PRINTrecords,'febEMfiles': febEMfiles, 'febINTfiles': febINTfiles, 'feballrecords': feballrecords, 
            'febEMCVSrecords': febEMCVSrecords, 'febINTCVSrecords': febINTCVSrecords, 'febEMrecords': febEMrecords, 'febEM_WEBrecords': febEM_WEBrecords, 'febEM_PRINTrecords': febEM_PRINTrecords, 'febINTrecords': febINTrecords, 
            'febINT_WEBrecords': febINT_WEBrecords, 'febINT_PRINTrecords': febINT_PRINTrecords, 'marEMfiles': marEMfiles, 'marINTfiles': marINTfiles, 'marallrecords': marallrecords, 
            'marEMCVSrecords': marEMCVSrecords, 'marINTCVSrecords': marINTCVSrecords, 'marEMrecords': marEMrecords, 'marEM_WEBrecords': marEM_WEBrecords, 'marEM_PRINTrecords': marEM_PRINTrecords, 'marINTrecords': marINTrecords, 
            'marINT_WEBrecords': marINT_WEBrecords, 'marINT_PRINTrecords': marINT_PRINTrecords, 'aprEMfiles': aprEMfiles, 'aprINTfiles': aprINTfiles, 'aprallrecords': aprallrecords, 
            'aprEMCVSrecords': aprEMCVSrecords, 'aprINTCVSrecords': aprINTCVSrecords, 'aprEMrecords': aprEMrecords, 'aprEM_WEBrecords': aprEM_WEBrecords, 'aprEM_PRINTrecords': aprEM_PRINTrecords, 'aprINTrecords': aprINTrecords, 
            'aprINT_WEBrecords': aprINT_WEBrecords, 'aprINT_PRINTrecords': aprINT_PRINTrecords, 'mayEMfiles': mayEMfiles, 'mayINTfiles': mayINTfiles, 'mayallrecords': mayallrecords, 
            'mayEMCVSrecords': mayEMCVSrecords, 'mayINTCVSrecords': mayINTCVSrecords, 'mayEMrecords': mayEMrecords, 'mayEM_WEBrecords': mayEM_WEBrecords, 'mayEM_PRINTrecords': mayEM_PRINTrecords, 'mayINTrecords': mayINTrecords, 
            'mayINT_WEBrecords': mayINT_WEBrecords, 'mayINT_PRINTrecords': mayINT_PRINTrecords,'junEMfiles': junEMfiles, 'junINTfiles': junINTfiles, 'junallrecords': junallrecords, 
            'junEMCVSrecords': junEMCVSrecords, 'junINTCVSrecords': junINTCVSrecords, 'junEMrecords': junEMrecords, 'junEM_WEBrecords': junEM_WEBrecords, 'junEM_PRINTrecords': junEM_PRINTrecords, 'junINTrecords': junINTrecords, 
            'junINT_WEBrecords': junINT_WEBrecords, 'junINT_PRINTrecords': junINT_PRINTrecords, 'julEMfiles': julEMfiles, 'julINTfiles': julINTfiles, 'julallrecords': julallrecords, 
            'julEMCVSrecords': julEMCVSrecords, 'julINTCVSrecords': julINTCVSrecords, 'julEMrecords': julEMrecords, 'julEM_WEBrecords': julEM_WEBrecords, 'julEM_PRINTrecords': julEM_PRINTrecords, 'julINTrecords': julINTrecords, 
            'julINT_WEBrecords': julINT_WEBrecords, 'julINT_PRINTrecords': julINT_PRINTrecords,'augEMfiles': augEMfiles, 'augINTfiles': augINTfiles, 'augallrecords': augallrecords, 
            'augEMCVSrecords': augEMCVSrecords, 'augINTCVSrecords': augINTCVSrecords, 'augEMrecords': augEMrecords, 'augEM_WEBrecords': augEM_WEBrecords, 'augEM_PRINTrecords': augEM_PRINTrecords, 'augINTrecords': augINTrecords, 
            'augINT_WEBrecords': augINT_WEBrecords, 'augINT_PRINTrecords': augINT_PRINTrecords, 'sepEMfiles': sepEMfiles, 'sepINTfiles': sepINTfiles, 'sepallrecords': sepallrecords, 
            'sepEMCVSrecords': sepEMCVSrecords, 'sepINTCVSrecords': sepINTCVSrecords, 'sepEMrecords': sepEMrecords, 'sepEM_WEBrecords': sepEM_WEBrecords, 'sepEM_PRINTrecords': sepEM_PRINTrecords, 'sepINTrecords': sepINTrecords, 
            'sepINT_WEBrecords': sepINT_WEBrecords, 'sepINT_PRINTrecords': sepINT_PRINTrecords, 'octEMfiles': octEMfiles, 'octINTfiles': octINTfiles, 'octallrecords': octallrecords, 
            'octEMCVSrecords': octEMCVSrecords, 'octINTCVSrecords': octINTCVSrecords, 'octEMrecords': octEMrecords, 'octEM_WEBrecords': octEM_WEBrecords, 'octEM_PRINTrecords': octEM_PRINTrecords, 'octINTrecords': octINTrecords, 
            'octINT_WEBrecords': octINT_WEBrecords, 'octINT_PRINTrecords': octINT_PRINTrecords, 'novEMfiles': novEMfiles, 'novINTfiles': novINTfiles, 'novallrecords': novallrecords, 
            'novEMCVSrecords': novEMCVSrecords, 'novINTCVSrecords': novINTCVSrecords, 'novEMrecords': novEMrecords, 'novEM_WEBrecords': novEM_WEBrecords, 'novEM_PRINTrecords': novEM_PRINTrecords, 'novINTrecords': novINTrecords, 
            'novINT_WEBrecords': novINT_WEBrecords, 'novINT_PRINTrecords': novINT_PRINTrecords,'decEMfiles': decEMfiles, 'decINTfiles': decINTfiles, 'decallrecords': decallrecords, 
            'decEMCVSrecords': decEMCVSrecords, 'decINTCVSrecords': decINTCVSrecords, 'decEMrecords': decEMrecords, 'decEM_WEBrecords': decEM_WEBrecords, 'decEM_PRINTrecords': decEM_PRINTrecords, 'decINTrecords': decINTrecords, 
            'decINT_WEBrecords': decINT_WEBrecords, 'decINT_PRINTrecords': decINT_PRINTrecords, 'countrecords': countrecords, 'junintrecords': junintrecords })
        return render_to_response(tmp, variables)
