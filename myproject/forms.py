from django.forms import modelformset_factory
from .models import *
from django.forms import TextInput


MyProjectFormSet = modelformset_factory(
    MyProject, fields=("field", ), extra=1, labels={"field": 'Данные'}, widgets={"field": TextInput()}
)
