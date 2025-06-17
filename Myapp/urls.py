from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.index, name="index"),
    path('doctors/', views.doctor_list, name='doctor_list'),
    path('contact', views.contact, name='contact'),
    path('ai-bot/', views.ai_bot, name='ai_bot'),
    path('appointment/', views.appointment_view, name='appointment'),
    path('blog-single/', views.blog_single, name='blog_single'),
    path('portfolio-details/', views.portfolio_details, name='portfolio-details'),
    
    
]+ static(settings.STATIC_URL, document_root=settings.STATICFILES_DIRS[0])