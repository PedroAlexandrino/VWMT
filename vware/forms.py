from django import forms
from django.forms import ClearableFileInput

from vware.models import ShippingOperation, ReceivingOperation, Procedimentos, Others


class FileModelForm(forms.ModelForm):
    class Meta:
        model = ShippingOperation
        fields = [
            "one",
            "two",
            "three",
            "four",
            "five",
            "six",
            "seven",
            "eight",
            "checklist",
            "others",
            "requestShippers",
        ]
        widgets = {
            "one": ClearableFileInput(attrs={"multiple": True}),
            "two": ClearableFileInput(attrs={"multiple": True}),
            "three": ClearableFileInput(attrs={"multiple": True}),
            "four": ClearableFileInput(attrs={"multiple": True}),
            "five": ClearableFileInput(attrs={"multiple": True}),
            "six": ClearableFileInput(attrs={"multiple": True}),
            "seven": ClearableFileInput(attrs={"multiple": True}),
            "eight": ClearableFileInput(attrs={"multiple": True}),
            "checklist": ClearableFileInput(attrs={"multiple": True}),
            "others": ClearableFileInput(attrs={"multiple": True}),
            "requestShippers": ClearableFileInput(attrs={"multiple": True}),
        }
        # widget is important to upload multiple files


class FileModelFormReceiving(forms.ModelForm):
    class Meta:
        model = ReceivingOperation
        fields = ["one", "two", "three", "four", "five", "six", "seven", "eight"]
        widgets = {
            "one": ClearableFileInput(attrs={"multiple": True}),
            "two": ClearableFileInput(attrs={"multiple": True}),
            "three": ClearableFileInput(attrs={"multiple": True}),
            "four": ClearableFileInput(attrs={"multiple": True}),
            "five": ClearableFileInput(attrs={"multiple": True}),
            "six": ClearableFileInput(attrs={"multiple": True}),
            "seven": ClearableFileInput(attrs={"multiple": True}),
            "eight": ClearableFileInput(attrs={"multiple": True}),
            "nine": ClearableFileInput(attrs={"multiple": True}),
        }
        # widget is important to upload multiple files


class FileModelFormProcedimentos(forms.ModelForm):
    class Meta:
        model = Procedimentos
        fields = [
            "anexoOne",
            "anexoTwo",
            "anexoThree",
            "anexoFour",
            "anexoFive",
            "anexoSix",
            "anexoSeven",
            "anexoEight",
            "anexoNine",
            "qpsOne",
            "qpsTwo",
            "qpsThree",
            "qpsFour",
            "qpsFive",
            "qpsSix",
            "qpsSeven",
            "qpsEight",
            "qpsNine",
        ]
        widgets = {
            "anexoOne": ClearableFileInput(attrs={"multiple": True}),
            "anexoTwo": ClearableFileInput(attrs={"multiple": True}),
            "anexoThree": ClearableFileInput(attrs={"multiple": True}),
            "anexoFour": ClearableFileInput(attrs={"multiple": True}),
            "anexoFive": ClearableFileInput(attrs={"multiple": True}),
            "anexoSix": ClearableFileInput(attrs={"multiple": True}),
            "anexoSeven": ClearableFileInput(attrs={"multiple": True}),
            "anexoEight": ClearableFileInput(attrs={"multiple": True}),
            "anexoNine": ClearableFileInput(attrs={"multiple": True}),
            "qpsOne": ClearableFileInput(attrs={"multiple": True}),
            "qpsTwo": ClearableFileInput(attrs={"multiple": True}),
            "qpsThree": ClearableFileInput(attrs={"multiple": True}),
            "qpsFour": ClearableFileInput(attrs={"multiple": True}),
            "qpsFive": ClearableFileInput(attrs={"multiple": True}),
            "qpsSix": ClearableFileInput(attrs={"multiple": True}),
            "qpsSeven": ClearableFileInput(attrs={"multiple": True}),
            "qpsEight": ClearableFileInput(attrs={"multiple": True}),
            "qpsNine": ClearableFileInput(attrs={"multiple": True}),
        }


class FileModelFormOthers(forms.ModelForm):
    class Meta:
        model = Others
        fields = ["one", "two", "three", "four", "five"]
        widgets = {
            "one": ClearableFileInput(attrs={"multiple": True}),
            "two": ClearableFileInput(attrs={"multiple": True}),
            "three": ClearableFileInput(attrs={"multiple": True}),
            "four": ClearableFileInput(attrs={"multiple": True}),
            "five": ClearableFileInput(attrs={"multiple": True}),
        }
