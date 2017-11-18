from django.db import models


class URL(models.Model):
	app_label = "url_short_mvc"

	full_url = models.CharField(max_length=200)
	short_url = models.CharField(max_length=200)
	url_short_id = models.CharField(max_length=200)

	@staticmethod
	def get_full_url(short_id):
		objects = URL.objects.get(url_short_id=short_id)
		return objects.full_url