<center>https://i.imgur.com/tklceW5.png</center>
#### Repository
- https://github.com/python-social-auth/social-app-django
- https://github.com/wise-team/python-social-auth-steemconnect/
- https://github.com/ipfs/py-ipfs-api
- https://github.com/jeffbr13/django-ipfs-storage

#### What Will I Learn?
- How to implementate steemconnect in django
- How to implementate IPFS as default file system storage in django

#### Requirements
- django >=2.0

#### Difficulty
- Intermediate

#### Tutorial Contents
Due to the fact that the latest tutorials about connecting the steemconnect to django appeared here more than a year ago, I decided to slightly refresh the @noisy user guide which explaining how to do this.
It is not bad, however, it lacks several elements, which means that instead of simply copying snippets and correctly running the application, we have to get tired why our SteemConnect does not work.

## <center>SteemConnect</center>
- Install
`pip install social-auth-steemconnect` and
`pip install social-auth-app-django` (or `social-auth-app-django==3.1.0`, if you have a problem installing the latest version)
- Write few lines of code in <b>settings.py</b>
```python
# # # Steemconnect
#
#
AUTHENTICATION_BACKENDS = ['steemconnect.backends.SteemConnectOAuth2', 'django.contrib.auth.backends.ModelBackend']
SOCIAL_AUTH_URL_NAMESPACE = 'social'
SOCIAL_AUTH_STEEMCONNECT_KEY = "myproject.app"
SOCIAL_AUTH_STEEMCONNECT_SECRET = "<here paste your secret to myproject.app>"
SOCIAL_AUTH_STEEMCONNECT_DEFAULT_SCOPE = ['vote', 'comment']
```
and `'social_django,'` w INSTALLED_APPS.
- For sure, add the following code in TEMPLATES > OPTIONS > context_processors
```
'social_django.context_processors.backends',
'social_django.context_processors.login_redirect',
```

- Also go to urls.py of the main application directory (where you have set the path to the admin panel) and paste it:
`path('', include('social_django.urls', namespace='social')),`

Everything is well set up, but where to get the authorization link right now? I am already saying.
- Go to your template where you want to add a login button and paste:
`<a href="{% url "social:begin" "steemconnect" %}">Login</a>`

.
.
## <center>IPFS</center>
Also, ipfs for django is neglected, on GitHub you can find one, not renewed for a long time, a project that will nevertheless be useful.
- First, download the main part of ipfs by selecting the appropriate version of your system:
https://dist.ipfs.io/#go-ipfs
- now install it (MAC OS/LINUX commands)
```
$ tar xvfz go-ipfs.tar.gz
$ cd go-ipfs
$ ./install.sh
```
- Install the package I mentioned earlier and ipfsapi for python
`pip install django-ipfs-storage`
`pip install ipfsapi`

If you want use IPFS in your upload model just..
- add this in settings.py
```
DEFAULT_FILE_STORAGE = 'ipfs_storage.InterPlanetaryFileSystemStorage'

IPFS_GATEWAY_API_URL = 'http://localhost:5001/ipfs/'
IPFS_STORAGE_GATEWAY_URL = 'http://localhost:8080/ipfs/'
```
- and create a model for uploading files to ipfs
```
from django.db import models
from ipfs_storage import InterPlanetaryFileSystemStorage 

class MyModel(models.Model):
    ipfs_file = models.FileField(storage=InterPlanetaryFileSystemStorage())

    def __str__(self):
        return ipfs_file.self.name
```
- Also put this in your views.py
```
def upload(request):
    if request.method == 'POST':
        form = ModelForm(request.POST, request.FILES)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.save()
            return redirect('index')
    else:
        form = ModelForm()
    return render(request, 'yourapp/upload.html', {'form':form})
```

and again the most important element, namely template.
- Go to template and create a form like this:
```
{% if form.errors %}
	<!-- Error messaging -->
	<div id="errors">
		<div class="inner">
			<p>There were some errors in the information you entered. Please correct the following:</p>
			{{ form.non_field_errors }}
			<ul>
				{% for field in form %}
					{% if field.errors %}<li>{{ field.label }}: {{ field.errors|striptags }}</li>{% endif %}
				{% endfor %}
			</ul>
		</div>
	</div>
{% endif %}

<form class="site-form" action="{% url 'upload' %}" method="post" autocomplete="off" enctype="multipart/form-data">
    {% csrf_token %}
    <div class="foo2">File</div>
    {{ form.as_p }}  OR   {{ form.ipfs_file }}
    <input type="submit" value="Upload">
```
Where {% url 'upload' %} change to your url in which the form is.

You will have the hash of the uploaded file as {{model.ipfs_file.name}} and a direct link to the file {{model.ipfs_file.path}} (Of course, after looking in the view.py file, we returned the records to the template via context and then in the template we looped variable using {{for x in contextvar_from_views}} but this is the basics of django)

<center>!!! DON'T forget run ipfs daemon by command: `ipfs daemon` otherwise, port 5001 will not work properly !!!</center>

#### Curriculum
It's full tutorial. No more episodes.

#### Proof of done work
- 
