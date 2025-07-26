from django.urls import path
from .views import signin, signup, signout, ajaxreg, profile, activate

urlpatterns = [
    path('signin', signin, name='signin'),
    path('signup', signup, name='signup'),
    path('signout', signout, name='signout'),
    path('ajaxreg', ajaxreg),
    path('profile', profile, name='profile'),
    path('activate/<str:uidb64>/<str:token>/', activate, name='activate')
]