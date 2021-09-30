from django import forms
from hello.models import LogMessage

class LogMessageform(forms.ModelForm):
    class Meta:
        model = LogMessage
        fields = ("message",)