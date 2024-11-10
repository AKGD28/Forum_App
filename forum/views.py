from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.contrib.auth.password_validation import validate_password
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.http import JsonResponse

def auth(request):
    if request.method == "POST":
        if 'inscription' in request.POST:
            username = request.POST['username']
            email = request.POST['email']
            password = request.POST['password']
            confirmpwd = request.POST['comfirmpwd']
            if User.objects.filter(username=username):
                messages.error(request, "Nom d'utilisateur déjà pris, veuillez en essayer un autre.")
                return redirect('login')
            if User.objects.filter(email=email):
                messages.error(request, 'Cet email a un compte.')
                return redirect('login')
            if len(username) > 10:
                messages.error(request, "Le nom d'utilisateur ne doit pas contenir plus de 10 caractères.")
                return redirect('login')
            if len(username) < 5:
                messages.error(request, "Le nom d'utilisateur doit contenir au moins 5 caractères.")
                return redirect('login')
            if not username.isalnum():
                messages.error(request, "Le nom d'utilisateur doit être alphanumérique.")
                return redirect('login')
            if password != confirmpwd:
                messages.error(request, 'Le mot de passe ne correspond pas!')
                return redirect('login')
            try:
                validate_password(password)
            except ValidationError as e:
                messages.error(request, str(e))
                return redirect('login')
            
            user = User.objects.create_user(username=username, email=email, password=password)
            user.is_active = True
            user.save()

            user = authenticate(username=username, password=password)
            if user is not None and user.is_active:
                login(request, user)
                return redirect('home')  # Assure-toi que l'URL 'home' existe
        elif 'connexion' in request.POST:
            name = request.POST.get("username")
            password = request.POST.get("password")
            user = authenticate(username=name, password=password)
            if user is not None and user.is_active:
                login(request, user)
                return redirect('home')  # Redirige vers la page d'accueil
            else:
                messages.error(request, 'Nom d\'utilisateur ou mot de passe invalide')
                return redirect('login')

    return render(request, 'login.html')

def logout_view(request):
    logout(request)
    messages.success(request, "Vous êtes déconnecté.")
    return redirect('home')  # Redirection après la déconnexion

def posts_list(request):
    # Logique pour récupérer et afficher les posts
    return render(request, 'posts_list.html')

def test_view(request):
    return HttpResponse("Test view is working!")

def login_view(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('index')  # Redirige vers la page d'accueil
        else:
            messages.error(request, "Nom d'utilisateur ou mot de passe incorrect.")
            return redirect('login')
    return render(request, 'login.html')

def home_view(request):
    return render(request, 'home.html')  # Assure-toi d'avoir un template 'home.html'


def questions_list(request):
    # Récupère les questions à afficher (par exemple, depuis la base de données)
    return render(request, 'questions_list.html')  # Assure-toi que le template existe

def about_view(request):
    return render(request, 'about.html')  # Assure-toi que le template about.html existe

def publier_view(request):
    if request.method == 'POST':
        # logiques pour traiter les données soumises
        pass
    return render(request, 'publier.html')  # Assure-toi que le template publier.html existe

def mes_questions_view(request):
    # Logique pour récupérer les questions de l'utilisateur, par exemple :
    questions = []  # Remplace ceci par la logique pour récupérer les données
    return render(request, 'mes_questions.html', {'questions': questions})


def post_detail(request, post_id):
    # Ici, tu pourrais récupérer les détails de la publication avec l'ID donné.
    # Exemple :
    # post = get_object_or_404(Post, id=post_id)
    return render(request, 'post_detail.html', {'post_id': post_id})

def register(request):
    # Logique pour gérer l'inscription des utilisateurs
    # Exemple simple de rendu de template
    return render(request, 'register.html')

def add_question(request):
    # Logique pour ajouter une nouvelle question
    return render(request, 'add_question.html')

def chat(request):
    # Logique pour afficher ou gérer le chat
    return render(request, 'chat.html')

def my_questions(request):
    # Logique pour afficher les questions de l'utilisateur
    return render(request, 'my_questions.html')

def bricolons_ensemble(request):
    # Logique de la page "Bricolons ensemble"
    return render(request, 'bricolons_ensemble.html')

def home(request):
    return render(request, 'forum/home.html')  # Chemin correct vers le template




def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            login(request, user)
            messages.success(request, "Bienvenue ! Vous êtes connecté.")
            return redirect('home')
        else:
            messages.error(request, "Identifiants incorrects. Veuillez réessayer.")
    
    return render(request, 'forum/connexion.html')

def chat(request):
    # En fonction de ton modèle de chat, tu pourrais récupérer des messages depuis la base de données ici
    return render(request, 'forum/chat.html')

# Une vue pour envoyer les messages (si tu veux utiliser AJAX par exemple)
def send_message(request):
    if request.method == 'POST':
        message = request.POST.get('message')
        # Sauvegarder le message dans la base de données ou en mémoire
        # (Tu devrais créer un modèle Message pour stocker les messages)
        return JsonResponse({'message': message}, status=200)
    return JsonResponse({'error': 'Invalid request'}, status=400)

def register(request):
    print("Vue d'inscription appelée")  # Cela s'affichera dans la console
    return render(request, 'register.html')
