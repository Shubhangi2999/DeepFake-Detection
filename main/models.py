from django.db import models

class Video(models.Model):
    name = models.CharField(max_length=500)
    videofile = models.FileField(upload_to='videos/', verbose_name="")

    def __str__(self):
        return str(self.videofile)