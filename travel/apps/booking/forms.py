from  django import forms
from .models import Package, Order

class BookingForm(forms.ModelForm):
    package = forms.ModelChoiceField (queryset= Package.objects.all(), widget=forms.Select (attrs={'class': 'form-control', 'required': 'required'}))
    from_date = forms.DateField(widget=forms.NumberInput (attrs={'type':'date','class': 'form-control', 'required': 'required'}))
    class Meta:
        model = Order
        fields = ['package', 'from_date']
    # def clean_from_date(self):
    #     data = self.cleaned_data['from_date']
    #     if not data:
    #         raise forms.ValidationError("Выберите дату!")
    #     return data
# class BookingForm(forms.ModelForm):
#     naming = forms.ChoiceField(
#         choices=[(package.id, package.naming) for package in Package.objects.all()],
#         widget=forms.Select(attrs={'placeholder': 'Пакет', 'class': 'form-control'})
#     )
#     from_date = forms.DateField(widget=forms.NumberInput(attrs={'type': 'date', 'class': 'form-control'}))
#
#     class Meta:
#         model = Order
#         fields = ['naming', 'from_data']


    # def __init__(self, *args, **kwargs):
    #     super(BookingForm, self).__init__(*args, **kwargs)
    #     self.fields['naming'].choices = [(option.id, option.naming) for option in Package.objects.all()]

    # def init(self, *args, **kwargs):
    #     super(MyForm, self).init(*args, **kwargs)
    #     # Получаем все объекты Option из базы данных
    #     options = Option.objects.all()
    #     self.fields['choice_field'].choices = [(option.id, option.name) for option in options]
