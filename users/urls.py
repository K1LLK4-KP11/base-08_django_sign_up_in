from django.urls import path  
from django.contrib.auth.views import LogoutView
from .views import profile
from .views import signup  

urlpatterns = [  
    path('signup/', signup, name='signup'),  
]  


from django.contrib.auth.views import LoginView  

urlpatterns += [  
    path('login/', LoginView.as_view(template_name='users/login.html'), name='login'),  
    path('profile/', profile, name='profile'),
]  

