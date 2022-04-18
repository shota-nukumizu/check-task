from django.db import models

PRIORITY_PROPERTIES = (
    ('highlight', 'highlight'),
    ('middle', 'middle'),
    ('low', 'low'),
)

class Task(models.Model):
    title = models.CharField(max_length=50)
    content = models.TextField(blank=True)
    priority = models.CharField(max_length=15, choices=PRIORITY_PROPERTIES)
    created = models.DateField(auto_now=True)
    due = models.DateField()
    done = models.BooleanField(default=False)
