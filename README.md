# DjangoProjects

django-admin startproject <project Name> -- To create project
django-admin startapp <app Name> -- To create app inside project directory

python manage.py runserver -- To start server
python manage.py makemigrations --> To create migrations or DB like object, class needs to be created first
python manage.py migrate --> create table
python manage.py shell -- > opens python shell

Object Relational Mapper Query -->

    1. modelname.objects.all()  --? list all data from model
    2. Create an object of Model i.e. a = Book(name="Name of Book",..)  --> This will create one object of model
    3. a.save()  --> commiting to Model

### Steps in Django

1. Creaate Folder
2. Create Project using cmd -- django-admin startproject <project_name>
3. Create App inside project -- django-admin startapp <app_name>
4. start server -- python manager.py runserver

### Stpes To create simple url --

1. To actually create one functionality in Django, you need to create function in views.py inside your app directory.
2. import --> from django.http import HttpResponse
3. Add fucntion there -- def products(request): return HttpResponse("Some response")
4. Register this fucntion in project_directory/urls.py
5. Inside urls.pyl, import views
6. under urlpatterns, add path --> path("urlpath/", views.function_name, name=name),

### Steps to create Model or Table in Db --

1. Write class inside models.py -- class Book(models.Model)
2. Define variables or columns in table as -- name = models.charField(max_length=100) , price = medels.IntegerField()
3. Open cmd and run python manage.py makemigrations
4. Create Taable --> python manage.py migrate
5. Open shell
6. Import table as from MyApp.models import Book
7. Create objetct of class and add values
8. Book.objects.all() will give you all values

### Stpes To views Model in Admin console of Django --

1. Import .models import Book ( inside admin.py)
2. add method admin.site.register(Book)

List your app in settings.py under "installed_apps" list.

### Templates in Django -- Templates in Django renders the template and models in order to create dynamic webpage

1. Create templates directory inside app directory
2. Create another folder with same name of app directory.(MyApp)
3. create html files inside -- index.html
4. in views.py, inside function use retunr render(request,MyApp/index.html, context)
5. To retrieve variables values or context values, use {{context_name}}

### Adding more dynamics

1. Suppose you want to create page which lists out all the id of books and you want to click on that id to get detailed view of books
2. Create one view that lists out all id of books
3. Create an another view that consistes of details
4. List this view in url patterns --> since once we click on an id, url will be localhost:8000/book/{id of book} -- since id of book is variable of type int
5. to pass variable to url, write static paart then <type of varibale(int, string) : name of variable>
6. E.g. path("books/<int: book_id>", views.deatils, name ="Details"),

### Note :- Flow Of Request

    	1. django serach for url pattern in urls.py
    	2. matching url pattern, djnago replaces variable with passing value and call respective view function
    	3. Execution of function -- this can render html page also

example :-
views.py
def products(request):
books_list = Book.objects.all()
context = {
"books_list" : books_list
}
return render(request, 'MyApp/prodcuts.html', context)
products.html

<h1> List Of Books </h1>
<ul>
{% for book in books_list %}
<li>{{book.id}} : <a href="{% url 'MyApp:details' book.id %}"{{book.name}} </li>
{% endfor %}
views.py
def details(request, book_id)
book = Book.objects.get(book_id)
context = {
"book" : book
}
return render(request, 'MyApp/details.html', context)
details.html
<h1> Details of {{book.name}} <h1>
<ul>
<li> Name : {{book.name}} </li>
<li> Genre: {{book.genre}} </li>
<li> Price: {{book.price}} </li>
</ul>
urls.py in MyApp ( import everything)
app_name = 'MyApp'
urlpatterns = [
path('products/', views.products, name='products'),
path('products/book/<int: book_id>', views.details, name='details'),
}
urls.py in MySite ( import include from djnago.urls)
urlpatterns = [
path('', include('MyApp.urls'),
]

### Including another URLconf

    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))

### Includinng static file (css and images) --

    1. Create folder static/MyApp/style.css
    2. Enter or link style.css in html as <link rel="stylesheet", href="{% static 'MyApp/style.css' %}">
    3. On top of HTMl page, add {% load static %}

### Adding bootstrap and managing repeated code in Django-HTMl

1.  Install bootstrap by adding css link of it
2.  Add components of your choice
3.  Create bas.html in templates/MyApp directory
4.  Add html tag and paste all css link from index.html or any other file that are repetative in base.html file
5.  Add repetative code in base.html
6.  Now the code which is specific to particular file like index.html, create block in base.html as follow:-

        {% block body %}
        {%endblock%}

7.  Now remove repetative code or unnecessary code from index.html
8.  First exetnds base.html file as follows :-

        {% extends 'MyApp/base.html'%}  # since base.html is inside MyApp directory

9.  Enclose specific code in below block tag
10.     {% block body %}
        {% endblock %}

### To add form inside Django-html, we first need to add csrf-token inside html file as below:

    		<form method="POST" enctype="multipart/form-data"> --> very very important
    			{% csrf_token %}
    			<input type="text", name="name_of_Variable", id="name_of_Variable" placeholder="enter name"> --> here name and id shouldd be kept same as variable name in model
    		</form>

### To get the contents of POSt request :

1. Inside views.py, under def add_book(request),
2. Add if condition to check if request is post request
3. if request.method == "POST"
4. Inside if condition, retrieve all form values as below
5. name = request.POST.get('name',) --> this is for string and integer
6. For files data, use book_image = request.FILES['book_image']

