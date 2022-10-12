from django.db import models

#create here model


from .extras import ProfanityFilter
from django.core.exceptions import ValidationError

pf = ProfanityFilter()


def validate_is_profane(value):
    rt = pf.is_profane(value)
    return rt
    # print(rt)
    # if rt is True:
    #     raise ValidationError('Please remove any profanity/swear words.')

class Data(models.Model):
    #text = models.CharField(max_length=300, validators=[validate_is_profane])
    text = models.CharField(max_length=300)
    def save(self, *args, **kwargs):
        self.text = validate_is_profane(self.text)
        return super().save(*args, **kwargs)