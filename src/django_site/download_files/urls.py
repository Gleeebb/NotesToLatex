from django.conf.urls import url, include
from .views import Index, Register, Login, \
        Logout, MyFiles, Editor
from django.conf import settings
from django.conf.urls.static import static
from django.views.static import serve


urlpatterns = [
    url(r'^$',  Index.as_view(), name='index'),
    url(r'^registration/', Register.as_view(), name='register'),
    url(r'login/', Login.as_view(), name='login'),
    url(r'logout/', Logout.as_view(), name='logout'),
    url(r'files/', MyFiles.as_view(), name='myfiles'),
    url(r'editor/img/(?P<img_id>\d+)/', Editor.as_view(), name='editor'),
    url(r'^markdownx/', include('markdownx.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
