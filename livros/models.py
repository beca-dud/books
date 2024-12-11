import django
from django.db import models

class Livro(models.Model):
    titulo = models.CharField(max_length=200, null=False)
    genero = models.CharField(max_length=100, null=False)
    nota = models.IntegerField(null=False)
    user = models.ForeignKey(django.contrib.auth.get_user_model(), on_delete=models.CASCADE)
    
def __str__(self):
    return self.titulo + 'pertence ao gênero' + self.genero + "e merece uma nota" + str(self.nota)