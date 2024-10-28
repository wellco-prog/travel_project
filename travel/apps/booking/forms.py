from  django import forms
from .models import Package, Destination

class BookingForm(forms.ModelForm):
    # naming = forms.ChoiceField (widget=forms.Select, choices=())
    naming = forms.ModelChoiceField (queryset= Package.objects.all(), widget=forms.Select (attrs={'placeholder': 'Пакет', 'class': 'form-control'}))
    from_date = forms.DateField(widget=forms.NumberInput (attrs={'type':'date','class': 'form-control'}))
    class Meta:
        model = Package
        fields = ['naming', 'from_date', 'daysCount']
        widgets = {
            # 'naming': forms.Select(attrs={'class': 'form-control'}),
            # 'from_date': forms.DateField(attrs={'placeholder': 'from_date','class': 'form-control'}),
            'daysCount': forms.NumberInput(attrs={'placeholder': 'daysCount','class': 'form-control'}),

        }


    # def __init__(self, *args, **kwargs):
    #     super(BookingForm, self).__init__(*args, **kwargs)
    #     self.fields['naming'].choices = [(option.id, option.naming) for option in Package.objects.all()]

    # def init(self, *args, **kwargs):
    #     super(MyForm, self).init(*args, **kwargs)
    #     # Получаем все объекты Option из базы данных
    #     options = Option.objects.all()
    #     self.fields['choice_field'].choices = [(option.id, option.name) for option in options]
