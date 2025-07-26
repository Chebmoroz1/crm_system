from django.db import models

class Project(models.Model):
    name = models.CharField(max_length=255)

class CashExpense(models.Model):
    TYPE_CHOICES = [
        ('CASH', 'Наличные'),
        ('NO_VAT', 'Без НДС'),
        ('VAT', 'С НДС')
    ]
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    expense_type = models.CharField(max_length=10, choices=TYPE_CHOICES, default='CASH')
    date = models.DateField()
    person = models.CharField(max_length=255)

class Person(models.Model):
    name = models.CharField(max_length=255)

class Attachment(models.Model):
    file = models.FileField(upload_to='attachments/')
    uploaded_at = models.DateTimeField(auto_now_add=True)

class Note(models.Model):
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

class ActivityLog(models.Model):
    action = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)

class Organization(models.Model):
    name = models.CharField(max_length=255)
    inn = models.CharField(max_length=12)
