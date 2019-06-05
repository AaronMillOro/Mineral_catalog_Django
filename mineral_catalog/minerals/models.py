from django.db import models


class Mineral(models.Model):
    name = models.CharField(max_length=255)
    image_filename = models.FilePathField(path='/img')
    image_caption = models.TextField()
    category = models.CharField(max_length=255)
    formula = models.TextField()
    strunz_classification = models.TextField()
    crystal_system = models.CharField(max_length=255)
    unit_cell = models.TextField()
    color = models.CharField(max_length=255)
    crystal_symmetry = models.TextField()
    cleavage = models.TextField()
    mohs_scale_hardness = models.TextField()
    luster = models.TextField()
    streak = models.TextField()
    diaphaneity = models.CharField(max_length=255)
    optical_properties = models.TextField()
    refractive_index = models.TextField()
    crystal_habit = models.TextField()
    specific_gravity = models.TextField()
    group = models.CharField(max_length=255)
