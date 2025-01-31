from django.db import models
from home.models import CustomBaseModel

class Metodo(CustomBaseModel):
    nome = models.CharField(max_length=100)
    
    def __str__(self):
        return self.nome

class Linhagem(CustomBaseModel):
    nome = models.CharField(max_length=100)
    
class Botijao(CustomBaseModel):
    numero = models.CharField(max_length=20)

    def __str__(self):
        return self.numero
    
class Caneco(CustomBaseModel):
    botijao_pk = models.ForeignKey(Botijao, on_delete=models.CASCADE)

    numero = models.CharField(max_length=20)
    data = models.DateField()
    linhagem = models.ForeignKey('Linhagem', blank=True, null=True, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.numero
    

class Hack(CustomBaseModel):
    cor_choices = {
        (1, 'Verde'),
        (2, 'Amarelo'),
        (3, 'Vermelho'),
    }

    caneco_pk = models.ForeignKey(Caneco, on_delete=models.CASCADE)

    numero = models.CharField(max_length=20)
    cor = models.IntegerField(max_length=2, choices=cor_choices, blank=True, null=True)

    def __str__(self):
        return self.numero
    
class Palheta(CustomBaseModel):
    hack_pk = models.ForeignKey(Hack, on_delete=models.CASCADE)

    numero = models.CharField(max_length=20)
    metodo = models.ForeignKey('Metodo', blank=True, null=True, on_delete=models.CASCADE)
    observacao = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.numero
    