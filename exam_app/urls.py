from django.urls import path
from .views import question_create, question_list

urlpatterns = [
    path('', question_create, name='question_create'),
    path('questions/', question_list, name='question_list'),

]


