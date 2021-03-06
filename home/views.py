from django.shortcuts import render

# Create your views here.

from home.models import CustomText, HomePage


def home(request):
    packages = [
	{'name':'google-assistant-sdk', 'url': 'http://pypi.python.org/pypi/google-assistant-sdk/0.4.2'},
	{'name':'boto3', 'url': 'http://pypi.python.org/pypi/boto3/1.5.15'},
	{'name':'django-googlecalendar', 'url': 'http://pypi.python.org/pypi/django-googlecalendar/3.0.0'},
	{'name':'djangorestframework', 'url': 'http://pypi.python.org/pypi/djangorestframework/3.7.7'},
	{'name':'django-bootstrap4', 'url': 'http://pypi.python.org/pypi/django-bootstrap4/0.0.5'},
	{'name':'django-allauth', 'url': 'http://pypi.python.org/pypi/django-allauth/0.34.0'},
    ]
    context = {
        'customtext': CustomText.objects.first(),
        'homepage': HomePage.objects.first(),
        'packages': packages
    }
    return render(request, 'home/index.html', context)
