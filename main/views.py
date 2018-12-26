from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.contrib.auth import login, authenticate
from django.contrib.auth.models import User
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from .forms import PostForm, LoginForm, SentenceForm, SoreForm, wishbookForm, ReplyForm, PeterCatForm
from .models import *
from django.contrib import messages 
from django.shortcuts import redirect
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import authentication, permissions
from datetime import timedelta

import datetime
import time
import random
import urllib.request
import os
import sys
import json

# index page loading.

def petercatRester(request):
    now = time.localtime()
    nowDateTime = "%04d-%02d-%02d %02d:%02d:%02d" % (now.tm_year, now.tm_mon, now.tm_mday, now.tm_hour, now.tm_min, now.tm_sec)
    makePkDateTime = "%04d%02d%02d%02d%02d%02d" % (now.tm_year, now.tm_mon, now.tm_mday, now.tm_hour, now.tm_min, now.tm_sec)
    if request.method == "POST":
        form = PeterCatForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.created = nowDateTime
            post.register = request.session['member_id']
            post.senId = str(request.session['member_id'])+str(makePkDateTime)+str(random.randrange(1,100))
            post.save()
            return redirect('../')
    else:
        return redirect("/")
def petercat(request):
    form = PeterCatForm()
    context = {'form': form, }
    return render(request, 'main/petercat.html', context)

def index(request):
    petercatSenten = petercatSentence.objects.all()
    context = {'petercatSenten':petercatSenten}
    return render(request, 'main/index.html', context)


def senChange(request):

    senId = request.GET.get('senId')
    print(senId)
    print(request.POST.get('senId'))
    now = time.localtime()
    nowDateTime = "%04d-%02d-%02d %02d:%02d:%02d" % (now.tm_year, now.tm_mon, now.tm_mday, now.tm_hour, now.tm_min, now.tm_sec)
    makePkDateTime = "%04d%02d%02d%02d%02d%02d" % (now.tm_year, now.tm_mon, now.tm_mday, now.tm_hour, now.tm_min, now.tm_sec)
    if request.method == "POST":
        form = PeterCatForm(request.POST)
        reading_instance = petercatSentence.objects.get(senId=request.POST.get('senId'))
        reading_instance.created = nowDateTime
        reading_instance.register = request.session['member_id']
        reading_instance.senId = request.POST.get('senId')
        reading_instance.bookName = request.POST.get('bookName')
        reading_instance.senContent = request.POST.get('senContent')
        reading_instance.senWriter = request.POST.get('senWriter')
        reading_instance.save()
        return redirect('../')
    else:
        reading = petercatSentence.objects.filter(senId=senId)
        print(reading[0].senContent)
        form = PeterCatForm(initial={'senContent': reading[0].senContent, 'bookName':reading[0].bookName,  'senWriter':reading[0].senWriter,
        'senId': reading[0].senId})
    context = {'form': form, 'senId':senId}
    return render(request, 'main/petercat.html', context)

def getDayName(year, month, day):
	return ['0','1','2','3','4','5','6'][datetime.date(year, month, day).weekday()]

