import datetime

from django import forms

from dogs.models import Dog
from users.forms import StyleFormMixin


class DogForm(StyleFormMixin, forms.ModelForm):
    class Meta:
        model = Dog
        exclude = ('owner',)

    def clean_birth_date(self):
        cleaned_data = self.cleaned_data['birth_date']
        if cleaned_data is None:
            return None
        now_year = datetime.datetime.now().year
        if now_year - cleaned_data.year > 100:
            raise forms.ValidationError('Собака должна быть моложе 100 лет')
        return cleaned_data


# class DogCreateUpdateForm(StyleFormMixin, forms.ModelForm):
#     class Meta:
#         model = Dog
#         exclude = ('owner',)
