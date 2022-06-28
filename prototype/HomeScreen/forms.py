from django import forms
from .models import TOS
from .models import Edit
from django.forms.models import inlineformset_factory 
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username',
                  'email', 'password1', 'password2']

class CompareForm(forms.Form):
    selected_toses = forms.ModelMultipleChoiceField(
        label = 'TOS Name',
        widget = forms.CheckboxSelectMultiple,
        queryset = TOS.objects.all()#filter(status = 'Approved').order_by('category','name')
    )

class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'email']
        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'first_name': forms.TextInput(attrs={'class': 'form-control'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control'})
        }

    # def __init__(self, *args, **kwargs):
    #     super(UserUpdateForm, self).__init__(*args, **kwargs)
    #     self.fields['first_name'].required = False
    #     self.fields['last_name'].required = False
    #     self.fields['email'].required = False
    #     self.fields['username'].required = False

# calendar for date input
class DateInput(forms.DateInput):
    input_type = 'date'


class TOSForm(forms.ModelForm):
    class Meta:
        model = TOS
        fields = ['name', 'fullText', 'date', 'category']
        widgets = {
            'date': DateInput()
        }

    def clean_name(self):
        name = self.cleaned_data.get('name')
        if TOS.objects.filter(name=name).exists():
            raise forms.ValidationError('TOS Already Exists!')
        return name

# TOS Edit Form
class EditForm(forms.ModelForm):
    class Meta:
        model = Edit
        fields = ['element', 'category', 'text']

# For making Edit forms with Formset rather than htmx
EditFormSet = inlineformset_factory(
        TOS,
        Edit,
        EditForm,
        can_delete=True,
        min_num=1,
        extra=0
)

class RankingForm(forms.Form):
    c = ([(i,i) for i in range(1,101)]) 
    ranking = forms.ChoiceField(choices = c) 