def petercatmenu(request):
    pc = petercatMenu(menuId='1',korname='에스프레소',engname=' Espresso',zhname=' Espresso',price='4500',useYn='Y',specialgubun='C',category='COFFEE')
    pc.save()
    pc = petercatMenu(menuId='2',korname='아메리카노',engname=' Americano',zhname=' Americano',price='4500',useYn='Y',specialgubun='C',category='COFFEE')
    pc.save()
    pc = petercatMenu(menuId='3',korname='아메리카노 리스트레토',engname=' Americano Ristretto',zhname=' Americano Ristretto',price='4500',useYn='Y',specialgubun='C',category='COFFEE')
    pc.save()
    pc = petercatMenu(menuId='4',korname='더치 아메리카노',engname=' Cold Brew',zhname=' Cold Brew',price='5000',useYn='Y',specialgubun='C',category='COFFEE')
    pc.save()
    pc = petercatMenu(menuId='5',korname='더치 라떼',engname=' Cold Brew Latte',zhname=' Cold Brew Latte',price='5500',useYn='Y',specialgubun='C',category='COFFEE')
    pc.save()
    pc = petercatMenu(menuId='6',korname='핸드드립',engname=' Hand Drip',zhname=' Hand Drip',price='6000',useYn='Y',specialgubun='C',category='COFFEE')
    pc.save()
    pc = petercatMenu(menuId='7',korname='카페라떼',engname=' Café Latte',zhname=' Café Latte',price='5000',useYn='Y',specialgubun='C',category='COFFEE')
    pc.save()
    pc = petercatMenu(menuId='8',korname='카푸치노',engname=' Cappuccino',zhname=' Cappuccino',price='5000',useYn='Y',specialgubun='C',category='COFFEE')
    pc.save()
    pc = petercatMenu(menuId='9',korname='카페모카',engname=' Café Mocha',zhname=' Café Mocha',price='5500',useYn='Y',specialgubun='C',category='COFFEE')
    pc.save()
    pc = petercatMenu(menuId='10',korname='카라멜 마키아토',engname=' Caramel Macchiato',zhname=' Caramel Macchiato',price='5500',useYn='Y',specialgubun='C',category='COFFEE')
    pc.save()
    pc = petercatMenu(menuId='11',korname='바닐라 라떼',engname=' Vanilla Latte',zhname=' Vanilla Latte',price='5500',useYn='Y',specialgubun='C',category='COFFEE')
    pc.save()
    pc = petercatMenu(menuId='12',korname='헤이즐넛 라떼',engname=' Hazelnut Latte',zhname=' Hazelnut Latte',price='5500',useYn='Y',specialgubun='C',category='COFFEE')
    pc.save()
    pc = petercatMenu(menuId='13',korname='원두 100g',engname='',zhname='',price='7000',useYn='Y',specialgubun='C',category='COFFEE')
    pc.save()
    pc = petercatMenu(menuId='14',korname='얼그레이 티',engname=' Earl Grey Tea',zhname=' Earl Grey Tea',price='5000',useYn='Y',specialgubun='C',category='BEVERGE')
    pc.save()
    pc = petercatMenu(menuId='15',korname='카모마일 티',engname=' Chamomile Tea',zhname=' Chamomile Tea',price='5000',useYn='Y',specialgubun='C',category='BEVERGE')
    pc.save()
    pc = petercatMenu(menuId='16',korname='페퍼민트 티',engname=' Peppermint Tea',zhname=' Peppermint Tea',price='5000',useYn='Y',specialgubun='C',category='BEVERGE')
    pc.save()
    pc = petercatMenu(menuId='17',korname='애플 리프레시 티',engname=' Apple Refresh Tea',zhname=' Apple Refresh Tea',price='5000',useYn='Y',specialgubun='C',category='BEVERGE')
    pc.save()
    pc = petercatMenu(menuId='18',korname='와일드 스트로베리 티',engname=' Wild Strawberry Tea',zhname=' Wild Strawberry Tea',price='5000',useYn='Y',specialgubun='C',category='BEVERGE')
    pc.save()
    pc = petercatMenu(menuId='19',korname='밀크티 라떼',engname=' Milk Tea Latte',zhname=' Milk Tea Latte',price='5500',useYn='Y',specialgubun='C',category='BEVERGE')
    pc.save()
    pc = petercatMenu(menuId='20',korname='레몬티',engname=' Lemon Tea',zhname=' Lemon Tea',price='5000',useYn='Y',specialgubun='C',category='BEVERGE')
    pc.save()
    pc = petercatMenu(menuId='21',korname='자몽티',engname=' Grapefruit Tea',zhname=' Grapefruit Tea',price='5000',useYn='Y',specialgubun='C',category='BEVERGE')
    pc.save()
    pc = petercatMenu(menuId='22',korname='진저티',engname=' Ginger Tea',zhname=' Ginger Tea',price='5000',useYn='Y',specialgubun='C',category='BEVERGE')
    pc.save()
    pc = petercatMenu(menuId='23',korname='진저라떼',engname=' Ginger Latte',zhname=' Ginger Latte',price='5500',useYn='Y',specialgubun='C',category='BEVERGE')
    pc.save()
    pc = petercatMenu(menuId='24',korname='그린티라떼',engname=' Green Tea Latte',zhname=' Green Tea Latte',price='5000',useYn='Y',specialgubun='C',category='BEVERGE')
    pc.save()
    pc = petercatMenu(menuId='25',korname='초코라떼',engname=' Chocolate Latte',zhname=' Chocolate Latte',price='5000',useYn='Y',specialgubun='C',category='BEVERGE')
    pc.save()
    pc = petercatMenu(menuId='26',korname='레몬에이드',engname=' Lemon Ade',zhname=' Lemon Ade',price='5500',useYn='Y',specialgubun='C',category='BEVERGE')
    pc.save()
    pc = petercatMenu(menuId='27',korname='자몽에이드',engname=' Grapefruit Ade',zhname=' Grapefruit Ade',price='5500',useYn='Y',specialgubun='C',category='BEVERGE')
    pc.save()
    pc = petercatMenu(menuId='28',korname='진저에이드',engname=' Ginger Ade',zhname=' Ginger Ade',price='6000',useYn='Y',specialgubun='C',category='BEVERGE')
    pc.save()
    pc = petercatMenu(menuId='29',korname='애플주스 (탄산,무탄산)',engname=' Apple Juice',zhname=' Apple Juice',price='4500',useYn='Y',specialgubun='C',category='BEVERGE')
    pc.save()
    pc = petercatMenu(menuId='30',korname='커티삭 온더록스',engname=' Cutty Sark On The Rocks',zhname=' Cutty Sark On The Rocks',price='6000',useYn='Y',specialgubun='C',category='COCKTAIL')
    pc.save()
    pc = petercatMenu(menuId='31',korname='진저 하이볼',engname=' Ginger Highball',zhname=' Ginger Highball',price='7000',useYn='Y',specialgubun='C',category='COCKTAIL')
    pc.save()
    pc = petercatMenu(menuId='32',korname='커티삭 하이볼',engname=' Cutty Sark Highball (1Q84)',zhname=' Cutty Sark Highball (1Q84)',price='7000',useYn='Y',specialgubun='C',category='COCKTAIL')
    pc.save()
    pc = petercatMenu(menuId='33',korname='진토닉',engname=' Gin and Tonic ',zhname=' Gin and Tonic ',price='7000',useYn='Y',specialgubun='C',category='COCKTAIL')
    pc.save()
    pc = petercatMenu(menuId='34',korname='보드카 토닉',engname=' Vodca Tonic (노르웨이의 숲)',zhname=' Vodca Tonic (노르웨이의 숲)',price='7000',useYn='Y',specialgubun='C',category='COCKTAIL')
    pc.save()
    pc = petercatMenu(menuId='35',korname='와인에이드',engname=' Wine Ade (그러나 즐겁게 살고 싶다)',zhname=' Wine Ade (그러나 즐겁게 살고 싶다)',price='7000',useYn='Y',specialgubun='C',category='COCKTAIL')
    pc.save()
    pc = petercatMenu(menuId='36',korname='깔루아 밀크',engname=' Kahlua Milk',zhname=' Kahlua Milk',price='7000',useYn='Y',specialgubun='C',category='COCKTAIL')
    pc.save()
    pc = petercatMenu(menuId='37',korname='깔루아 스파클링',engname=' Kahlua Sparkling',zhname=' Kahlua Sparkling',price='7000',useYn='Y',specialgubun='C',category='COCKTAIL')
    pc.save()
    pc = petercatMenu(menuId='38',korname='베일리스 밀크',engname=' Baileys Milk',zhname=' Baileys Milk',price='7000',useYn='Y',specialgubun='C',category='COCKTAIL')
    pc.save()
    pc = petercatMenu(menuId='39',korname='블랙 러시안',engname=' Black Russian',zhname=' Black Russian',price='8000',useYn='Y',specialgubun='C',category='COCKTAIL')
    pc.save()
    pc = petercatMenu(menuId='40',korname='자몽 보드카 펀치',engname=' Grapefruit Vodka Punch',zhname=' Grapefruit Vodka Punch',price='8000',useYn='Y',specialgubun='C',category='COCKTAIL')
    pc.save()
    pc = petercatMenu(menuId='41',korname='클라우드',engname=' Kloud Beer',zhname=' Kloud Beer',price='6000',useYn='Y',specialgubun='C',category='COCKTAIL')
    pc.save()
    pc = petercatMenu(menuId='42',korname='플레인 치즈케익',engname=' Plain Cheese Cake',zhname=' Plain Cheese Cake',price='4500',useYn='Y',specialgubun='C',category='SIDE MENU')
    pc.save()
    pc = petercatMenu(menuId='43',korname='스콘 (딸기잼)',engname=' Scone',zhname=' Scone',price='3000',useYn='Y',specialgubun='C',category='SIDE MENU')
    pc.save()
    pc = petercatMenu(menuId='44',korname='초코머핀',engname=' Chocolate Muffin',zhname=' Chocolate Muffin',price='3000',useYn='Y',specialgubun='C',category='SIDE MENU')
    pc.save()
    pc = petercatMenu(menuId='45',korname='블루베리 머핀',engname=' Blueberry Muffin',zhname=' Blueberry Muffin',price='3000',useYn='Y',specialgubun='C',category='SIDE MENU')
    pc.save()
    pc = petercatMenu(menuId='46',korname='쿠키',engname=' Cookie',zhname=' Cookie',price='3000',useYn='Y',specialgubun='C',category='SIDE MENU')
    pc.save()
    pc = petercatMenu(menuId='47',korname='감자튀김',engname=' Fried potato',zhname=' Fried potato',price='3000',useYn='Y',specialgubun='C',category='SIDE MENU')
    pc.save()
    pc = petercatMenu(menuId='48',korname='나쵸',engname=' Nacho',zhname=' Nacho',price='3000',useYn='Y',specialgubun='C',category='SIDE MENU')
    pc.save()
    pc = petercatMenu(menuId='49',korname='베이글 크림치즈',engname=' Bagel with Cream Cheese',zhname=' Bagel with Cream Cheese',price='4000',useYn='Y',specialgubun='C',category='SIDE MENU')
    pc.save()
    pc = petercatMenu(menuId='50',korname='크로크무슈',engname=' Croque-monsieur',zhname=' Croque-monsieur',price='5000',useYn='Y',specialgubun='C',category='SIDE MENU')
    pc.save()

    coffeeMenu = petercatMenu.objects.filter(category='COFFEE', useYn='Y')
    cocktailMenu = petercatMenu.objects.filter(category='COCKTAIL', useYn='Y')
    sideMenu = petercatMenu.objects.filter(category='SIDE MENU', useYn='Y')
    beverageMenu = petercatMenu.objects.filter(category='BEVERGE', useYn='Y')
    now = time.localtime()
    strweek = getDayName(now.tm_year, now.tm_mon, now.tm_mday)
    nowday = datetime.date(now.tm_year, now.tm_mon, now.tm_mday)
    startday = nowday + timedelta(days=-int(strweek))
    endday = nowday + timedelta(days=(6-int(strweek)))
    print(startday, endday)

    weekbooks = petercatBook.objects.filter(meeingdate__range=[str(startday), str(endday)]).order_by('meeingtime')
    context = {'coffeeMenu': coffeeMenu, 'cocktailMenu': cocktailMenu,
     'beverageMenu': beverageMenu, 'sideMenu': sideMenu, 'weekbooks':weekbooks}
    return render(request, 'main/petercatMenu.html', context)



