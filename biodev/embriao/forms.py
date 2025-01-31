from crispy_forms.helper import FormHelper
from crispy_forms.layout import Div, Field

from home.forms import softdelete_fields
from django import forms

from embriao.models import Botijao, Caneco, Hack, Palheta


class BotijaoForm(forms.ModelForm):
    class Meta:
        model = Botijao
        exclude = softdelete_fields
        

    def __init__(self, *args, readonly=False, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper(self)
        self.helper.form_tag = False
        if readonly:
            self.helper.all().wrap(Field, readonly='readonly', disabled='disabled')
        self.helper.all().wrap(Div, css_class='col-6')



class CanecoForm(forms.ModelForm):
    class Meta:
        model = Caneco
        exclude = softdelete_fields
        widgets = {
            'data': forms.TextInput(attrs={'type': 'date'}),
        }

    def __init__(self, *args, readonly=False, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper(self)
        self.helper.form_tag = False
        if readonly:
            self.helper.all().wrap(Field, readonly='readonly', disabled='disabled')
        self.helper.all().wrap(Div, css_class='col-6')

class HackForm(forms.ModelForm):
    class Meta:
        model = Hack
        exclude = softdelete_fields


    def __init__(self, *args, readonly=False, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper(self)
        self.helper.form_tag = False
        if readonly:
            self.helper.all().wrap(Field, readonly='readonly', disabled='disabled')
        self.helper.all().wrap(Div, css_class='col-6')


class PalhetaForm(forms.ModelForm):
    class Meta:
        model = Palheta
        exclude = softdelete_fields


    def __init__(self, *args, readonly=False, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper(self)
        self.helper.form_tag = False
        if readonly:
            self.helper.all().wrap(Field, readonly='readonly', disabled='disabled')
        self.helper.all().wrap(Div, css_class='col-6')


