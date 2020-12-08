from django.db import models

# Create your models here.
class List(models.Model):
    item = models.CharField(max_length=200)
    checked = models.BooleanField(default=False)

    def changeChecked(self):
        if self.checked:
            self.checked = False
        else:
            self.checked = True

    def __str__(self):
        return self.item + " | " + str(self.checked)