def nowbooksendelete(request):
    senten = sentence.objects.get(senId=request.GET.get('senId'))
    senten.delete()
    return redirect("/nowbook/")

def nowbookscoredelete(request):
    star = starScore.objects.get(scoreId=request.GET.get('scoreId'))
    star.delete()
    return redirect("/nowbook/")

def nowbooksendeletefordetail(request):
    senten = sentence.objects.get(senId=request.GET.get('senId'))
    senten.delete()
    return redirect('../bookDetail?bookId='+str(request.GET.get('bookId')))

def nowbookscoredeletefordetail(request):
    star = starScore.objects.get(scoreId=request.GET.get('scoreId'))
    star.delete()
    return redirect('../bookDetail?bookId='+str(request.GET.get('bookId')))

def scoreregist(request):
    now = time.localtime()
    nowDateTime = "%04d-%02d-%02d %02d:%02d:%02d" % (now.tm_year, now.tm_mon, now.tm_mday, now.tm_hour, now.tm_min, now.tm_sec)
    makePkDateTime = "%04d%02d%02d%02d%02d%02d" % (now.tm_year, now.tm_mon, now.tm_mday, now.tm_hour, now.tm_min, now.tm_sec)
    if request.method == "POST":
        form = SoreForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.created = nowDateTime
            post.scoreWriter = request.session['member_id']
            post.scoreId = str(request.session['member_id'])+str(makePkDateTime)+str(random.randrange(1,100))
            post.save()
            return redirect('../nowbook/')
    else:
        return redirect("/nowbook/")

