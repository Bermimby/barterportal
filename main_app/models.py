from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User

TRADE_STATUS=(
    ('1','Proposed'),
    ('2','Approved'),
    ('3','Denied')
)
# Create your models here.

class Item(models.Model):
    name=models.CharField(max_length=150)
    description=models.CharField(max_length=500)
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    
    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('items_myitems')
    
class Trade(models.Model):
    item_primary=models.ForeignKey(Item, related_name="trade_primary", on_delete=models.CASCADE)
    item_proposed=models.ForeignKey(Item, related_name="trade_proposed", on_delete=models.CASCADE)
    status=models.CharField(
        max_length=1,
        choices=TRADE_STATUS,
        default=TRADE_STATUS[0][0]
    )
    def __str__(self):
        return f"trade {self.primary_item} for {self.proposed_item}"
    

