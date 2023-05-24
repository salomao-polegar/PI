from django.db import models
from django.utils.timezone import   localtime

# class Loja (models.Model):
#     nome = models.TextField(max_length=50)
#     endereco = models.TextField("Endereço", max_length=300)
#     horario = models.TextField("Horário", max_length=50)
#     telefone = models.TextField(max_length=11)
#     email = models.TextField(max_length=50)
#     website = models.TextField(max_length=50)
    
#     def __str__(self):
#         return self.nome

class FormasDePagamento(models.Model):
    tipo_pagamento = models.CharField(max_length=30, unique=True)
    def __str__(self):
        return self.tipo_pagamento
    
# class Aceita(models.Model):
#     loja = models.ForeignKey(Loja, on_delete=models.CASCADE)
#     formaDePagamento = models.ForeignKey(FormasDePagamento, on_delete=models.CASCADE)
    
#     def __str__(self):
#         return str(self.loja) + " aceita " + str(self.formaDePagamento)
    
# class Profissional (models.Model):
#     loja = models.ForeignKey(Loja, on_delete=models.CASCADE)
#     nome = models.TextField(max_length=50)
#     telefone = models.TextField(max_length=11)
#     resumo = models.TextField(max_length=500)
    
#     def __str__(self):
#         return self.nome

class TipoServico (models.Model):
    tipo = models.TextField(max_length=50)
    descricao = models.TextField(max_length=500)
    
    def __str__(self):
        return self.tipo

    
class Servico (models.Model):
    servico = models.TextField(max_length=50)
    descricao = models.TextField(max_length=500, blank=True, null=True)
    tipoServico = models.ForeignKey(TipoServico, on_delete=models.CASCADE)
    fotoPrincipal = models.ImageField(upload_to='fotos/%d/%m/%Y/', blank=True)
    valor = models.FloatField(blank=True, null=True)
    duracao = models.TimeField("Duração")

    def __str__(self):
        return self.servico
    
# class Subservico (models.Model):
#     servico = models.ForeignKey(Servico, on_delete=models.CASCADE)
#     tipo_de_cobranca = models.TextField(max_length=50)
#     descricao = models.TextField("Descrição", max_length=50)
#     valor = models.FloatField()
#     duracao = models.TimeField("Duração")
    
    # def __str__(self):
    #     return str(self.servico) + " (" + str(self.tipo_de_cobranca) + " | " + str(self.descricao) + ")"
    
    
class Cliente(models.Model):
    nome = models.TextField(max_length=50)
    celular = models.TextField(max_length=11)
    
    def __str__(self):
        return self.nome
        

# class Oferece(models.Model):
#     servico = models.ForeignKey(Servico, on_delete=models.CASCADE)
#     profissional = models.ForeignKey(Profissional, on_delete=models.CASCADE)

#     def __str__(self):
#         return str(self.profissional) + " oferece " + str(self.servico)

class Agenda(models.Model):    
    servico = models.ForeignKey(Servico, on_delete=models.CASCADE)
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    horario = models.DateTimeField(unique=True)
    formaPagamento = models.ForeignKey(FormasDePagamento, on_delete=models.CASCADE)
    #profissional = models.ForeignKey(Profissional, on_delete=models.CASCADE, default=None)
    def __str__(self):
        return str(localtime(self.horario).strftime('%d de %b de %Y')) + ' | ' + self.cliente.nome + ' | ' + self.servico.servico
    

class FotosServico(models.Model):
    servico = models.ForeignKey(Servico, on_delete=models.CASCADE)
    foto = models.ImageField(upload_to='fotos/%d/%m/%Y/', blank=True)

# class Configuracoes(models.Model):
#     texto_inicial = models.CharField(max_length=140)
    