from django.urls import path, re_path

from . import views

urlpatterns = [
    path('vis_df/', views.vis_df, name='vis_df'),
] 