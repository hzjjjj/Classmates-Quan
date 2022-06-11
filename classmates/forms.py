from django import forms
from classmates.models import Quan

class QuanForm(forms.ModelForm):
      class Meta:
          model = Quan
          fields = [
              'quan_type',
              'quan_title',
              'quan_content',
              'quan_tag',
              'quan_pic',
          ]