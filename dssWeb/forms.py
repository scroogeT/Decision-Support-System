from django import forms

class vrpSolveForm(forms.Form):
    loadTime = forms.IntegerField(label=("Load Time"))
    base = forms.ChoiceField()
    cons = forms.CheckboxSelectMultiple()
    trucks = forms.CheckboxSelectMultiple()

class csvImportForm(forms.Form):
    formInput = forms.FileInput()

    '''

Imagine this scenario: you are to write a form that handles customer address, with a field for phone number, including area code.

from django import forms

class PhoneForm(forms.Form):
    # very basic
    number = forms.CharField()
    area_code = forms.CharField()

Seems easy? What if you have to write HTML with two inputs, one for phone number and one for area code, but in the database there's only one field, for a phone number with area code?

First answer would be to handle this in the clean method, like so:

class PhoneForm(forms.ModelForm):
    number = forms.CharField()
    area_code = forms.CharField()

    def clean(self):
        number = self.cleaned_data['number']
        code = self.cleaned_data['area_code']
        self.cleaned_data['full_number'] = code + number

But this is: a) nasty b) inextensible. You can't simply reuse any of that code and you keep action not directly cleaning anything in the clean method.

But, there's a better way - enter the Django MultiValueField

To use it effectively we need to subclass MultiValueField and MultiWidget. You then set the widget subclass as the field subclass widget, so that you can handle both data manipulation and display.

Final thing to remember is that you need to implement compress and decompress methods for field and widget respectively. This is because the field has to return a single value and is given a single, no matter how many inputs you actually display or how much data is submitted.

E.g.

class PhoneNumberWidget(forms.MultiWidget):
    def __init__(self, *args, **kwargs):
        super(PhoneNumberWidget, self).__init__(*args, **kwargs)
        self.widgets = [
            forms.TextInput(),
            forms.TextInput()
        ]
    def decompress(self, value):
        if value:
            return value.split(' ')
        return [None, None]

class PhoneNumberField(forms.MultiValueField):
    widget = PhoneNumberWidget

    def __init__(self, *args, **kwargs):
        super(PhoneNumberField, self).__init__(*args, **kwargs)
        fields = (
            forms.CharField(),
            forms.CharField()
        )

    def compress(self, data_list):
        return ' '.join(data_list)


class PhoneForm(forms.ModelForm):
    phone_number = PhoneNumberField()

    def __init__(self, *args, **kwargs):
        super(PhoneForm, self).__init__(self, *args, **kwargs)
        self.initial['phone_number'] = ['+1','11111111']

This is a bit more code, but it lets you nicely wrap business logic with code. If you need a field to handle a phone number with area code this way anywhere else, you can just import the field instead of using the copy-paste method.

    '''