from __future__ import unicode_literals
from django.db import models
from django.utils.translation import ugettext as _
import random


def get_random_value(start=100, end=100000):
    def get_random():
        return random.randint(start, end) * 0.01
    return get_random


class Trader(models.Model):
    name = models.CharField(verbose_name=_('name'), max_length=128)
    balance = models.FloatField(verbose_name=_('balance'), default=get_random_value())

    class Meta:
        verbose_name = _('trader')
        verbose_name_plural = _('traders')
        ordering = ['-id']

    def __unicode__(self):
        return '<Trader: %s, %s>' % (self.id, self.name)


class Transaction(models.Model):
    trader = models.ForeignKey(Trader, verbose_name=_('trader'))
    time = models.DateTimeField(verbose_name=_('time'), auto_created=True)
    amount = models.FloatField(verbose_name=_('amount'), default=get_random_value())
    type = models.IntegerField(verbose_name=_('type'), default=1, db_index=True)

    class Meta:
        verbose_name = _('transaction')
        verbose_name_plural = _('transactions')
        ordering = ['-id']

    def __unicode__(self):
        return '<Transaction: %s, %s, %s, %s>' % (self.id, self.time, self.amount, self.trader_id)


class Deal(models.Model):
    trader = models.ForeignKey(Trader, verbose_name=_('trader'))
    time = models.DateTimeField(verbose_name=_('time'), db_index=True, auto_created=True)
    amount = models.FloatField(verbose_name=_('amount'), default=get_random_value())
    result_amount = models.FloatField(verbose_name=_('result amount'), default=get_random_value(-100000))

    class Meta:
        verbose_name = _('deal')
        verbose_name_plural = _('deals')
        ordering = ['-id']

    def __unicode__(self):
        return '<Deal: %s, %s, %s, %s>' % (self.id, self.time, self.amount, self.trader_id)