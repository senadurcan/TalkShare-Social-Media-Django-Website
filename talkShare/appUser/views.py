from django.shortcuts import render

# Create your views here.

def profile_page(request):
       context = {
           
       }
       return render(request, 'users/profile-page.html', context)




def login(request):
    context = {
        
    }
    return render(request, 'users/login.html', context)