from django.contrib import admin

from . import models as sampling_station_models


admin.site.register(sampling_station_models.SamplingStation)
