from django.shortcuts import render
from .models import CashExpense, Project, Person
from django.db.models import Q

def cash_expenses_list(request):
    project_id = request.GET.get("project")
    person_id = request.GET.get("person")
    date_from = request.GET.get("date_from")
    date_to = request.GET.get("date_to")

    expenses = CashExpense.objects.select_related("project", "person").all()

    if project_id:
        expenses = expenses.filter(project_id=project_id)
    if person_id:
        expenses = expenses.filter(person_id=person_id)
    if date_from:
        expenses = expenses.filter(date__gte=date_from)
    if date_to:
        expenses = expenses.filter(date__lte=date_to)

    context = {
        "expenses": expenses,
        "projects": Project.objects.all(),
        "persons": Person.objects.all(),
        "selected_project": project_id,
        "selected_person": person_id,
        "date_from": date_from,
        "date_to": date_to,
    }
    return render(request, "projects/cash_expenses_list.html", context)
