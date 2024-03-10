from django.db import models

CATEGORY = (('business', 'ビジネス'), ('life','生活'), ('other','その他'))

class Rebels(models.Model):
    titlle = models.CharField(max_length=100)
    text = models.TextField()
    number = models.ImageField(
        max_length=100,
        choices = CATEGORY
    )


    def __str__(self):
        return self.titlle