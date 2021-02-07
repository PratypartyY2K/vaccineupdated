from django.urls import path
from . import views
from .views import Enrollment,HospitalPageView,Final
urlpatterns = [
    path('',views.home,name='home'),
    path('enroll/',Enrollment.as_view(),name='enroll'),
    path('book/', HospitalPageView.as_view(), name='book'),
    path('final/',Final.as_view(),name='final'),
    path('phase2/',views.phase2,name='phase2'),
]