def scoreregistfordetail(request):
    now = time.localtime()
    nowDateTime = "%04d-%02d-%02d %02d:%02d:%02d" % (now.tm_year, now.tm_mon, now.tm_mday, now.tm_hour, now.tm_min, now.tm_sec)
    makePkDateTime = "%04d%02d%02d%02d%02d%02d" % (now.tm_year, now.tm_mon, now.tm_mday, now.tm_hour, now.tm_min, now.tm_sec)
    if request.method == "POST":
        form = SoreForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.created = nowDateTime
            post.scoreWriter = request.session['member_id']
            post.scoreId = str(request.session['member_id'])+str(makePkDateTime)+str(random.randrange(1,100))
            post.save()
            return redirect('../bookDetail?bookId='+str(request.POST.get('bookId')))
    else:
        return redirect("/book/")


def nowbookCall(request):
    nowbook = Ourbooks.objects.filter(statusflag='C')
    senten = sentence.objects.filter(bookId=nowbook[0].bookId)
    star = starScore.objects.filter(bookId=nowbook[0].bookId)
    for starindi in star:
        starindi.scoreDuble = int(float(starindi.scoreStar)*2)
    now = time.localtime()
    nowDateTime = "%04d-%02d-%02d %02d:%02d:%02d" % (now.tm_year, now.tm_mon, now.tm_mday, now.tm_hour, now.tm_min, now.tm_sec)
    makePkDateTime = "%04d%02d%02d%02d%02d%02d" % (now.tm_year, now.tm_mon, now.tm_mday, now.tm_hour, now.tm_min, now.tm_sec)
    if request.method == "POST":
        form = SentenceForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.created = nowDateTime
            post.senWriter = request.session['member_id']
            post.senId = str(request.session['member_id'])+str(makePkDateTime)+str(random.randrange(1,100))
            post.save()
            return redirect('../nowbook/')
        
    else:
        form = SentenceForm()
        starForm = SoreForm()
    context = {'nowbook':nowbook, 'form': form, 'star':star, 'sentence':senten, 'starForm':starForm}
    return render(request, 'main/nowbook.html', context)

