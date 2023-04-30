from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.db import transaction
from .models import *



class PatientSignUpForm(UserCreationForm):  
    first_name=forms.CharField(required=True, widget = forms.TextInput(attrs={'class':'form-control'}))
    last_name=forms.CharField(required=True, widget = forms.TextInput(attrs={'class':'form-control'}))
    phone = forms.CharField(required=True, widget = forms.TextInput(attrs={'class':'form-control'}))
    email=forms.EmailField(required=True, widget = forms.EmailInput(attrs={'class':'form-control'}))
    address = forms.CharField(required=False, widget = forms.TextInput(attrs={'class':'form-control'}))
    
    class Meta(UserCreationForm.Meta):
        model = User
        fields = ('username', 'password1', 'password2','first_name', 'last_name', 'phone', 'email', 'address')
    @transaction.atomic
    def save(self):
        
        user = super().save(commit=False)
        
        user.is_patient = True
        user.save()
        patient = Patient.objects.create(user=user)
        patient.first_name=self.cleaned_data.get('first_name')
        patient.last_name=self.cleaned_data.get('last_name')
        patient.phone=self.cleaned_data.get('phone')
        patient.email=self.cleaned_data.get('email')
        patient.address=self.cleaned_data.get('address')
        patient.save()
        return user
    
    def __init__(self, *args, **kwargs):
        super(PatientSignUpForm, self). __init__(*args, **kwargs)
        self.fields['username'].widget.attrs['class'] = 'form-control'
        self.fields['password1'].widget.attrs['class'] = 'form-control'
        self.fields['password2'].widget.attrs['class'] = 'form-control'




SPECIALTY = [ 
    ('Periodontists','Periodontists' ),
    ('Prosthodontists','Prosthodontists' ),
    ('Pediatric','Pediatric' ),
    ('General Checkup','General Checkup' ),
    ('Toothache','Toothache' ),
    ]





class DoctorSignUpForm(UserCreationForm):  
    first_name=forms.CharField(required=True, widget = forms.TextInput(attrs={'class':'form-control'}))
    last_name=forms.CharField(required=True, widget = forms.TextInput(attrs={'class':'form-control'}))
    phone = forms.CharField(required=True, widget = forms.TextInput(attrs={'class':'form-control'}))
    email=forms.EmailField(required=True, widget = forms.EmailInput(attrs={'class':'form-control'}))
    #specialty = forms.ModelChoiceField(queryset=Doctor.objects.all(), to_field_name='specialty_id', widget=forms.Select(attrs={'class': 'form-control'}))
    specialty = forms.CharField(required=False, widget=forms.Select(choices=SPECIALTY, attrs={'class':'form-control'}))
    address = forms.CharField(required=False, widget = forms.TextInput(attrs={'class':'form-control'}))
    





    class Meta(UserCreationForm.Meta):
        model = User
        #fields = ('username', 'password1', 'password2','first_name', 'last_name', 'phone', 'email', 'specialty','address')
    @transaction.atomic
    def save(self):
        
        user = super().save(commit=False)
        
        user.is_doctor = True
        user.save()
        doctor = Doctor.objects.create(user=user)
        doctor.first_name=self.cleaned_data.get('first_name')
        doctor.last_name=self.cleaned_data.get('last_name')
        doctor.phone=self.cleaned_data.get('phone')
        doctor.email=self.cleaned_data.get('email')
        doctor.specialty=self.cleaned_data.get('specialty')
        doctor.address=self.cleaned_data.get('address')
        doctor.save()
        return user
    
    def __init__(self, *args, **kwargs):
        super(DoctorSignUpForm, self). __init__(*args, **kwargs)
        self.fields['username'].widget.attrs['class'] = 'form-control'
        self.fields['password1'].widget.attrs['class'] = 'form-control'
        self.fields['password2'].widget.attrs['class'] = 'form-control'