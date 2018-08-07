from django.shortcuts import render
from django.http import HttpResponse
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from .forms import PostForm
from .models import Meeting, category, Ourbooks, Reading
from django.shortcuts import redirect
import time

# index page loading.
def index(request):
    cateName = category.objects.all().order_by('categoryCode')
    ourbook = Ourbooks.objects.all().order_by('-readingdate')[:12]
    for book in ourbook:
        book.imgindex = book.bookId[-3:]
    meeting = Meeting.objects.all().order_by('meetingdate')
    count = 0
    for meet in meeting:
        count = count +1
        meet.lastorder = str(count)
    context = {'meeting':meeting, 'category':cateName, 'ourbooks':ourbook}

    return render(request, 'main/index.html', context)

# bookmain page loading.
def bookpage(request):
    
    cateName = category.objects.all().order_by('categoryCode')
    
    filterName = request.GET.get('kindName')

    if filterName is None or str(filterName)=='' or str(filterName)=='None':
        ourbook = Ourbooks.objects.all().order_by('-readingdate')
    else:
        ourbook = Ourbooks.objects.filter(category=filterName).order_by('-readingdate')

    PAGE_ROW_COUNT = 16
    PAGE_DISPLAY_COUNT = 5
    
    
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
            'filterName':filterName
            }
            )

# bookDetail page loading.
def bookDetail(request):
    cateName = category.objects.all().order_by('categoryCode')    
    
    filterName = request.GET.get('bookId')
    ourbook = Ourbooks.objects.filter(bookId=filterName)
    
    for book in ourbook:
        book.imgindex = book.bookId[-3:]

    context = {'category':cateName, 'ourbook':ourbook}
    return render(request, 'main/bookDetail.html', context)

# readinglist page loading.
def readinglist(request):
    reading = Reading.objects.select_related('bookId')
    print(reading)
    context = {'reading':reading}
    return render(request, 'main/readinglist.html', context)
    


# readingwrite page loading.
def readingWirte(request):
    now = time.localtime()
    nowDateTime = "%04d-%02d-%02d %02d:%02d:%02d" % (now.tm_year, now.tm_mon, now.tm_mday, now.tm_hour, now.tm_min, now.tm_sec)
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.created = nowDateTime
            post.writer = 'jjinho28'
            post.save()
            return redirect('../readinglist/')
    else:
        form = PostForm()
    return render(request, 'main/readingwrite.html', {'form': form})