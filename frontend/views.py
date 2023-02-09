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
        response = requests.post(url, json=data)
        if response.status_code == 200:
            print('success')
            return redirect('login_user')
    return render(request, 'register.html')

def login(request):
    return render(request, 'login.html')