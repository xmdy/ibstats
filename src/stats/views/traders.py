from django.db.models import Sum
from django.shortcuts import redirect
from django.urls import reverse
from django.utils import timezone
from django.views.generic import ListView

from stats.models import Trader, Deal, Transaction


class TradersStatsView(ListView):
    model = Trader
    paginate_by = 1000

    def get(self, request, *args, **kwargs):
        today = timezone.datetime.today()

        if 'year' not in kwargs:
            kw = {'year': today.year, 'month': today.month, 'day': today.day}
            return redirect(reverse('traders', kwargs=kw))

        self.year = int(kwargs.get('year', today.year))
        self.month = int(kwargs.get('month', today.month))
        self.day = int(kwargs.get('day', today.day))

        self.day_start = timezone.datetime(self.year, self.month, day=self.day, hour=0, minute=0, second=0)
        self.day_end = timezone.datetime(self.year, self.month, day=self.day, hour=23, minute=59, second=59)

        self.today_deals = self.get_deals_qs()

        return super(TradersStatsView, self).get(request, *args, **kwargs)

    def get_deals_qs(self):
        return Deal.objects.filter(time__gte=self.day_start, time__lte=self.day_end).order_by()

    def get_queryset(self):
        return self.model.objects.filter(id__in=self.today_deals.values_list('trader_id'))

    def get_today_profit(self):
        deals = self.get_deals_qs()\
            .values_list('trader_id')\
            .annotate(today_profit=Sum('result_amount')).order_by()
        return dict(deals)

    def get_total_profit(self, traders_id_list):
        deals = Deal.objects\
            .filter(trader_id__in=traders_id_list)\
            .values_list('trader_id')\
            .annotate(total_profit=Sum('result_amount')).order_by()
        return dict(deals)

    def get_total_deposit(self, traders_id_list):
        transactions = Transaction.objects\
            .filter(trader_id__in=traders_id_list, type=1)\
            .values_list('trader_id')\
            .annotate(total_deposit=Sum('amount')).order_by()
        return dict(transactions)

    def get_today_stat(self):
        return self.get_deals_qs()\
            .aggregate(today_volume=Sum('amount'), today_result=Sum('result_amount'))

    def get_context_data(self, **kwargs):
        super_ctx = super(TradersStatsView, self).get_context_data()

        traders_obj_list = super_ctx['object_list']
        traders_id_qs = traders_obj_list.values_list('id')

        today_profit = self.get_today_profit()
        total_profit = self.get_total_profit(traders_id_qs)
        total_deposit = self.get_total_deposit(traders_id_qs)

        for obj in traders_obj_list:
            obj.today_profit = today_profit.get(obj.pk, 0)
            obj.total_profit = total_profit.get(obj.pk, 0)
            obj.total_deposit = total_deposit.get(obj.pk, 0)

        super_ctx['stats'] = self.get_today_stat()
        super_ctx['today'] = self.day_start

        return super_ctx

    def get_template_names(self):
        return ['stats/traders/traders_list.html']