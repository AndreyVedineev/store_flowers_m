from django import forms

from flowers.models import Flowers


class FlowersForm(forms.ModelForm):
    class Meta:
        model = Flowers
        # fields = '__all__'
        exclude = ('date_of_creation', 'last_modified_date',)

    def clean_name(self):
        bad = {'казино', 'криптовалюта', 'крипта', 'биржа', 'дешево', 'бесплатно', 'обман', 'полиция',
               'радар'}
        cleaned_data = self.cleaned_data['name']
        words_name = cleaned_data.lower().split()
        if bad & set(words_name):
            raise forms.ValidationError(f'Вы используете запрещенные слова! {bad}')

        return cleaned_data