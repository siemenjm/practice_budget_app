from django.db import models

class Institution(models.Model):
    institution_id = models.CharField(max_length=100)
    name = models.CharField(max_length=250)
    logo = models.URLField(max_length=500)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['institution_id']
