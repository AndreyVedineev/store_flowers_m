from django import forms

from flowers.models import Flowers, Version


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


class VersionForm(forms.ModelForm):
    class Meta:
        model = Version
        fields = '__all__'

    def clean(self):
        # super().clean()
        count = 0
        cleaned_date = self.cleaned_data
        cleaned_data = self.cleaned_data['indicator']
        if cleaned_data is True:

            count += 1

        print(count)

        if count > 1:
            raise forms.ValidationError(
                'Может быть только одна активная версия продукта.')

        return cleaned_date
