from django.db import models

from django.contrib.auth.models import User
from django.db import models
# Register your models here.


def user_directory_path(instance, filename):
        # file will be uploaded to MEDIA_ROOT/user_<id>/<filename>
        return 'user_{0}/{1}'.format(instance.user.id, filename)

class Document(models.Model):
    name = models.CharField(max_length=200, help_text = 'name of document')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    


class Scheme(models.Model):
    name = models.CharField(max_length=200, help_text='name of scheme')
    documents = models.ManyToManyField(Document)
    
