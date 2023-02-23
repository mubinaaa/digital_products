from django.db import models
from django.utils.translation import ugettext_lazy as _
# Create your models here.

class Category(models.Model):
    Parent = models.ForignKey('self',verbose_name = _('Parent'),blank=True,null=True,on_delete=models.CASCADE)
    title = models.CharField(_('Title'),max_length=50)
    description = models.TextField(_('Description'),blank=True)
    avatar = models.ImageField(_('Avatar'),blank=True,upload_to='categories')
    is_enable = models.BooleanField(_('Is Enable'),default=True)
    created_time = models.DateTimeField(_('Created Time'),auto_now_add=True)
    updated_time = models.DateTimeField(_('Updated Time'),auto_now=True)

    #The name of table in database
    class Meta:
        db_table = 'categories'
        verbose_name = _('Category')
        verbose_name_plural = _('Categories')



class Product(models.Model):
    title = models.CharField(_('Title'), max_length=50)
    description = models.TextField(_('Description'), blank=True)
    avatar = models.ImageField(_('Avatar'), blank=True, upload_to='categories')
    is_enable = models.BooleanField(_('Is Enable'), default=True)
    created_time = models.DateTimeField(_('Created Time'), auto_now_add=True)
    updated_time = models.DateTimeField(_('Updated Time'), auto_now=True)

    # The name of table in database
    class Meta:
        db_table = 'Product'
        verbose_name = _('Product')
        verbose_name_plural = _('Products')


class File(models.Model):
    pass