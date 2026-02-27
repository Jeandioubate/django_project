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
#### 5. En ajoutant un nouvel utilisateur via l'interface admin, sans lui attribuer le statut "équipe" ou "super-utilisateur". En se déconnectant et essayant une nouvelle connexion avec le nouvel user, on rencontre ce message :
" Veuillez compléter correctement les champs (nom d'utilisateur) et (mot de passe) d'un compte autorisé. Sachez que les deux champs peuvent être sensibles à la casse." Par conséquent on ne peut pas se connecter avec le nouvel user.
#### 6. Reconnectez-vous avec l'admin (super-utilisateur) et faites en sorte que l'user puisse se connecter à l'interface admin. Profitez-en pour changer son mot de passe.
Pour que le nouvel user puisse se connecter via l'interface admin, il faut lui attribuer le statut "équipe" et le sauvegarder. 
Quant au mot de passe, il faut une réinitialisation pour le changer.
#### 7. L'utilisateur ayant quitté l'organisation, cherchez maintenant à désactiver son compte plutôt que de le supprimer. Vérifiez qu'il ne peut plus se connecter.
Pour désactiver un utilisateur, il faut décocher la case "Active" dans les permissions de la fiche de l'utilisateur et sauvegarder.
L'utilisateur ne peut plus se connecter et le message affiché par l'interface est le même qu'à la question 5.

## 2.2.2 Exercice shell
### 2.2.2.1 Préambule
* Ouvrir un terminal
* Aller dans le répertoire du projet
* Lancez le *shell* Django ($ python manage.py shell)
### 2.2.2.2 Questions
#### 1. Lister tous les objets de type Question : faites une boucle pour afficher les attributs de chaque question sur une ligne différente.
```
>>> for q in Question.objects.all():    
...     q.id, q.question_text, q.pub_date
```
#### 2. Ajoutez un filtre sur la date de publication-portant par ex. sur un de ses composants suivant : *year, month, day* - de vos questions et lister un sous-ensemble de vos questions suivant les dates que vous avez saisies à l'exo précédent.
```
>>> from django.utils import timezone
>>> current_day = timezone.now().day
>>> Question.objects.filter(pub_date__day=current_day)
```
#### 3. Trouver la deuxième question (pour laquelle l'attribut de clé primaire id=2) de votre base de données, puis affichez les valeurs de tous ses attributs et tous les choix associés.
```
>>> q = Question.objects.get(id=2)
>>> q.id, q.question_text, q.pub_date
>>> q.choice_set.all()
```
#### 4. Faites une boucle pour afficher les attributs de chaque question leurs choix associés.
```
>>> for q in Question.objects.all():
...     q.id, q.question_text, q.pub_date
...     for c in q.choice_set.all():
...         c.choice_text, c.votes
```
#### 5. Affichez le nombre de choix enregistrés pour chaque question.
```
>>> for q in Question.objects.all():
...     q, q.choice_set.count()
```
#### 6. [optionnel] Cherchez toutes les questions triées par le nombre de votes à chaque choix, en utilisant la méthode <ins>*order by()*</ins> – la méthode <ins>*values()*</ins> peut également être utilisée pour obtenir un affichage plus complet des questions. Essayer d'utiliser <ins>Recherches traversant les relations</ins> pour obtenir une solution la plus synthétique possible.
```
>>> for c in Choice.objects.all().order_by('votes'):
...     c.question.question_text, c.choice_text, c.votes
>>> for q in 
Question.objects.all().order_by('choice__votes').values('question_
text', 'choice__choice_text', 'choice__votes'):
...     q
>>> for c in 
Choice.objects.all().order_by('votes').values('question__question_
text', 'choice_text', 'votes'):
...     c
```
#### 7. Triez les questions par ordre antéchronologique.
```
>>> Question.objects.all().order_by('-pub_date')
```
#### 8. [optionnel] Cherchez toutes les questions dont un mot est présent dans le texte de ses choix, en utilisant la recherche <ins>*contains*</ins>. <ins>Recherches traversant les relations</ins> permet de bien comprendre la 3e solution proposée ci-après (qui est plutôt celle attendue avec Django) :
```
>>> for q in Question.objects.all():
...     for c in q.choice_set.all():
...         if 'Non' in c.choice_text:
...             print(q, c.choice_text)
...             break

>>> for q in Question.objects.all():
...     if any(map(lambda c: 'Non' in c.choice_text, 
q.choice_set.all())):
...         q, q.choice_set.all()
>>> Question.objects.filter(choice__choice_text__contains='Non')
```
#### 9. Créez une question en le shell.
```
>>> q = Question(question_text="Quelle est la couleur du cheval 
blanc d'Henri IV ?", pub_date=timezone.now())
>>> q.save()
>>> q.id # pour vérifier que la question a bien été rajoutée dans 
la base
```
#### 10. Ajoutez 3 choix à cette question en utilisant le shell.
```
>>> q.choice_set.create(choice_text="Blanc", votes=0)
>>> q.choice_set.create(choice_text="Noir", votes=0)
>>> q.choice_set.create(choice_text="Gris clair", votes=0)
```
#### 11. Listez les questions publiées récemment.
```
>>> for q in Question.objects.all():
...     if q.was_published_recently():
...         q
ou avec une compréhension de liste :
>>> [q for q in Question.objects.all() if 
q.was_published_recently()]
```
#### 12. [optionnel] Listez tous les utilisateurs enregistrés sur l'application, en s'inspirant de <ins>Utilisation du système d’authentification de Django</ins> > <ins>Création d'utilisateurs</ins> pour accéder à tous les objets de la classe User (s'inspirer également du code de la Q1).
```
>>> from django.contrib.auth.models import User
>>> User.objects.all()
```
# 3.2 Exercice parties (3 et 4)
Il est question de rajouter quelques fonctionnalités à l'application.
#### 1. Ajouter l'affichage de la date de publication du sondage dans le template *index.html*.
```
{% if latest_question_list %}
    <ul>
    {% for question in latest_question_list %}
        <li>
            <a href="{% url 'polls:detail' question.id %}">
                {{ question.question_text }}
            </a>
            <small>(publié le {{ question.pub_date|date:"d/m/Y à H:i" }})</small></li>
    {% endfor %}
    </ul>
{% else %}
    <p>No polls are available.</p>
{% endif %}
```
#### 2. Ajoutez une page http://127.0.0.1:8000/polls/all/ qui liste tous les sondages avec leur numéro id et leur titre portant un lien vers leur page de détail.

