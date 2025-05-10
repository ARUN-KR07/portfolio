from django.urls import path, include
from django.views.generic import TemplateView

urlpatterns = [
    path('', include('portfolio.urls')),
     path('about/', TemplateView.as_view(template_name='portfolio/bio.html'), name='about'),
]
