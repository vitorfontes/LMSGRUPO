from django.db import models

# Create your models here.
class Professor(models.Model):
    def __str__(self):
        return "Nome: " + self.nome + " - Email: " + self.email

    nome = models.TextField(max_length=255)
    email = models.TextField(max_length=255)
    celular = models.TextField(max_length=20)
    login = models.TextField(max_length=20)
    senha = models.TextField(max_length=20)

    def save(self):
        print('estou salvando!')
        if(self.login == ''):
            raise Exception('login nao enviado')
        if(self.email == ''):
            self.email = "email nao fornecido"
        professores_login = Professor.objects.filter(login=self.login)
        if len(professores_login) >0:
            raise Exception("login ja utilizado")
        super(Professor,self).save()
class Disciplina(models.Model):
    def __str__(self):
        return "Nome: " + self.nome + " - Email: " + self.ementa

    nome = models.TextField(max_length=50)
    ementa = models.TextField(max_length=5000)
    

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

class DisciplinaOfertada(models.Model):

    curso = models.TextField(max_length=255)
    turma = models.TextField(max_length=255)
    ano = models.TextField()
    semestre = models.TextField()
    professor = models.TextField()
    disciplina = models.IntegerField()
    
    def save (self):
        if(self.curso != 'ADS' and self.curso != 'SI' and self.curso != 'BD' ):
            raise Exception("curso não existe")
        ofertada_curso = DisciplinaOfertada.objects.filter(curso=self.curso)
        ofertada_turma = DisciplinaOfertada.objects.filter(turma=self.turma)
        ofertada_ano = DisciplinaOfertada.objects.filter(ano=self.ano)
        ofertada_semestre = DisciplinaOfertada.objects.filter(semestre=self.semestre)
        ofertada_professor = DisciplinaOfertada.objects.filter(professor=self.professor)
        ofertada_disciplina = DisciplinaOfertada.objects.filter(disciplina=self.disciplina)
        if (len(ofertada_curso) >0) and (len(ofertada_turma) >0) and (len(ofertada_ano) >0) and (len(ofertada_semestre) >0) and (len(ofertada_professor) >0) and (len(ofertada_disciplina) >0) :
            raise Exception("disciplina já existe")
        
        super(DisciplinaOfertada,self).save()

        










