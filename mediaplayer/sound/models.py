from django.db import models

class Sound(models.Model):
        title = models.TextField()
        image = models.ImageField(blank=True)
        audio_file = models.FileField(blank=True, null=True)
        audio_file2 = models.FileField(blank=True, null=True)
        audio_file3 = models.FileField(blank=True, null=True)
        audio_file4 = models.FileField(blank=True, null=True)
        audio_file5 = models.FileField(blank=True, null=True)
        audio_file6 = models.FileField(blank=True, null=True)
        audio_file7 = models.FileField(blank=True, null=True)
        audio_file8 = models.FileField(blank=True, null=True)
        audio_file9 = models.FileField(blank=True, null=True)
        audio_link = models.CharField(max_length=200, blank=True, null=True)
        duration = models.CharField(max_length=20)
        paginate_by = 2

        def __str__(self):
            return self.title

