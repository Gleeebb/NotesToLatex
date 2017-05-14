from django.conf.urls import url
from .views import Index, Download, Register, Login, \
        Logout, MyFiles

urlpatterns = [
    url(r'^$',  Index.as_view(), name='index'),
    url(r'^download/', Download.as_view(), name='download'),
    url(r'^registration/', Register.as_view(), name='register'),
    url(r'login/', Login.as_view(), name='login'),
    url(r'logout/', Logout.as_view(), name='logout'),
    url(r'files/', MyFiles.as_view(), name='myfiles')
]