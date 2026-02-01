from django.db import models
from django.conf import settings
# Create your models here.

class JobApplications(models.Model):
  STATUS_CHOICES = [
    ('applied', 'Applied'),
    ('interview','Interview'),
    ('offer','Offer'),
    ('rejected','Rejected'),
  ]

  user = models.ForeignKey(settings.AUTH_USER_MODEL,
                           on_delete=models.CASCADE,
                           related_name="application")

  company_name = models.CharField(max_length=200)
  role=models.CharField(max_length=200)
  status = models.CharField(max_length=20 , choices=STATUS_CHOICES,default='applied')
  appliced_date = models.DateTimeField(auto_now_add=True)
  notes = models.TextField(blank=True)
  created_at = models.DateTimeField(auto_now_add=True)

  def __str__(self):
    return f"{self.company_name} - {self.role}"