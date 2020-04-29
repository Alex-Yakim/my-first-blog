from django.db import models

# Create your models here.
class Testimonials(models.Model):
    text = models.TextField()
    #photo = models.ImageField()
    name = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    date = models.DateField()

    #def publish(self):
        #self.save()

    def __str__(self):
        return self.text
