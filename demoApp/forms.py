"""Demo App Form."""
from django import forms

from demoApp.models import Demo

FAVOURITE_DISH = [
    ("Egyptian", "Egyptian"),
    ("Italian", "Italian"),
    ("Mexican", "Mexican"),
    ("Indian", "Indian"),
    ("Chinese", "Chinese"),
    ("Thai", "Thai"),
    ("Japanese", "Japanese"),
    ("American", "American"),
    ("French", "French"),
    ("Greek", "Greek"),
    ("Spanish", "Spanish"),
    ("German", "German"),
    ("Irish", "Irish"),
    ("Polish", "Polish"),
    ("Russian", "Russian"),
    ("Swedish", "Swedish"),
]


class DemoForm(forms.Form):
    """Demo Form"""
    name = forms.CharField(label='Name', max_length=100, help_text='Enter your name')
    email = forms.EmailField(label='Email', required=True, initial="enter your email")
    address = forms.CharField(label='Address', max_length=100)
    city = forms.CharField(label='City', max_length=100)
    state = forms.CharField(label='State', max_length=100)
    zip = forms.CharField(label='Zip', max_length=100)
    phone = forms.CharField(label='Phone', max_length=100)
    comments = forms.CharField(label='Comments', max_length=100,
                               widget=forms.Textarea(
                                   attrs={'rows': 5, 'cols': 20}
                               ))
    reservation_date = forms.DateField(label='Reservation Date',
                                       widget=forms.SelectDateWidget(
                                           empty_label=("Choose Year", "Choose Month", "Choose Day"),
                                       ))

    reservation_date2 = forms.DateField(label='Reservation Date',
                                        widget=forms.NumberInput(attrs={'type': 'date'}
                                                                 ))
    favorit_dishes1 = forms.ChoiceField(label='Favorit Dishes',
                                  choices=FAVOURITE_DISH,
                                  widget=forms.Select(attrs={'class': 'form-control'}))

    favorit_dishes2 = forms.MultipleChoiceField(label='Favorit Dishes',
                                           choices=FAVOURITE_DISH,
                                           widget=forms.SelectMultiple(attrs={'class': 'form-control'}))

    favorit_dishes3 = forms.ChoiceField(label='Favorit Dishes',

                                           widget=forms.RadioSelect, choices=FAVOURITE_DISH)


class DemoModelForm(forms.ModelForm):
   class Meta:
       model = Demo
       fields = '__all__'