#### a. Ajouter la vue dans polls/views.py

```
from django.shortcuts import render
from .models import Question


def all_polls(request):
    questions = Question.objects.all()
    context = {
        'questions': questions
    }
    return render(request, 'polls/all.html', context)
```
#### b. Ajouter l'URL /polls/all/ dans polls/urls.py

```
from django.urls import path

from . import views

app_name = "polls"
urlpatterns = [
    path("", views.IndexView.as_view(), name="index"),
    path("<int:pk>/", views.DetailView.as_view(), name="detail"),
    path("<int:pk>/results/", views.ResultsView.as_view(), name="results"),
    path("<int:question_id>/vote/", views.vote, name="vote"),
    path('all/', views.all_polls, name='all'),
]
```
#### c. Créer un template polls/all.html

```
<h1>Liste de tous les sondages</h1>

{% if questions %}
    <ul>
    {% for question in questions %}
        <li>
            {{ question.id }} —
            <a href="{% url 'polls:detail' question.id %}">
                {{ question.question_text }}
            </a>
        </li>
    {% endfor %}
    </ul>
{% else %}
    <p>Aucun sondage disponible.</p>
{% endif %}
```
#### 3. Dans cette même page http://127.0.0.1:8000/polls/all/, modifier le lien porté par chaque question pour aboutir à une page du type http://127.0.0.1:8000/polls/1/frequency/ affichant les résultats du sondage en valeur absolue et en pourcentage plutôt que le formulaire de vote.

