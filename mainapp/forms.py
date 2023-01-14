from django.forms import ModelForm

from mainapp.models import Feedback


class FeedbackForm(ModelForm):
    class Meta:
        model = Feedback
        fields = (
            'first_name',
            'phone_number',
            'email',
            'text'
        )

    # def __init__(self, *args, **kwargs):
    # super()...
    # for name, item in ....
    # item.... = 'tb1'
