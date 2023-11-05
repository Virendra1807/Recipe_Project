from django.db import models
# This is for authentication
from django.contrib.auth.models import User


class Receipe(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    receipe_name = models.CharField(max_length=50, default="NA")
    receipe_desc = models.TextField(null=True , blank=True)
    receipe_img = models.ImageField(upload_to="receipe_folder",null=True , blank=True )

