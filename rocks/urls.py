from django.urls import path
from .views import *
from django.conf import settings
from django.conf.urls.static import static
app_name: str = 'rocks'
urlpatterns = [
    path('', MainView.as_view(), name='home'),
    path('create/', RockCreateView.as_view(), name='create'),
    path('update/<int:pk>', RockUpdateView.as_view(), name='update'),
    path('delete/<int:pk>', RockDeleteView.as_view(), name='delete'),
    path('rock/<int:pk>', RockView.as_view(), name='rock'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)