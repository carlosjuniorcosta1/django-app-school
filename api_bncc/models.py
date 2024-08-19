from django.db import models
from django.core.exceptions import ValidationError
from django.core.validators import FileExtensionValidator
import os
from accounts.models import CustomUser as User


class ElementarySchoolBncc(models.Model):
    cur_comp_choices = [
        ('arte', 'Arte'),
        ('geografia', 'Geografia'),
        ('historia', 'História'),
        ('lingua_portuguesa', 'Língua Portuguesa'),
        ('lingua_inglesa', 'Língua Inglesa'),
        ('educacao_fisica', 'Educação Física'),
        ('ciencias', 'Ciências'),
        ('ensino_religioso', 'Ensino Religioso'),
        ('matematica', 'Matemática')]
    cur_comp = models.CharField(max_length=40, choices=cur_comp_choices, blank=True, null=True)
    thema_unities = models.CharField(max_length=90, null=True, blank=True)    
    k_obj = models.CharField(max_length=510, null=True, blank=True)
    whole_skill = models.CharField(max_length=1610, null=True)
    cod_skill = models.CharField(max_length=10, null=True)
    skill = models.CharField(max_length=1610)
    field_act = models.CharField(max_length=40, null=True, blank=True)
    lang_prac = models.CharField(max_length=150, null=True, blank=True)
    axis = models.CharField(max_length=40, null=True, blank=True)
    es1 = models.BooleanField()
    es2 = models.BooleanField()
    es3 = models.BooleanField()
    es4 = models.BooleanField()
    es5 = models.BooleanField()
    es6 = models.BooleanField()
    es7 = models.BooleanField()
    es8 = models.BooleanField()
    es9 = models.BooleanField()
       
    def __str__(self):
        return self.get_cur_comp_display()
    
    def get_cur_comp_db(self):
       return self.cur_comp
        
    
class HighSchoolBncc(models.Model):
    cur_comp_choices = [
        ('linguagens', 'Linguagens'),
        ('matematica', 'Matemática'),
        ('lingua_portuguesa', 'Língua Portuguesa'),
        ('ciencias_humanas', 'Ciências Humanas'),
        ('ciencias_da_natureza', 'Ciências da Natureza')]

    cur_comp = models.CharField(max_length=40, choices=cur_comp_choices, blank=True, null=True)

    whole_skill = models.CharField(max_length=1610, null=True)
    cod_skill = models.CharField(max_length=10, null=True)
    skill = models.CharField(max_length=1610)
    field_act = models.CharField(max_length=40, null=True, blank=True)
    es10 = models.BooleanField(blank=True, null=True)
    es11 = models.BooleanField(blank=True, null=True)
    es12 = models.BooleanField(blank=True, null=True)
    
    def __str__(self):
        return f'{self.get_cur_comp_display()}, {self.skill[:100]}'
    


    




    




