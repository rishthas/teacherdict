from django import forms
from .models import Teacher,Subject

class CreateNewTeacher(forms.ModelForm):
    # firstName   =   forms.CharField(label="First Name", max_length=200)
    # LastName    =   forms.CharField(label="First Name", max_length=200)
    # profilePic  =   forms.FileField(label="Profile Picture")
    # emailId     =   forms.EmailField(label="Email Address",help_text='A valid email address, please.')
    # phoneNumber =   forms.CharField(label="Phone Number ")
    # subject     =   forms.ModelMultipleChoiceField(queryset=Subject.objects.all().values('subject_name'))
    class Meta:
        model = Teacher
        fields = [
            'first_name',
            'last_name',
            'profil_pic',
            'email_id',
            'phone_no',
            'room_no',
            'subjects'
        ]
        widgets={
            'first_name': forms.TextInput(attrs={'class':'form-control'}),
            'last_name': forms.TextInput(attrs={'class':'form-control'}),
            'profil_pic': forms.FileInput(attrs={'class':'form-control'}),
            'email_id': forms.EmailInput(attrs={'class':'form-control'}),
            'phone_no': forms.TextInput(attrs={'class':'form-control'}),
            'room_no': forms.NumberInput(attrs={'class':'form-control'}),
            'subjects': forms.SelectMultiple(attrs={'class':'form-control'}),
        }