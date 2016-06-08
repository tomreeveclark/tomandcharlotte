from __future__ import unicode_literals

from django.db import models
from django.utils.text import slugify
from imagekit.models import ProcessedImageField
from imagekit.processors import ResizeToFill

# Create your models here.
class Image(models.Model):
	image = ProcessedImageField(upload_to='images',
	                           #processors=[ResizeToFill(800,)],
	                           format='JPEG',
	                           options={'quality': 50})
	location = models.CharField(max_length=200)
	date = models.DateField(auto_now_add = True, blank = True)
	time = models.TimeField(auto_now_add = True, blank = True)
	latitude = models.DecimalField(max_digits=10, decimal_places=7, blank=True, null = True)
	longitude = models.DecimalField(max_digits=10, decimal_places=7, blank=True, null = True)
	shutter = models.CharField(max_length = 10, blank = True)
	aperture = models.CharField(max_length = 10, blank = True)
	iso = models.CharField(max_length = 10, blank = True)
	slug = models.SlugField(null=True, blank=True)

	def __str__(self):
		return self.location + ' ' +  str(self.date) + ' ' + str(self.latitude) + ' ' + str(self.longitude) + ' ' + str(self.shutter) + ' ' + str(self.aperture) + ' ' + str(self.iso)

	def save(self, *args, **kwargs):
		# For automatic slug generation.
		if not self.slug:
			self.slug = slugify(self.location+str(self.latitude)+str(self.longitude))

		return super(Image, self).save(*args, **kwargs)