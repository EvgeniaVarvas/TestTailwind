from django import forms
from registry.models import Orders
from cut.models import Format


class OrderFilterForm(forms.Form):
    compounds = forms.MultipleChoiceField(
        choices=[],
        widget=forms.CheckboxSelectMultiple,
        label='Выберите составы'
    )
    formats = forms.MultipleChoiceField(
        choices=[],
        widget=forms.CheckboxSelectMultiple,
        label='Выберите форматы'
    )

    def __init__(self, *args, **kwargs):
        super(OrderFilterForm, self).__init__(*args, **kwargs)
        compounds = Orders.objects.values_list('compound', flat=True).distinct()
        formats = Format.objects.all()
        self.fields['compounds'].choices = [(compound, compound) for compound in compounds]
        self.fields['formats'].choices = [(format_obj.id, format_obj.name) for format_obj in formats]
