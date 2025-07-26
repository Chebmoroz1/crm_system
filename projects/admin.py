from django.contrib import admin
from .models import Project, CashExpense, Person, Attachment, Note, ActivityLog, Organization

admin.site.register(Project)
admin.site.register(CashExpense)
admin.site.register(Person)
admin.site.register(Attachment)
admin.site.register(Note)
admin.site.register(ActivityLog)
admin.site.register(Organization)