def nextbook(request):
    now = time.localtime()
    nowDateTime = "%04d-%02d-%02d %02d:%02d:%02d" % (now.tm_year, now.tm_mon, now.tm_mday, now.tm_hour, now.tm_min, now.tm_sec)
    makePkDateTime = "%04d%02d%02d%02d%02d%02d" % (now.tm_year, now.tm_mon, now.tm_mday, now.tm_hour, now.tm_min, now.tm_sec)
    if request.method == "POST":
        form = wishbookForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.created = nowDateTime
            post.wishId = str(request.session['member_id'])+str(makePkDateTime)+str(random.randrange(1,100))
            post.ourbookflag = 'F'
            post.register = request.session['member_id']
            post.save()
            return redirect('../wishlist/')
        else:
            print(messages.error(request, "Error"))
    else:
        form = None
        
    context = {'form': form}
    return render(request, 'main/nextbook.html', context)


# bookmain page loading.
def bookpage(request):
    
    cateName = category.objects.all().order_by('categoryCode')
    
    filterName = request.GET.get('kindName')

    if filterName is None or str(filterName) =='' or str(filterName) =='None':
        ourbook = Ourbooks.objects.filter(statusflag='R').order_by('-readingdate')
    else:
        ourbook = Ourbooks.objects.filter(category=filterName, statusflag='R').order_by('-readingdate')

    PAGE_ROW_COUNT = 16
    PAGE_DISPLAY_COUNT = 5

    if len(ourbook) == 0 : noresult = None
    else : noresult = 'exist'

    for book in ourbook:
        book.imgindex = book.bookId[-3:]
    
    paginator=Paginator(ourbook, PAGE_ROW_COUNT)
    pageNum=request.GET.get('pageNum')
    
    totalPageCount=paginator.num_pages # 전체 페이지 갯수 
    
    try:
        ourbook=paginator.page(pageNum)
    except PageNotAnInteger:
        ourbook=paginator.page(1)
        pageNum=1
    except EmptyPage:
        member_list=paginator.page(paginator.num_pages)
        pageNum=paginator.num_pages
        
    pageNum=int(pageNum)
    
    startPageNum=1+((pageNum-1)/PAGE_DISPLAY_COUNT)*PAGE_DISPLAY_COUNT
    endPageNum=startPageNum+PAGE_DISPLAY_COUNT-1
    if totalPageCount < endPageNum:
        endPageNum=totalPageCount
        
    bottomPages=range(int(startPageNum), int(endPageNum)+1)

    return render(request, 'main/bookmain.html', 
            {
            'ourbooks':ourbook,
            'category':cateName,
            'pageNum':pageNum,
            'bottomPages':bottomPages,
            'totalPageCount':totalPageCount,
            'startPageNum':startPageNum,
            'endPageNum':endPageNum,
            'filterName':filterName,
            'noresult':noresult
            }
            )

