# coding: utf-8
from django.db import models
from django.utils.translation import ugettext_lazy as _

# Create your models here.

class Structure(models.Model):

    dataVersion = models.IntegerField(_(u'Versão'))
    timestamp = models.CharField(_('Timestamp'), max_length=8)
    dataType = models.IntegerField(_('Tipo'))
    dataFormat = models.IntegerField(_('Formato'))
    dataPayload = models.CharField(_('Payload'), max_length=100)

    class Meta:
		ordering = ['timestamp']
		verbose_name = _(u'Estrutura')
		verbose_name_plural = _(u'Estruturas')

    def __unicode__(self):
        return self.timestamp