### Updating an entry inside databse using html template

1.  First create forms.py inside MyApp directory

    from django import forms
    from .models import Book

    class BookForm(forms.ModelForm):
    class meta:
    model = Book
    fields = ['name', 'genre', 'price', 'book_image']

2.  Then in views.py import forms

3.  from .forms import BookForm

4.  Inside views.py, add ur function

    def update(request,id):

        book = Book.objects.get(id=id)

        # creating form object and passing request.POST or None, FILES if any and instance of book object which is to be updated
        form = BookForm(request.POST or None, request.FILES, instance=book)

        if form.is_valid():
        	form.save()
        	return redirect('/')

        return render(request, 'MyApp/update.html', {'form': form, 'book': book})

### Class based views -

    Generic Views :-



    	1. Built in class based views are called as Generic views

    	2. used for common tasks such as listing objects, displaying their details, adding objects, uodating object and deleting objects

    	3. E.g. ListView - used to display list of objects

    	4. DetailView, CreateView, UpdatedView and DeleteView




    1. Import generic view

    		from django.views.generic import DetailView, CreateView, UpdatedView, DeleteView, ListView

    2. Create custome class and extends import generic view classes

    		class TaskListView(ListView):

    			model = <assign model object or instance of model>

    			template_name = <template to be render for this view>

    			context_object_name = 'task_list'


    3. In urls.py

    		path('list/', views.TaskListView.as_view(), name='index')

# Django Rest framework

1.  Install Django rest fremawork

    sudo install djnagorestframework

2.  Architecture

3.  Here our main app communicates with different apis(that we create) in the backend

4.  First start Django prohject

    django-admin startproject mysite

5.  Create app

    django-admin startapp MyApp

6.  Now suppose your app has Movie model which has 3 fields

    models.py in MyApp

    Class Movie(models.Model):

        name = models.CharField(max_length=100)
        desc = models.CharField(max_length=100)
        rating =  models.FloatField()

7.  Now run makemigrations command to start Db

8.                     python manage.py makemigrations

    python manage.py migrate

9.  Create some fields in your models

10. Now create another app in mysite as follows

    django-admin startapp movieapi

11. So basically this app will fetch all movie details whenever we type url "http://localhost/movieapi"

12. Create urls.py inside movieapi

13. In mysite.urls, include movieapi.urls as follows

    from django.urls import path, include
    from movieapi import urls

    urlpatterns = [
    path('admin/', admin.site.urls),
    path('movieapi/', include('movieapi.urls')) #so basically if url containes /moviapi/ then redirect to movieapi app
    ]

14. In movieapi.urls

    from .views import movieAPIView

    urlspatterns = [
    path('', movieAPIView.as_view, name='movieapi')
    ]

15. Now, we have to create movieAPIView generic class view in our views.py

    from myapp.models import Movie
    from rest_framework import generics

    class movieAPIView(generics.ListAPIView):

        queryset = Movie.objets.all()

16. Now to serialize the field in JSON format from Movie model, we need serializers

17. Create serializers.py in movieapi app

18. Inside this file, create following

    from rest_framework import serializers
    from myapp.models import Movie

    class MovieSerializers(serializers.ModelSerializer):

        class Meta:
        	model = Movie  #assigning model of which field need to be serialized
        	fields = ['name', 'desc', 'rating'] # include which fields you want to serialize

19. Now add this serializers to moviAPIView generic class as follows:

    from myapp.models import Movie
    from rest_framework import generics
    from .serializers import MovieSerializers

    class movieAPIView(generics.ListAPIView):
    queryset = Model.objects.all()
    serializer_class = MovieSerializers

20. Now run server, and enter url as localhost:8000/movieapi and it wil give you json formmated result that consists of fields from Movie model

## fetching single detail from models

1. Create url in movieapi.urls as follows

   from .views import MovieDetailView

   path('<int:pk>', MovieDetailView.as_view, name="detailview")

2. Create MovieDetailView in view.py file as follows

   from myapp.models import Movie
   from rest_framework.models import generics
   from .serializers import MovieSerializers

   class MovieDetailView(generics.RetrieveAPIView):
   queryset = Movie.objects.all()
   serializer_class = MovieSerializers

3. Now enter url as "localhost:8000/movieapi/1" and get detil of first movie and so on.

## Posting data to models

1.  Django rest framework has generics.ListCreateAPIView to actually create and list entries from Models.

2.  To retrieve, update and delete in single view in DjnagoRestFramework -- generics.RetrieveUpdateDestroyAPIView

## To allow serializers to serialize file like images and all other, for images Ipllow package is required

4.  Inside serializers.py,

    from myapp.models import Movie
    from rest_framework import serializers

    class MovieSerializers(serializers.ModelSerializer):

        image = serializers.ImageField(max_length=None, use_url=true)

        class Meta:
        	model = Movie
        	fields = ['name', 'desc', 'rating', 'image']

## Since our backend service runs on 8000 port i.e. moviapi, Fro frontend we need to have different port to run

## To exchange data between this port, we need to have django's CROS package

1.           pip install django-cors-headers==3.2

2.  After instaling package, add corsheaders to installed_app section in settings.py of project

3.  'corsheaders.middleware.CorsMiddleware', to Middleware section

4.  ADD below section to whitlist ports for cross origin

    CORS_ORIGIN_WHITELIST = (
    'http://localhost:3000',
    'http://localhost:8000'
    )

## Connect Django API to React frontend to render Movie Details
