from django import forms 
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm, PasswordChangeForm
from django.contrib.auth import get_user_model
from main.models import groups


class LoginUsersForm(AuthenticationForm):
    username = forms.CharField(label = 'Логин',
                                widget=forms.TextInput(attrs={'class':'form-input'}))
    password = forms.CharField(label = 'Пароль',
                                widget=forms.PasswordInput(attrs={'class':'form-input'}))

    class Meta:
        model = get_user_model()
        fields = ['username', 'password']


class RegisterUserForm(UserCreationForm):
    username = forms.CharField(label='Логин', widget=forms.TextInput(attrs={'class':'form-input'}))
    password1 = forms. CharField(label='Пароль', widget=forms.PasswordInput(attrs={'class':'form-input'}))
    password2 = forms. CharField(label='Повтор пароль', widget=forms.PasswordInput(attrs={'class':'form-input'}))
    Group = forms.ModelChoiceField(label='Группа', queryset=groups.objects.all())

    class Meta:
        model = get_user_model()
        fields = ['username', 'email','Group', 'first_name', 'last_name', 'password1', 'password2']
        labels = {
            'email':'Корпоративная почта',
            'first_name':'Имя',
            'last_name':'Фамилия',
        }

        widgets = {
            'email': forms.EmailInput(attrs={'class':'form-input'}),
            'first_name': forms.TextInput(attrs={'class':'form-input'}),
            'last_name': forms.TextInput(attrs={'class':'form-input'}),
        }
    
    def clean_email(self):
        email = self.cleaned_data['email']
        if get_user_model().objects.filter(email=email).exists():
            raise forms.ValidationError('Такая поячта уже существует')
        return email
    


class ProfileUserForm(forms.ModelForm):
    username = forms.CharField(disabled=True, label='Логин', widget=forms.TextInput(attrs={'class':'form-input'}))
    email = forms.CharField(disabled=True, label='Кооперативная почта', widget=forms.TextInput(attrs={'class':'form-input'}))

    class Meta:
        model = get_user_model()
        fields = ['username', 'email', 'first_name', 'last_name']
        labels = {
            'first_name':'Имя',
            'last_name':'фамилия',
        }
        widgets = {
            'first_name': forms.TextInput(attrs={'class':'form-input'}),
            'last_name': forms.TextInput(attrs={'class':'form-input'}),
        }


class UserPasswordChangeForm(PasswordChangeForm):
    old_password = forms.CharField(label='Старый пароль', widget=forms.PasswordInput(attrs={'class':'form-input'}))
    password1 = forms.CharField(label='Новый пароль', widget=forms.PasswordInput(attrs={'class':'form-input'}))
    password2 = forms.CharField(label='Повтор нового пароля', widget=forms.PasswordInput(attrs={'class':'form-input'}))

    