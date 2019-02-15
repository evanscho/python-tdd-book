from django.db import models
from django.conf import settings
from django.core.urlresolvers import reverse

class List(models.Model):
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='lists_owned', blank=True, null=True)
    shared_with = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='lists_shared_with_me')

    @property
    def name(self):
        return self.item_set.first().text
    

    def get_absolute_url(self):
        return reverse('view_list', args=[self.id])

    @staticmethod
    def create_new(first_item_text, owner=None):
        list_ = List.objects.create(owner=owner)
        new_item = Item.objects.create(text=first_item_text, list=list_)
        return list_

#    def shared_with.add(email):
#        self.shared_with

class Item(models.Model):
    text = models.TextField(default='')
    list = models.ForeignKey(List, default=None)

    class Meta:
        ordering = ('id',)
        unique_together = ('list', 'text')

    def __str__(self):
        return self.text