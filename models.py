from django.db import models
from django.conf import settings

CATEGORY_CHOICES = [
    ('Food','Food'),
    ('Travel','Travel'),
    ('Bills','Bills'),
    ('Shopping','Shopping'),
    ('Entertainment','Entertainment'),
    ('Health','Health'),
    ('Other','Other'),
]

class Expense(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='expenses')
    description = models.CharField(max_length=255)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    date = models.DateField()
    category = models.CharField(max_length=30, choices=CATEGORY_CHOICES, default='Other')
    notes = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-date', '-created_at']

    def __str__(self):
        return f"{self.description} - {self.amount}"    