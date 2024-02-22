from django.shortcuts import render
from .models import Category, News
import requests


def home_page(request):
    categories = Category.objects.all()
    news = News.objects.all().order_by('-created_at')
    context = {
        'categories': categories,
        'news': news,
    }
    return render(request, 'index.html', context=context)


def single_page(request, news_slug):
    news = News.objects.get(slug=news_slug)
    tranding_news = News.objects.all().order_by('-views')[:5]
    news.views += 1
    news.save()

    context = {
        'news': news,
        'tranding_news': tranding_news,
    }
    return render(request,'single.html', context=context)


def category_page(request, category_slug):
    categories = Category.objects.all()
    news = News.objects.filter(category__slug=category_slug)
    context = {
        "news": news,
        "categories": categories
    }
    return render(request,'category.html', context=context)


def contact_page(request):
    if request.method == 'POST':
        token = ''
        chat_id = -100
        name = request.POST.get('name')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        message = request.POST.get('message')

        content = f"Ism: {name}\nE-Pochta: {email}\nMavzu: {subject}\n Xabar: {message}"

        url = f"https://api.telegram.org/bot{token}/sendMessage?chat_id={chat_id}&text={content}"
        requests.post(url)

    return render(request, 'contact.html')

