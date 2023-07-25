from django import forms
from django.core.exceptions import ValidationError
from django.forms import ModelForm
from .models import Store, Product, OperatingHours, User, Business, SiteConfiguration, Imagem
from captcha.fields import CaptchaField
from django.contrib.auth.forms import SetPasswordForm
from django.utils.translation import gettext_lazy as _


class NewStoreForm(ModelForm):
    class Meta:
        model = Store
        fields = '__all__'


class ProductsForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['store', 'name', 'description', 'image']
        widgets = {
            'store': forms.Select(attrs={'class': 'form-select'}),
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'rows': 4}),
            'image': forms.ClearableFileInput(attrs={'class': 'form-control'}),
        }

    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user')
        super().__init__(*args, **kwargs)
        if not user.is_superuser and not user.role == "ADMIN":
            self.fields['store'].queryset = Store.objects.filter(user=user)


class ContactForm(forms.Form):
    name = forms.CharField(max_length=100,
                           widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nome Sobrenome'}),
                           label='Nome')
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'email@email.com'}),
                             label='Email')
    subject = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'}), label='Assunto')
    message = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control'}), label='Mensagem')
    captcha = CaptchaField(label='')


class ChangePassword(forms.Form):
    new_password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    new_password_confirmation = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control'}))


class StoreForm(forms.ModelForm):
    class Meta:
        model = Store
        fields = ['store_num', 'image', 'brand', 'business', 'phoneNum', 'email', 'description', 'facebookLink',
                  'instagramLink', 'linkedinLink', 'twitterLink', 'websiteLink', 'user']


class OperatingHoursForm(forms.ModelForm):
    class Meta:
        model = OperatingHours
        fields = ['weekday', 'opening_time', 'closing_time', 'lunch_start_time', 'lunch_end_time']
        widgets = {
            'weekday': forms.HiddenInput(),
            'opening_time': forms.TimeInput(attrs={'type': 'time'}),
            'closing_time': forms.TimeInput(attrs={'type': 'time'}),
            'lunch_start_time': forms.TimeInput(attrs={'type': 'time'}),
            'lunch_end_time': forms.TimeInput(attrs={'type': 'time'}),
        }


class BusinessForm(forms.ModelForm):
    class Meta:
        model = Business
        fields = ['business']
        labels = {
            'business': '',
        }
        widgets = {
            'business': forms.TextInput(attrs={'placeholder': 'Ramo de Atividade'}),
        }


class SiteConfigurationForm(forms.ModelForm):
    class Meta:
        model = SiteConfiguration
        fields = ('logo', 'description','facebookLink','instagramLink')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Remove the required attribute for individual fields
        self.fields['logo'].required = False
        self.fields['description'].required = False
        self.fields['facebookLink'].required = False
        self.fields['instagramLink'].required = False

class ImagemForm(forms.ModelForm):
    class Meta:
        model = Imagem
        fields = ['imagem']