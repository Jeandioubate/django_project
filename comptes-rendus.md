# 2.2 Exercices parties (1 et 2)

## 2.2.1 Exercice d'administration

#### 1. Ajoutez une interface de la classe ***Choice***, comme précédemment fait dans le cours avec ***Question***.

>***from django.contrib import admin***
> 
>***from .models import Question, Choice***

>***admin.site.register(Question, QuestionAdmin)***
>***admin.site.register(Choice, ChoiceAdmin)***

#### 2. A l'aide de la nouvelle interface, ajoutez 5 questions avec 3 choix pour chaque question.
Attention : prendre soin de saisir des dates de publication différentes pour chaque question.

>Saisir cette adresse url ***http://127.0.0.1:8000/admin/polls/question/*** pour ajouter les questions en cliquant sur "Ajouter Question", remplir ensuite les champs et enregistrer.
> 
> Pareil pour les choix en saisissant l'adresse suivante : ***http://127.0.0.1:8000/admin/polls/choice/***. On sélectionne la question correspondante à chacun de ses choix.

#### 3. Visualisez le résultat des saisies dans l'interface admin.

* Voyez-vous tous les attributs de vos classes ? Non
* Pouvez-vous filtrer vos données suivants tous les attributs ? Non
* Pouvez-vous trier vos données suivants tous les attributs ? Non
* Pouvez-vous chercher un contenu parmi tous les champs ? Non

#### 4.  Les options de ModelAdmin pour rendre la réponse de la question (3) positive.
* list_display : ***contrôle les champs qui seront affichés sur la page de liste.***

* list_filter : ***active des filtres dans la barre de droite de la page de liste.***
* ordering : ***précise comment les listes d'objets doivent être ordonnées dans les vues d'administration.***
* search_fields : ***active une boîte de recherche sur la page de liste.***

#### 4.1 Ajoutez deux classes admin
```
> class QuestionAdmin(admin.ModelAdmin)

> class ChoiceAdmin(admin.ModelAdmin)
```
#### 4.2 Ajoutez les 4 options à chacune des 2 classes (fichier admin.py)
```

> class QuestionAdmin(admin.ModelAdmin):
    list_display = ('question_text', 'pub_date')
    list_filter = ('question_text','pub_date')
    ordering = ('question_text', 'pub_date')
    search_fields = ['question_text', 'pub_date']

> class ChoiceAdmin(admin.ModelAdmin):
    list_display = ('question', 'choice_text', 'votes')
    list_filter = ('question', 'choice_text', 'votes')
    ordering = ('question', 'choice_text', 'votes')
    search_fields = ['choice_text']

```
#### 4.3 Enregistrez les classes admin avec leur classe correspondante
```
> admin.site.register(Question, QuestionAdmin)
> admin.site.register(Choice, ChoiceAdmin)
```
#### code complet
```
from django.contrib import admin
from .models import Question, Choice


class QuestionAdmin(admin.ModelAdmin):
    list_display = ('question_text', 'pub_date')
    list_filter = ('question_text','pub_date')
    ordering = ('question_text', 'pub_date')
    search_fields = ['question_text', 'pub_date']

class ChoiceAdmin(admin.ModelAdmin):
    list_display = ('question', 'choice_text', 'votes')
    list_filter = ('question', 'choice_text', 'votes')
    ordering = ('question', 'choice_text', 'votes')
    search_fields = ['choice_text']


admin.site.register(Question, QuestionAdmin)
admin.site.register(Choice, ChoiceAdmin)
```