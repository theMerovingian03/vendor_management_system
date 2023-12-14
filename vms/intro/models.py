from django.db import models

# Create your models here.

class APIs(models.Model):
    api_title = models.CharField(max_length=100)
    api_desc = models.TextField(max_length=200)
    api_url = models.CharField(max_length=100)
    api_method = models.CharField(max_length=7)
    api_params = models.TextField(max_length=150)

    class Meta:
        verbose_name = "API"
        verbose_name_plural = "APIs"
        
    def __str__(self):
        return f"{self.api_title}"