# bookDetail page loading.
def bookDetail(request):
    now = time.localtime()
    nowDateTime = "%04d-%02d-%02d %02d:%02d:%02d" % (now.tm_year, now.tm_mon, now.tm_mday, now.tm_hour, now.tm_min, now.tm_sec)
    makePkDateTime = "%04d%02d%02d%02d%02d%02d" % (now.tm_year, now.tm_mon, now.tm_mday, now.tm_hour, now.tm_min, now.tm_sec)
    if request.method == "POST":
        form = SentenceForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.created = nowDateTime
            post.senWriter = request.session['member_id']
            post.senId = str(request.session['member_id'])+str(makePkDateTime)+str(random.randrange(1,100))
            post.save()
            return redirect('../bookDetail?bookId='+str(request.POST.get('bookId')))
        
    else:
        form = SentenceForm()
        starForm = SoreForm()
        filterName = request.GET.get('bookId')
        ourbook = Ourbooks.objects.filter(bookId=filterName)
    
        senten = sentence.objects.filter(bookId=ourbook[0].bookId)
        star = starScore.objects.filter(bookId=ourbook[0].bookId)

        indiaverStar=0
        averStar = 0
        totalCnt = len(star)
        for starindi in star:
            indiaverStar = indiaverStar + float(starindi.scoreStar)
            starindi.scoreDuble = int(float(starindi.scoreStar)*2)
        if indiaverStar != 0:
            averStar = indiaverStar / totalCnt
            averStar = round(averStar,1)

        for book in ourbook:
            book.imgindex = book.bookId[-3:]

        context = {'ourbook':ourbook, 'form': form, 'star':star, 'sentence':senten, 
        'starForm':starForm, 'averStar':averStar, 'totalCnt':totalCnt}
        return render(request, 'main/bookdetail.html', context)



# readinglist page loading.
def readinglist(request):
    reading = Reading.objects.all().order_by('-created')
    replycount = {}
    for read in reading:
        replycount[read.readId] = len( readingReplys.objects.filter(readId=read.readId) )
    context = {'reading':reading, 'replycount':replycount}
    return render(request, 'main/readinglist.html', context)

def readingdetail(request):
    now = time.localtime()
    nowDateTime = "%04d-%02d-%02d %02d:%02d:%02d" % (now.tm_year, now.tm_mon, now.tm_mday, now.tm_hour, now.tm_min, now.tm_sec)
    makePkDateTime = "%04d%02d%02d%02d%02d%02d" % (now.tm_year, now.tm_mon, now.tm_mday, now.tm_hour, now.tm_min, now.tm_sec)    
    filterName = request.GET.get('readId')
    reading = Reading.objects.select_related('bookId').filter(readId=filterName)
    readingReply = readingReplys.objects.filter(readId=filterName)

    if request.method == "POST":
        form = ReplyForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.created = nowDateTime
            post.replyWriter = request.session['member_id']
            post.replyId = 'reply_'+str(request.session['member_id'])+str(makePkDateTime)+str(random.randrange(1,100))
            post.save()
            return redirect('../readingdetail?readId='+str(request.POST.dict()['readId']))
    else:
        form = ReplyForm()    
    
    context = {'reading':reading, 'readingReply':readingReply, 'form':form}
    return render(request, 'main/readingdetail.html', context)

def replydelete(request):
    readingReply = readingReplys.objects.get(replyId=request.GET.get('replyId'))
    readingReply.delete()
    return redirect('../readingdetail?readId='+request.GET.get('readId'))



# readingwrite page loading.
def readingWirte(request):

    now = time.localtime()
    nowDateTime = "%04d-%02d-%02d %02d:%02d:%02d" % (now.tm_year, now.tm_mon, now.tm_mday, now.tm_hour, now.tm_min, now.tm_sec)
    makePkDateTime = "%04d%02d%02d%02d%02d%02d" % (now.tm_year, now.tm_mon, now.tm_mday, now.tm_hour, now.tm_min, now.tm_sec)
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.created = nowDateTime
            post.writer = request.session['member_id']
            post.save()
            return redirect('../readingdetail?readId='+post.readId)
    else:
        form = PostForm()
        
    context = {'form': form}
    return render(request, 'main/readingwrite.html', context)

def readingChange(request):

    readId = request.GET.get('readId')
    now = time.localtime()
    nowDateTime = "%04d-%02d-%02d %02d:%02d:%02d" % (now.tm_year, now.tm_mon, now.tm_mday, now.tm_hour, now.tm_min, now.tm_sec)
    makePkDateTime = "%04d%02d%02d%02d%02d%02d" % (now.tm_year, now.tm_mon, now.tm_mday, now.tm_hour, now.tm_min, now.tm_sec)
    if request.method == "POST":
        form = PostForm(request.POST)
        filterReadId = request.POST.get('bookId')
        reading_instance = Reading.objects.get(readId=request.POST.get('readId'))
        reading_instance.created = nowDateTime
        reading_instance.writer = request.session['member_id']
        reading_instance.readId = request.POST.get('readId')
        reading_instance.title = request.POST.get('title')
        reading_instance.content = request.POST.get('content')
        reading_instance.bookId.bookId = request.POST.get('bookId')
        reading_instance.save()
        return redirect('../readingdetail?readId='+request.POST.get('readId'))
    else:
        reading = Reading.objects.select_related('bookId').filter(readId=readId)
        form = PostForm(initial={'content': reading[0].content, 'title':reading[0].title,  'bookId':reading[0].bookId})
    context = {'form': form, 'readId':readId}
    return render(request, 'main/readingwrite.html', context)


