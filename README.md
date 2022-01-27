# P11_FOSTER_Harris
Güdlft

Projet 11 OpenClassrooms

## MVP Application Flask de Réservation de Compétitions qui permet aux utilisateurs de :
- S'authentifier grâce à leurs informations de compte
- Réserver des places dans les compétitions grâce à leurs points
- Vérifier leurs points de réservation

## Prérequis de base
- Une application de type 'terminal' - GitBash, Mintty, Cygwin (si vous êtes sur Windows) 
   ou les terminaux par défaut si vous utilisez Macintosh ou Linux. 
- Python 3.9+
- Flask 2.01+

## Installation
### Pour les développeurs et utilisateurs (windows 10, mac, linux) :
#### Clonez la source de Güdlft localement (en utilisant votre terminal) :
```sh
$ git clone https://github.com/harrisafoster/P11_FOSTER_Harris
$ cd P11_FOSTER_Harris
```
##### Dans votre terminal dans le dossier P11_FOSTER_Harris/ : Créer et activer un environnement virtuel avec (windows 10) :
```sh
$ python -m venv env
$ source ./env/Scripts/activate
```
##### Créer et activer un environnement virtuel avec (mac & linux) :
```sh
$ virtualenv venv
$ source venv/bin/activate
```
##### Installez les packages requis avec :
```sh
$ pip install -r requirements.txt
```
## Utilisation
### Vous pouvez mettre Güdlft en route depuis votre terminal avec :
```sh
$ export FLASK_APP=server.py
$ flask run
```
Puis accédez à l'Application via le port 5000 sur votre navigateur sur http://127.0.0.1:5000/

## Procédure de tests
Informations sur les tests PyTest/Locust disponible ici : https://github.com/harrisafoster/P11_FOSTER_Harris/tree/master/locust_pytest_results

### Bugs/améliorations résolus
1. improvement/points_display_board 
2. bug/points_updates 
3. bug/book_past_competitions 
4. bug/book_more_than_12 
5. bug/spend_more_than_own_points 
6. bug/unknown_email_crash 
7. feature/3_points_per_place

## Testé avec
PyTest 6.2.5

PyTest-Flask 1.2.0

Locust 2.5.1

Coverage 6.2

## Construit avec
Python 3.9 

Flask 2.0.1
