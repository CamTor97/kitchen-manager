from .models import Purchase
from django.db.models import Sum, F
class CalculatedVariablesMixin:
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Calculating Total Revenue
        total_revenue = Purchase.objects.aggregate(
            total=Sum("menu_item__price")
        )["total"] or 0
        # Calculating Total Costs
        total_cost = Purchase.objects.aggregate(
            total=Sum(
                F("menu_item__requirements__quantity_needed") *
                F("menu_item__requirements__ingredient__unit_price")
            )
        )["total"] or 0
        # Calculating Total Profit
        total_profit = total_revenue - total_cost
        # Updating context
        context.update({
            "total_revenue": total_revenue,
            "total_cost": total_cost,
            "total_profit": total_profit,
        })
        return context