def meetingmain(request):
    meeting = Meeting.objects.all().order_by('-meetingdate')
    PAGE_ROW_COUNT = 3
    PAGE_DISPLAY_COUNT = 5
    
    
    paginator=Paginator(meeting, PAGE_ROW_COUNT)
    pageNum=request.GET.get('pageNum')
    
    totalPageCount=paginator.num_pages # 전체 페이지 갯수 
    
    try:
        meeting=paginator.page(pageNum)
    except PageNotAnInteger:
        meeting=paginator.page(1)
        pageNum=1
    except EmptyPage:
        member_list=paginator.page(paginator.num_pages)
        pageNum=paginator.num_pages
        
    pageNum=int(pageNum)
    
    startPageNum=1+((pageNum-1)/PAGE_DISPLAY_COUNT)*PAGE_DISPLAY_COUNT
    endPageNum=startPageNum+PAGE_DISPLAY_COUNT-1
    if totalPageCount < endPageNum:
        endPageNum=totalPageCount
        
    bottomPages=range(int(startPageNum), int(endPageNum)+1)

    return render(request, 'main/meetingmain.html', 
            {
            'meeting':meeting,
            'pageNum':pageNum,
            'bottomPages':bottomPages,
            'totalPageCount':totalPageCount,
            'startPageNum':startPageNum,
            'endPageNum':endPageNum
            }
            )


def signin(request):
    if request.method == "POST":
        form = LoginForm(request.POST)
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username = username, password = password)
        if user is not None:
            login(request, user)
            request.session['member_id'] = username
            return redirect('/')
        else:
            return HttpResponse('로그인 실패. 다시 시도 해보세요.')
    else:
        form = LoginForm()
        return render(request, 'main/login.html', {'form': form})

def meetingdetail(request):
    filterName = request.GET.get('meetingid')
    meeting = Meeting.objects.filter(meetingId=filterName)
    context = {'meeting':meeting}
    return render(request, 'main/meetingdetail.html', context)


def nextbooksearch(request):
    searchKeyWord = request.GET.get('searchKey')
    client_id = "4oOHm4oAQ2oUFLEfXyKp"
    client_secret = "HKkulo_dgv"
    encText = urllib.parse.quote(str(searchKeyWord))
    url = "https://openapi.naver.com/v1/search/book?query=" + encText+"&sort=count&display=4"
    request_forNaver = urllib.request.Request(url)
    request_forNaver.add_header("X-Naver-Client-Id",client_id)
    request_forNaver.add_header("X-Naver-Client-Secret",client_secret)
    response = urllib.request.urlopen(request_forNaver)
    rescode = response.getcode()
    searchBook = []
    if(rescode==200):
        response_body = response.read()
        json_rt = response_body.decode('utf-8')
        py_rt = json.loads(json_rt)

        for i in range(0, len(py_rt['items'])):
            dic = {'isbn': py_rt['items'][i]['isbn'].split(' ')[1],
             'imgIndex': py_rt['items'][i]['isbn'].split(' ')[1][-3:],
             'imgAlt':py_rt['items'][i]['image'],
             'title':py_rt['items'][i]['title'],
             'author':py_rt['items'][i]['author'],
             'publisher':py_rt['items'][i]['publisher']}
            searchBook.append(dic)
    else:
        print("Error Code:" + rescode)
    form = wishbookForm()
    nosearch = ''    
    context = {'searchBook':searchBook}
    if (len(searchBook) == 0) :
        nosearch = ''
    else:
        nosearch = 'exist'

    return render(request, 'main/nextbook.html', {'searchBook':searchBook, 'nosearch':nosearch, 'form':form})

def post_wishBookdetail(request):
    post_isbn = request.POST.get('isbn')

    ourbook = Ourbooks.objects.filter(bookId=post_isbn)
    context = {}
    if( len(ourbook) > 0 ):
        context = {'message':'이미 발제한 책입니다.'}
        return HttpResponse(json.dumps(context), content_type="application/json")

    wishbook = Wishbooks.objects.filter(bookId=post_isbn)
    if( len(wishbook) > 0 ):
        context = {'message':'이미 등록된 책입니다. 등록된 책 리스트를 확인하세요'}
        return HttpResponse(json.dumps(context), content_type="application/json")
    else :
        context = {'message':''}
        return HttpResponse(json.dumps(context), content_type="application/json")

