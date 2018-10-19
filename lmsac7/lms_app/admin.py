from django.contrib import admin

# Register your models here.
from lms_app.models import Professor
admin.site.register(Professor)


from lms_app.models import Disciplina
admin.site.register(Disciplina)


from lms_app.models import DisciplinaOfertada
admin.site.register(DisciplinaOfertada)