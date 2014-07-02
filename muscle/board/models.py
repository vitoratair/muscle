# coding: utf-8
from django.db import models
from django.utils.translation import ugettext_lazy as _

# Create your models here.

class Structure(models.Model):

    dataVersion = models.IntegerField(_(u'Versão'))
    timestamp = models.CharField(_('Timestamp'), max_length=8)
    dataFormat = models.IntegerField(_('Formato'))
    dataPayload = models.CharField(_('Payload'), max_length=100)
    mac = models.ForeignKey('User')
    dataType = models.ForeignKey('Type')

    class Meta:
		ordering = ['timestamp']
		verbose_name = _(u'Estrutura')
		verbose_name_plural = _(u'Estruturas')

    def __unicode__(self):
        return self.timestamp


class User(models.Model):

    mac = models.CharField(_(u'Mac'), primary_key=True, max_length=17)
    nome = models.CharField(_(u'Nome'), max_length=100, unique=True)

    class Meta:
        ordering = ['nome']
        verbose_name = _(u'Nome de usuário')
        verbose_name_plural = _(u'Nome de usuários')

    def __unicode__(self):
        return self.nome

class Type(models.Model):

    cod = models.IntegerField(_(u'Código'), primary_key=True)
    nome = models.CharField(_(u'Nome'), max_length=45)

    class Meta:
        ordering = ['cod']
        verbose_name = _(u'Tipo de dado')
        verbose_name_plural = _(u'Tipos de dados')

    def __unicode__(self):
        return self.nome