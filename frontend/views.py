from django.shortcuts import render, redirect
import json, requests

def index(request):
    # current_user = request.user
    # print(current_user)
    return render(request, 'index.html')

def register(request):
    url = "http://localhost:8000/api/register/"
    if request.method == 'POST':
        data = request.POST.copy()
        if 'csrfmiddlewaretoken' in data:
            del data['csrfmiddlewaretoken']
        json_data = json.dumps(data.dict())
        print(json_data)
        response = requests.post(url, json=data)
        if response.status_code == 200:
            print('success')
            return redirect('login_user')
    return render(request, 'register.html')

def login(request):
    url = "http://localhost:8000/api/login/"
    if request.method == 'POST':
        data = request.POST.copy()
        if 'csrfmiddlewaretoken' in data:
            del data['csrfmiddlewaretoken']
        json_data = json.dumps(data.dict())
        response = requests.post(url, json=data)
        if response.status_code == 200:
            print('success')
            return redirect('home_user')
    return render(request, 'login.html')

def home(request):
    current_user = request.user
    url = "http://localhost:8000/api/list-article/"
    response = requests.get(url)
    articles = response.json()

    context = {
        'articles': articles,
    }

    return render(request, "home.html", context)

def createArticle(request):
    current_user = request.user
    url = "http://localhost:8000/api/create-article/"
    if request.method == 'POST':
        data = request.POST.copy()
        if 'csrfmiddlewaretoken' in data:
            del data['csrfmiddlewaretoken']
        data["username"] = request.user.pk
        json_data = json.dumps(data.dict())
        print(json_data)
        response = requests.post(url, json=data)
        if response.status_code == 200:
            print('success')
            return redirect('home_user')
    return render(request, "create.html")

def viewArticle(request, id):
    url = f"http://localhost:8000/api/article/{id}"
    response = requests.get(url)
    article = response.json()

    context = {
        'article': article,
    }

    return render(request, "article-view.html", context)

def updateArticle(request, id):
    url = f"http://localhost:8000/api/update-article/{id}/"

    if request.method == 'POST':
        title = request.POST.get('title')
        content = request.POST.get('content')

        data = {
            'id' : id,
            'username' : request.user.pk,
            'title': title,
            'content': content,
        } 
        print(data)
        response = requests.put(url, data=data)
        return redirect('view_article', id=id)

    return render(request, "update-article.html")

def deleteArticle(request, id):
    url = f"http://localhost:8000/api/delete-article/{id}"
    
    if request.method == 'POST':
        response = requests.delete(url)
        return redirect('home_user')
    return render(request, "delete-article.html")