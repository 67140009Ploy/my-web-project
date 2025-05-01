from django.db import models

class Transaction(models.Model):
    TYPE_CHOICES = (
        ('income', 'รายรับ'),
        ('expense', 'รายจ่าย'),
    )

    title = models.CharField(max_length=100)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    transaction_type = models.CharField(max_length=10, choices=TYPE_CHOICES)
    date = models.DateField(auto_now_add=False)

    def __str__(self):
        return f"{self.title} - {self.amount}"