#### a. Ajouter l'URL frequency dans polls/urls.py
```
from django.urls import path

from . import views

app_name = "polls"
urlpatterns = [
    path("", views.IndexView.as_view(), name="index"),
    path("<int:pk>/", views.DetailView.as_view(), name="detail"),
    path("<int:pk>/results/", views.ResultsView.as_view(), name="results"),
    path("<int:question_id>/vote/", views.vote, name="vote"),
    path('all/', views.all_polls, name='all'),
    path('<int:question_id>/frequency/', views.frequency, name='frequency'),
]
```
#### b. Ajouter la vue frequency dans polls/views.py
```
from django.shortcuts import get_object_or_404, render
from .models import Question


def frequency(request, question_id):
    question = get_object_or_404(Question, pk=question_id)

    choices = question.choice_set.all()
    total_votes = sum(choice.votes for choice in choices)

    results = []
    for choice in choices:
        if total_votes > 0:
            percentage = (choice.votes / total_votes) * 100
        else:
            percentage = 0
        results.append((choice, percentage))

    context = {
        'question': question,
        'results': results,
        'total_votes': total_votes,
    }
    return render(request, 'polls/frequency.html', context)
```
#### c. Créer le template polls/frequency.html
```
<h1>{{ question.question_text }}</h1>

{% if results %}
    <ul>
    {% for choice, percentage in results %}
        <li>
            {{ choice.choice_text }} :
            {{ choice.votes }} vote{{ choice.votes|pluralize }}
            — {{ percentage|floatformat:2 }} %
        </li>
    {% endfor %}
    </ul>
    <p><strong>Total :</strong> {{ total_votes }} votes</p>
{% else %}
    <p>Aucun vote pour ce sondage.</p>
{% endif %}

<p><a href="{% url 'polls:all' %}">Retour à la liste des sondages</a></p>
```
#### d. Modifier les liens dans /polls/all/
Dans polls/all.html, on remplace le lien
```
<a href="{% url 'polls:detail' question.id %}">
```
par:
```
<a href="{% url 'polls:frequency' question.id %}">
```
#### 4. Ajoutez une page de statistiques http://127.0.0.1:8000/polls/statistics/ affichant diverses fonctionnalités :
#### a. Implémenter les méthodes de classe dans polls/models.py
```
    def total_votes(self):
        return self.choice_set.aggregate(total=Sum('votes'))['total'] or 0

    @classmethod
    def most_popular(cls):
        return max(cls.objects.all(), key=lambda q: q.total_votes(), default=None)

    @classmethod
    def least_popular(cls):
        return min(cls.objects.all(), key=lambda q: q.total_votes(), default=None)
```
#### b. Ajouter la vue statistics dans polls/views.py
```
def statistics(request):
    total_questions = Question.objects.count()
    total_choices = Choice.objects.count()
    total_votes = Choice.objects.aggregate(total=Sum('votes'))['total'] or 0

    average_votes = (
        total_votes / total_questions if total_questions > 0 else 0
    )

    most_popular = Question.most_popular()
    least_popular = Question.least_popular()

    last_question = Question.objects.aggregate(
        last_date=Max('pub_date')
    )
    last_question = Question.objects.filter(
        pub_date=last_question['last_date']
    ).first()

    context = {
        'total_questions': total_questions,
        'total_choices': total_choices,
        'total_votes': total_votes,
        'average_votes': average_votes,
        'most_popular': most_popular,
        'least_popular': least_popular,
        'last_question': last_question,
    }
    return render(request, 'polls/statistics.html', context)
```
#### c. Ajouter l'URL statistics dans polls/urls.py
```
from django.urls import path

from . import views

app_name = "polls"
urlpatterns = [
    path("", views.IndexView.as_view(), name="index"),
    path("<int:pk>/", views.DetailView.as_view(), name="detail"),
    path("<int:pk>/results/", views.ResultsView.as_view(), name="results"),
    path("<int:question_id>/vote/", views.vote, name="vote"),
    path('all/', views.all_polls, name='all'),
    path('<int:question_id>/frequency/', views.frequency, name='frequency'),
    path('statistics/', views.statistics, name='statistics'),
]
```
#### d. Créer le template statistics.html
```
<h1>Statistiques des sondages</h1>

<ul>
    <li>Nombre total de sondages : {{ total_questions }}</li>
    <li>Nombre total de choix : {{ total_choices }}</li>
    <li>Nombre total de votes : {{ total_votes }}</li>
    <li>Moyenne de votes par sondage : {{ average_votes|floatformat:2 }}</li>
</ul>

<h2>Popularité</h2>
<ul>
    <li>
        Question la plus populaire :
        {% if most_popular %}
            {{ most_popular.question_text }} ({{ most_popular.total_votes }} votes)
        {% else %}
            Aucune
        {% endif %}
    </li>
    <li>
        Question la moins populaire :
        {% if least_popular %}
            {{ least_popular.question_text }} ({{ least_popular.total_votes }} votes)
        {% else %}
            Aucune
        {% endif %}
    </li>
</ul>

<h2>Dernière question enregistrée</h2>
{% if last_question %}
    <p>{{ last_question.question_text }} — {{ last_question.pub_date }}</p>
{% else %}
    <p>Aucune question enregistrée.</p>
{% endif %}

<p><a href="{% url 'polls:all' %}">Retour à la liste des sondages</a></p>
```
#### 5. Ajoutez un formulaire - accessible par un lien depuis la page http://127.0.0.1:8000/polls/ – qui permette de créer une question.

