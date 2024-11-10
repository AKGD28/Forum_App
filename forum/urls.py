from django.urls import path
from . import views
from django.contrib.auth import views as auth_views  # pour les vues de connexion et déconnexion
from .views import posts_list
from .views import test_view
from .views import login_view
from .views import home_view, questions_list, about_view  # Assure-toi d'importer ta nouvelle vue
from .views import publier_view  # Assure-toi d'importer la nouvelle vue
from .views import mes_questions_view  # Assure-toi d'importer la nouvelle vue
from .views import home
from .views import post_detail
from .views import register
from .views import add_question
from .views import chat
from .views import my_questions
from .views import bricolons_ensemble
from forum import views  # Remplace `your_app_name` par le nom de ton application
from django.contrib import admin





urlpatterns = [
    path('', views.home, name='home'),  # Page d'accueil
    path('posts/', views.posts_list, name='posts_list'),  # Liste des publications
    path('posts/<int:post_id>/', views.post_detail, name='post_detail'),  # Détail d'une publication
    path('register/', views.register, name='register'),  # Page d'inscription
]
urlpatterns = [
    # Page d'accueil
    path('', views.home, name='home'),
    
    # Liste des publications
    path('publications/', views.posts_list, name='posts_list'),
    
    
    path('publications/<int:post_id>/', views.post_detail, name='post_detail'),
    
    
    path('add/', views.add_question, name='add_question'),

   
    path('inscription/', views.register, name='register'),

    
    

    path('chat/', views.chat, name='chat'),
    
 
    path('mes_questions/', views.my_questions, name='my_questions'),

    # Page "Bricolons ensemble" pour les projets collaboratifs
    path('bricolons_ensemble/', views.bricolons_ensemble, name='bricolons_ensemble'),

    path('chat/', views.chat, name='chat'),
    # Autres routes...

    path('connexion/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('deconnexion/', auth_views.LogoutView.as_view(), name='logout'),

    path('publications/', posts_list, name='posts_list'),  # Assure-toi que cette ligne est correcte
    # Autres URLs...

    # ... tes autres URL
    path('test/', test_view, name='test_view'),

    path('questions/', views.questions_list, name='questions_list'),
    # autres URL de l'application

    path('login/', login_view, name='login'),

    path('about/', about_view, name='about'),  # Ajoute cette ligne

    path('', home_view, name='home'),  # Assure-toi que cela est défini
    path('publier/', publier_view, name='publier'),  # Ajoute cette ligne
    # D'autres chemins...

     path('mes_questions/', mes_questions_view, name='mes_questions'),  # Ajoute cette ligne
    # D'autres chemins...

    path('login/', views.login_view, name='login'),  # Ajoute cette ligne pour la page de connexion

    path('', posts_list, name='posts_list'),

    path('questions/', questions_list, name='questions_list'),  # Ajoute cette route

    path('', home, name='home'),
    path('register/', views.register, name='register'),


    path('posts/<int:post_id>/', post_detail, name='post_detail'),
    # autres routes

    path('register/', register, name='register'),

    path('add/', add_question, name='add_question'),

    path('chat/', chat, name='chat'),

    path('mes_questions/', my_questions, name='my_questions'),

     path('bricolons_ensemble/', bricolons_ensemble, name='bricolons_ensemble'),
    # autres routes

    path('chat/', views.chat, name='chat'),
    path('send-message/', views.send_message, name='send_message'),  # Si tu utilises AJAX pour envoyer un message

    path('', views.home, name='home'),  # Exemple de route pour la page d'accueil
    path('questions/', views.questions_list, name='questions_list'),  # Exemple pour la liste de questions
    path('register/', views.register, name='register'),  # Ajoute cette ligne pour la page d'inscription

    path('admin/', admin.site.urls),
    path('', views.home, name='home'),  # Page d'accueil
    path('questions/', views.questions_list, name='questions_list'),  # Liste de questions
    path('register/', views.register, name='register'),  # Page d'inscription




   

]



