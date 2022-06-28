from django.contrib import admin
from .models import *
# Register your models here.
admin.site.register(Profile)
admin.site.register(Element)
#admin.site.register(TOS)


# To Display TOS Edits inline when Viewwing their respective TOS
class EditInlineAdmin(admin.TabularInline):
    model = Edit

class TOSEditAdmin(admin.ModelAdmin):
    inlines = [EditInlineAdmin]

admin.site.register(TOS, TOSEditAdmin)

@admin.register(Edit)
class EditAdmin(admin.ModelAdmin):
    """ Approve or Reject selected edits """
    actions = [
            'approve',
            'reject',
    ]
    def approve(self, request, queryset):
        queryset.update(status='Approved')
        for edit in queryset:
            tos = TOS.objects.get(pk=edit.tos_id)
            e = edit.element
            sentence = edit.text

            tos.elements.add(e, through_defaults={
                'associatedText':sentence
            })
            tos.save()
    approve.short_description = 'Approve Selected'

    def reject(self, request, queryset):
        for edit in queryset:
            edit.status = 'Rejected'
            edit.save(update_fields=['status'])
    reject.short_description = 'Reject Selected'

"""
    This function allows for deletion of elementTexts and will update the auto
    ranking score after deletion. 
"""
@admin.action(description = 'Delete elements for one TOS and reset weight')
def deleteElementText(modeladmin, request, queryset):
    allElement = Element.objects.all()
    # allText = ElementText.objects.filter(tos = instance) 
    # filter to get all elements in tos
    tosElements =  allElement.filter(tos = queryset[0].tos)
    queryElements = queryset.values_list('element', flat = True)
    excluded = tosElements.exclude(id__in = queryElements)
    weights = excluded.values_list('weight', flat = True)
    # get absolute weight
        
    absTotal = sum(abs(w) for w in weights) 
    regTotal = sum(weights)
    # get total
    total = absTotal + regTotal 
    # set rating
    TOS.objects.filter(pk=queryset[0].tos.pk).update(weightRating = round((total / absTotal) * 100))
    queryset.delete()

class ElementTextAdmin(admin.ModelAdmin):
    actions = [deleteElementText]

admin.site.register(ElementText, ElementTextAdmin)
