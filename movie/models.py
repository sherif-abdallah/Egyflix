from django.db import models
import datetime



CATEGORY_CHOICES = (
    ('ACTION', 'ACTION'),
    ('DRAMA', 'DRAMA'),
    ('COMEDY', 'COMEDY'),
    ('ROMANCE', 'ROMANCE'),
    ('ADVENTURE', 'ADVENTURE'),
)

LANGUAGE_CHOICES = (
    ('ENGLISH', 'ENGLISH'),
    ('ARABIC', 'ARABIC'),
    ('Asian', 'Asian')
)

STATUS_CHOICES = (
    ('TRENDS', 'TRENDS'),
    ('RECENTLY ADDED', 'RECENTLY ADDED'),
    ('MOST WATCHED', 'MOST WATCHED'),
    ('TOP RATED', 'TOP RATED'),

)


year = datetime.datetime.now()
year = year.year
year = int(year)


# Create your models here.



class Movie(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to ='')
    category = models.CharField(max_length=100 ,choices=CATEGORY_CHOICES )
    language = models.CharField(choices=LANGUAGE_CHOICES, max_length=100)
    status = models.CharField(choices=STATUS_CHOICES, max_length=100)
    came_out = models.IntegerField(default=year)
    blog_view = models.IntegerField(default=0)

    # Servers
    video = models.URLField()
    download_link = models.URLField()




    def __str__(self):
        return self.title



