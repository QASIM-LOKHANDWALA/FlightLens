from django.shortcuts import render

# Create your views here.
def register_view(request):
  pass

def login_view(request):
  if request.method == 'POST':
    email = request.POST.get("email")
    password = request.POST.get("password")
    print(email, password)
  return render(request, 'user_auth/login.html')

def logout_view(request):
  pass