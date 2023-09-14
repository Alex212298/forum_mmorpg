from django_filters import FilterSet
from .models import *



class RespFilter(FilterSet):
    class Meta:
        model = Repsponses
        fields = ('post_id_id', 'user_id_id', 'resp_text')