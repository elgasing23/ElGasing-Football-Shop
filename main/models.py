import uuid
from django.db import models

class Item(models.Model):
    CATEGORY_CHOICES = [
        ('ball', 'Ball'),
        ('shoes', 'Shoes'),
        ('shocks', 'Shocks'),
        ('jersey', 'Jersey'),
        ('other', 'Other'),
    ]

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=255)  
    price = models.IntegerField() 
    description = models.TextField()  
    thumbnail = models.URLField(blank=True, null=True)  
    category = models.CharField(max_length=50, choices=CATEGORY_CHOICES, default='other')
    is_featured = models.BooleanField(default=False)  
    created_at = models.DateTimeField(auto_now_add=True)
    items_views = models.PositiveBigIntegerField(default=0)

    def __str__(self):
        return f"{self.name} - Rp{self.price:,}"
    
    @property
    def is_items_hot(self):
        return self.items_views > 20
        
    def increment_views(self):
        self.items_views += 1
        self.save()
