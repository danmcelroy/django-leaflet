"""mushrooms URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/stable/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls import url
from django.conf.urls.static import static
from django.views.generic import TemplateView
from djgeojson.views import GeoJSONLayerView

from .models import SamplingStation


urlpatterns = [
    url(r'^$', TemplateView.as_view(template_name='sampling_stations/index.html'), name='sampling_stations'),
    url(r'^station_data.geojson$', GeoJSONLayerView.as_view(model=SamplingStation, properties=('title', 'description')), name='station_data')
]
