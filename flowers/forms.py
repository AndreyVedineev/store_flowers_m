from django import forms

from flowers.models import Flowers, Version


class StyleFormMixin:
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            print(field_name)
            field.widget.attrs['class'] = 'form-control'


class FlowersForm(StyleFormMixin, forms.ModelForm):
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


class VersionForm(StyleFormMixin, forms.ModelForm):
    class Meta:
        model = Version
        fields = '__all__'


    def clean_indicator(self):
        cleaned_data = self.cleaned_data['indicator']
        # print(cleaned_data)
        # # print(self.instance.product.version_set.filter(indicator=True).exclude(id=self.instance.id).exists())

        if cleaned_data and self.instance.product.version_set.filter(indicator=True).exclude(
                id=self.instance.id).exists():
            raise forms.ValidationError(f'Может существовать только одна активная версия.')

        return cleaned_data
