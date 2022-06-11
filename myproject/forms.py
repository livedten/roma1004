from django.forms import modelformset_factory
from .models import *


MyProjectFormSet = modelformset_factory(
    MyProject, fields=('name',), extra=1, labels='Имя'
)
