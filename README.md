---- PARTIE 1 ----
#commande d'installation des outils(avec connexion internet)
python -m pip install -r requirements.txt

#commande pour verifier installation
django-admin --version

#debut de creation du projet
django-admin startproject generateur

#on rentre dans le projet creer et on ouvre visual studio
#on configure le fichier settings.py qui se trouve dans le dossier generateur
#on descend jusquu'a la ligne 106 oû se trouve LANGUAGE_CODE
#on remplace 'en-US' par 'fr-FR'

# on damare le serveur
python manage.py runserver

#on ouvre un navigateur telque chrome ou edge puis on saisi dans la bare de recherche
# localhost:8000

#définition de template
#fichier html, css et javascript créé par d'autres développeurs qui va nous permettre 
#d'avoir des pages html personnalisées sans taper une seule ligne de code
#quelques sites où on peut trouver des templates
# bbbootstrap.com
# freecss

#pour arrêter le serveur on tape ctrl+c
### création d'application 
python manage.py startapp cryptage

#prise en compte de l'application cryptage
#pour que le projet prend en compte notre application, on doit ajouter le nom de notre 
#application sur la liste INSTALLED_APPS qui se trouve dans settings.py à la ligne 33


#codage d'application
#configuration des templates 
#pour que les templates soient accessibles, sans confusion, dans chaque application
#créée, on crée à l'intérieur de chaque application un dossier qui a pour nom templates
#on rentre dans chaque dossier templates puis on crée à l'intérieur un autre dossier qui
#a même nom que l'application dans laquelle le templates se trouve
#c'est dans les dossiers ayant les mêmes noms que les applications se trouvant dans
#les dossiers templates qu'on doit placer tous les fichiers html de chaque application


#configuration des fichiers 'static'
#définition: un fichier static, est un fichier css ou javascript ou image ou video
#pour que les fichiers static soient accessibles, il y a deux méthodes 
#1ère méthode: que nous nous allons utiliser dans le cas de notre application
#on crée à la racine de notre projet un dossier qui a pour nom static
#on rentre dans ce dossier static, on crée 4 sous dossiers qui sont:
#js, images, video, css
#la racine du projet est l'endroit où se trouve manage.py
#faire reconnaitre le dossier static au projet on rentre dans le fichier settings.py
#après la variable STATIC_URL qui est généralement à la ligne 119, on crée un variable
# STATICFILES_DIRS =[
    BASE_DIR / "static",

]

---- PARTIE 2 -----
#explication de l'arboressence de l'application
#dans notre application, on retrouve des dossiers et des fichiers
#_pycache_: c'est le dossier qui contient tous les fichiers caches (les anciens traitements)
#migrations: c'est le dossier qui contient tous les fichiers de migration permettant de créer une base de données
#templates: c'est dans ce dossier où se trouvent tous les fichiers html de l'application
#__init__: c'est ce fichier qui montre qu'on travaille avec le langage python 
#admin: c'est ce fichier qui contient toutes les configurations et personnalisations et l'interface d'administration
#apps: c'est le fichier qui contient toutes les configurations de l'application
#models: c'est le fichier qui contient toutes les tables liées à cette application 
#test: c'est le fichier qui contient tous les textes unitaires 
#views: c'est ce fichier qui contient toutes les requêtes, il joue le rôle du contrôleur

#création de la première page
#le premier élément à configurer est le fichier urls qui se trouve dans le dossier de configuration du projet (dossier qui a même
#nom que le projet), mais il faut d'abord créer un fichier urls.py dans chaque application, on fait la liaison des fichiers urls 
#en incluant tous les fichiers urls des applications dans le fichier urls du dossier de configuration 
#pour cela on rentre dans urls qui se trouve le fichier de configuration on importe le module include (on place ',' après path puis
#on écrit include)
#en fin dans la variable urlpatterns on ajoute à la fin path('',include('cryptage.urls')),


#affichage de la première page
#pour afficher une page on doit modifier deux fichiers qui se trouvent tous dans l'application et qui sont urls.py et views.py
#avant de modifier ces deux fichiers on doit créer le fichier html à afficher dans le templates des applications
#puis on crée une fonction qui renvoie la page htlm qu'on a créé, et on associe une urls à cette fonction créée 

--partie 3---
# MODIFICATION DU CONTENU DE LA PAGE HTML
# on ouvre notre fichier index.html, puis on creer un fichier index.css dans le dossier css qui se trouve dans le dossier static
#à l'interieur de index.html à la première ligne on charge les fichiers static en tapant
# {% load static %}
#puis on lie tous les fichier static 
#le lien des fichier static doit être {% static 'chemin/nom.extension' %}
