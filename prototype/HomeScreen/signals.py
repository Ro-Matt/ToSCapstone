# signals.py is used to automatically generate methods after an object is saved
from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.dispatch import receiver
from .models import * 

"""
When user is saved, send signal to create profile.

arguments: instance is user that created profile


"""

@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)


@receiver(post_save, sender=User)
def save_profile(sender, instance, created, **kwargs):
    instance.profile.save()

@receiver(post_save, sender = TOS)
def updateWeight(sender, instance, **kwargs):
    allElement = Element.objects.all()
    # allText = ElementText.objects.filter(tos = instance) 
    # filter to get all elements in tos
    tosElements =  allElement.filter(tos = instance.id)
    if tosElements.exists():
        weights = tosElements.values_list('weight', flat = True)
        # get absolute weight
            
        absTotal = sum(abs(w) for w in weights) 
        regTotal = sum(weights)
        # get total
        total = absTotal + regTotal 
        # set rating
        TOS.objects.filter(pk=instance.pk).update(weightRating = round((total / absTotal) * 100))