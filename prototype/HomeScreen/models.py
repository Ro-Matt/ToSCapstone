# TODO: Database Setup with models below
# Admin rights to us all or just a shared account
# User registrations
# manually input all elements (description, explanation, weight, category never to be changed)
# Lab 2 Outline
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

class Profile(models.Model):
    """
    This class hold information for the community member. Name of user, email, contributions are stored.

    """
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    contributions = models.FloatField(default=0)
    # image = models.ImageField(
    #     default='staticfiles/img/dogs/image2.jpeg', upload_to='profile_pics')

    def __str__(self):
        return f'{self.user.username} Profile'

class Element(models.Model):
    """
    This class holds information for an indivdual element of a TOS. The description

    Args:
        models (_type_): _description_

    Returns:
        _type_: _description_
    """
    CATEGORY = (
        ('Ownership', 'Ownership'),
        ('Privacy/Data', 'Privacy/Data')
    )

    description = models.CharField(max_length=200, null=True)
    explanation = models.CharField(max_length=500, null=True)
    weight = models.FloatField(null=True)
    category = models.CharField(max_length=15, null=False, choices=CATEGORY)

    #order must remain same for bot to work correctly
    class Meta:
        ordering = ['pk']

    def __str__(self):
        return self.description

class TOS(models.Model):
    # type of TO
    CATEGORY = (
        ('Social Media', 'Social Media'),
        ('Streaming', 'Streaming'),
        ('News', 'News'),
        ('Shopping', 'Shopping'),
        ('Finance', 'Finance'),
        ('Misc', 'Misc'),
    )
    STATUS = (
        ('Approved', 'Approved'),
        ('Pending', 'Pending'),
        ('Rejected', 'Rejected'),
    )
    name = models.CharField('Name of Service', max_length=50,
                            unique=True, blank=False)
    elements = models.ManyToManyField(Element, through='ElementText')
    date = models.DateTimeField('Date of Last Update', null=True, blank=False)
    #bot rating
    weightRating = models.FloatField(null=True)
    #overall community rating for user input
    communityRating = models.FloatField(null=True)
    category = models.CharField(max_length=20, null=True, choices=CATEGORY)
    fullText = models.TextField('Text', null=True, blank=False)
    status = models.CharField(max_length=20, default='Pending', choices=STATUS)
    author = models.ForeignKey(User, null = True, on_delete=models.RESTRICT)
    outOfDate = models.BooleanField(default=False)
    communityCount = models.IntegerField(default=0)
    def __str__(self):
        return self.name

    @property
    def getByCategory(self):
        return TOS.objects.filter(category=self.category)

class Edit(models.Model):
    #current status of edit, inital = Pending -> changed by admin to 'accept' or 'reject'
    STATUS = [
        ('Accepted', 'Accepted'),
        ('Rejected', 'Rejected'),
        ('Pending', 'Pending')
    ]
    status = models.CharField(max_length=9, choices=STATUS, default="Pending")

    # Category of Element being Edited
    ELEMENT_EDIT_CATEGORIES = [
            ('PD', 'Privacy/Data'),
            ('O', 'Ownership'),
    ]
    category = models.CharField(max_length=2, choices=ELEMENT_EDIT_CATEGORIES, default = 'PD')
    
    # The TOS for which the Edit is for
    tos = models.ForeignKey(TOS, null=True, on_delete=models.CASCADE)
    
    #element associated with the edit, RESTRICT - element can be deleted if edit is being deleted
    element = models.ForeignKey(Element, null=True, on_delete=models.RESTRICT)

    #user associated with edit, RESTRICT - author can be deleted if edit is also being deleted
    author = models.ForeignKey(User, null=True, on_delete=models.RESTRICT)

    #text associated with the edit
    text = models.TextField(blank=True)

    #add date and time auto
    date_added = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return 'User: {}, Id: {}, {}'.format(self.author.username, self.id, self.date_added)

#additional field for text with element
class ElementText(models.Model):
    element = models.ForeignKey(Element, on_delete=models.CASCADE)
    tos = models.ForeignKey(TOS, on_delete=models.CASCADE)
    associatedText = models.CharField(max_length=500, blank=True)
    #cannot have multiple of same element for same tos
    class Meta:
        unique_together = [['element', 'tos']]

    def __str__(self):
        return 'TOS: {} {}'.format(self.tos.name, self.element.description)
