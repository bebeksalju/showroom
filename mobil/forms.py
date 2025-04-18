from django import forms
from .models import Mobil, Service

class MobilForm(forms.ModelForm):
    class Meta:
        model = Mobil
        fields = '__all__'
        widget ={
            'tahun': forms.NumberInput(attrs={'min':1900, 'max':2100}),
            'menggunakan_bank': forms.CheckboxInput(attrs={'id': 'bank-toggle'}),
        }
        
        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)
            self.fields['pinjaman_bank'].required = False
            self.fields['suku_bunga'].required = False
        
        def clean(self):
            cleaned_data = super().clean()
            if cleaned_data.get('menggunakan_bank'):
                if not cleaned_data.get('pinjaman_bank'):
                    raise forms.ValidationError('pinjaman_bank', 'Pinjaman Bank harus diisi jika menggunakan bank.')
                if not cleaned_data.get('suku_bunga'):
                    raise forms.ValidationError('suku_bunga', 'Suku Bunga harus diisi jika menggunakan bank.')
            return cleaned_data

class ServiceForm(forms.ModelForm):
    class Meta:
        model = Service
        fields = [
            'tanggal_service',
            'deskripsi',
            'biaya_service',
        ]
        widgets = {
            'tanggal_service': forms.DateInput(attrs={'type': 'date'}),
        }