#### a. Créer un nouveau fichier polls/forms.py
```
from django import forms
from .models import Question


class QuestionForm(forms.ModelForm):
    class Meta:
        model = Question
        fields = ['question_text', 'pub_date']
```
#### b. Ajouter la vue create_question dans polls/views.py
```
def create_question(request):
    if request.method == 'POST':
        form = QuestionForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('polls:index')
    else:
        form = QuestionForm()

    return render(request, 'polls/create_question.html', {'form': form})
```
#### c. Ajouter l'URL create dans polls/urls.py
```
from django.urls import path

from . import views

app_name = "polls"
urlpatterns = [
    path("", views.IndexView.as_view(), name="index"),
    path("<int:pk>/", views.DetailView.as_view(), name="detail"),
    path("<int:pk>/results/", views.ResultsView.as_view(), name="results"),
    path("<int:question_id>/vote/", views.vote, name="vote"),
    path('all/', views.all_polls, name='all'),
    path('<int:question_id>/frequency/', views.frequency, name='frequency'),
    path('statistics/', views.statistics, name='statistics'),
    path('create/', views.create_question, name='create'),
]
```
#### d. Créer un template create_question.html
```
<h1>Créer une nouvelle question</h1>

<form method="post">
    {% csrf_token %}
    {{ form.as_p }}
    <button type="submit">Créer</button>
</form>

<p><a href="{% url 'polls:index' %}">Retour aux sondages</a></p>
```
#### e. Ajouter le lien 'polls:create' dans polls/index.html
```
<p>
   <a href="{% url 'polls:create' %}">
      ➕ Ajouter une nouvelle question
   </a>
</p>
```
#### 6. Enrichissez-le pour permettre de saisir les choix possibles de façon simplifiée, en prévoyant 5 champs de saisie de choix, seuls les n premiers champs saisis (non vide) étant alors pris en compte comme choix de la question.

#### a. Modifier forms.py dans polls/forms.py, en ajoutant cinq champs supplémentaires.
```
from django import forms
from .models import Question


class QuestionForm(forms.ModelForm):

    choice1 = forms.CharField(required=False, label="Choix 1")
    choice2 = forms.CharField(required=False, label="Choix 2")
    choice3 = forms.CharField(required=False, label="Choix 3")
    choice4 = forms.CharField(required=False, label="Choix 4")
    choice5 = forms.CharField(required=False, label="Choix 5")

    class Meta:
        model = Question
        fields = ['question_text', 'pub_date']
```
#### b. Modifier la vue create_question dans polls/views.py.
```
def create_question(request):
    if request.method == 'POST':
        form = QuestionForm(request.POST)
        if form.is_valid():
            question = form.save()

            choices = [
                form.cleaned_data.get('choice1'),
                form.cleaned_data.get('choice2'),
                form.cleaned_data.get('choice3'),
                form.cleaned_data.get('choice4'),
                form.cleaned_data.get('choice5'),
            ]

            for choice_text in choices:
                if choice_text:
                    Choice.objects.create(
                        question=question,
                        choice_text=choice_text,
                        votes=0
                    )
            return redirect('polls:index')
    else:
        form = QuestionForm()

    return render(request, 'polls/create_question.html', {'form': form})
```
