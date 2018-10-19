from django.contrib import admin

# Register your models here.
from curriculo.models import Curso
admin.site.register(Curso)

from curriculo.models import Disciplina
admin.site.register(Disciplina)
