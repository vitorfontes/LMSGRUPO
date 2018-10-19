from django.db import models

# Create your models here.
class Curso(models.Model):
    def __str__(self):
        return "Nome: " + self.nome + " - Email: " + self.ano

    nome = models.TextField(max_length=255)
    ano = models.TextField(max_length=255)

    def save(self):
        print('estou salvando!')
        if(self.nome == ''):
            raise Exception('nome do curso nao enviado')
        if(self.ano == ''):
            self.ano = "ano nao fornecido"
        curso_nome = Curso.objects.filter(nome=self.nome)
        if len(Curso_nome) >0:
            raise Exception("nome ja utilizado")
        super(Curso,self).save()

class Disciplina(models.Model):
    def __str__(self):
        return "Nome: " + self.nome + " - Email: " + self.ementa

    nome = models.TextField('Nome',max_length=50)
    etiqueta = models.TextField('Etiqueta', max_length=50)
    carga_horario = models.IntegerField("Carga Horaria")
    

    def save(self):
        print('estou salvando!')
        if(self.nome == ''):
            raise Exception('login nao enviado')
        if(self.ementa == ''):
            self.ementa = "email nao fornecido"
        disciplina_nome = Disciplina.objects.filter(nome=self.nome)
        if len(disciplina_nome) >0:
            raise Exception("nome ja utilizado")
        super(Disciplina,self).save()