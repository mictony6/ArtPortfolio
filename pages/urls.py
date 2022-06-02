from django.urls import path


from pages.views import about_view, commissions_view, home_view


urlpatterns = [
    path('', home_view, name='home'),
    path('about/', about_view, name='about'),
    path('commissions/', commissions_view, name='commissions'),
]