def wishlist(request):
    wishbook = Wishbooks.objects.all()
    for book in wishbook:
        book.imgindex = book.bookId[-3:]
    

    
    context = {'wishbook':wishbook}
    return render(request, 'main/nextbookwishlist.html', context)

def wishbookdelete(request):
    wishbook = Wishbooks.objects.get(bookId=request.GET.get('bookId'))
    wishbook.delete()
    return redirect('../wishlist/')

def like(request):
    if request.method == 'POST':
        user = request.user # 로그인한 유저를 가져온다.
        memo_id = request.POST.get('pk', None)
        wishlike = Wishbooks.objects.get(bookId = memo_id) #해당 메모 오브젝트를 가져온다.

        if wishlike.likes.filter(id = user.id).exists(): #이미 해당 유저가 likes컬럼에 존재하면
            wishlike.likes.remove(user) #likes 컬럼에서 해당 유저를 지운다.
            message = '좋아요를 취소합니다.'
        else:
            wishlike.likes.add(user)
            message = '좋아요를 눌렀습니다.'

    context = {'likes_count' : wishlike.total_likes, 'message' : message}
    return HttpResponse(json.dumps(context), content_type='application/json')

def staticsPage(request):
    
    presentation = request.GET.get('presentation')
    if presentation == '전체' or presentation == '' or presentation is None :
        presentation = ''
    
    #총 권수 구하기
    ourbook = Ourbooks.objects.all()
    totalCount = len(ourbook)

    #기준 날짜 가져오기
    meeting = Meeting.objects.filter(newMemberYN='Y')

    ourbookcount=[]
    cateName = category.objects.all().order_by('categoryCode')
    for catego in cateName :
        if catego.categoryName != '전체':
            ourbookcount.append(len(Ourbooks.objects.filter(category=catego.categoryName, presentation__contains=presentation, statusflag='R')))
    ddd = {'count':ourbookcount}
    sss = json.dumps(ddd)
    
    userInfo = User.objects.all()

    context = {'totalCount':totalCount, 'meeting':meeting, 'ourbookcount':sss, 'userInfo':userInfo, 'presentation': presentation}
    return render(request, 'main/staticsMain.html', context)

def chartReload(request):
    presentation = request.POST.get('presentation', None)
    if presentation == '전체' :
        presentation = ''
    ourbookcount=[]
    cateName = category.objects.all().order_by('categoryCode')
    for catego in cateName :
        if catego.categoryName != '전체':
            ourbookcount.append(len(Ourbooks.objects.filter(category=catego.categoryName, presentation__contains=presentation, statusflag='R')))
    ddd = {'count':ourbookcount}
    sss = json.dumps(ddd)

    return HttpResponse(sss, content_type='application/json')

def mypageMain(request):
    userName = User.objects.filter(username = request.user.get_username())
    mybooks = Ourbooks.objects.filter(presentation__contains=userName[0].first_name)
    for book in mybooks:
        book.imgindex = book.bookId[-3:]
    context = {'mybooks':mybooks}
    return render(request, 'main/mypage.html', context)

def mypageWish(request):
    mybooks = Wishbooks.objects.filter(register=request.user.get_username())
    for book in mybooks:
        book.imgindex = book.bookId[-3:]
    context = {'mybooks':mybooks}
    return render(request, 'main/mypagewish.html', context)


def mystatics(request):
    

    #총 권수 구하기
    userName = User.objects.filter(username = request.user.get_username())
    mybooks = Ourbooks.objects.filter(presentation__contains=userName[0].first_name)
    totalCount = len(mybooks)


    ourbookcount=[]
    cateName = category.objects.all().order_by('categoryCode')
    for catego in cateName :
        if catego.categoryName != '전체':
            ourbookcount.append(len(Ourbooks.objects.filter(category=catego.categoryName, presentation__contains=userName[0].first_name, statusflag='R')))
    ddd = {'count':ourbookcount}
    sss = json.dumps(ddd)
    
    userInfo = User.objects.all()

    context = {'totalCount':totalCount, 'ourbookcount':sss, 'userInfo':userInfo}
    return render(request, 'main/mystatics.html', context)




class ChartData(APIView):
    authentication_classes = []
    permission_classes = []

    def get(self, request, format=None):
        data = {
            "sales":100,
            "customers":10,
        }
        return Response(data)
