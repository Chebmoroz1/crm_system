from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

class Organization(models.Model):
    name = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return self.name

class Project(models.Model):
    name = models.CharField(max_length=255)
    contract_amount = models.DecimalField(max_digits=12, decimal_places=2)
    shipping_date = models.DateField(null=True, blank=True)
    customer = models.ForeignKey(Organization, on_delete=models.PROTECT, related_name='customer_projects')
    executor_company = models.ForeignKey(Organization, on_delete=models.PROTECT, related_name='executor_projects')

    def __str__(self):
        return self.name

class Person(models.Model):
    name = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return self.name

class CashExpense(models.Model):
    class ExpenseType(models.TextChoices):
        CASH = 'CASH', 'Наличные'
        NO_VAT = 'NO_VAT', 'Без НДС'
        VAT = 'VAT', 'С НДС'

    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    person = models.ForeignKey(Person, on_delete=models.PROTECT)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    expense_type = models.CharField(max_length=10, choices=ExpenseType.choices, default=ExpenseType.CASH)
    date = models.DateField()
    comment = models.TextField(blank=True)

    def __str__(self):
        return f'{self.amount} для {self.person.name}'

class Attachment(models.Model):
    file = models.FileField(upload_to='attachments/')
    project = models.ForeignKey(Project, on_delete=models.CASCADE, null=True, blank=True)
    expense = models.ForeignKey(CashExpense, on_delete=models.CASCADE, null=True, blank=True)
    uploaded_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    uploaded_at = models.DateTimeField(auto_now_add=True)

class Note(models.Model):
    content = models.TextField()
    project = models.ForeignKey(Project, on_delete=models.CASCADE, null=True, blank=True)
    expense = models.ForeignKey(CashExpense, on_delete=models.CASCADE, null=True, blank=True)
    created_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

class ActivityLog(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    action = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    related_project = models.ForeignKey(Project, on_delete=models.SET_NULL, null=True, blank=True)
    related_expense = models.ForeignKey(CashExpense, on_delete=models.SET_NULL, null=True, blank=True)
