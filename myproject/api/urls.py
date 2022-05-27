from django.urls import path  
from .views import get_data , add_data 





urlpatterns = [
	path('' , get_data),
	path('add/' , add_data),

]