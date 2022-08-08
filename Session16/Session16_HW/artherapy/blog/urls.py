from artherapy import settings
from blog import views
from django.urls import path
from django.conf.urls.static import static

urlpatterns = [
    # static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT),
    path('home/', views.home, name='home'),
    path('mypage/', views.mypage, name='mypage'),
    path('detail/<int:post_pk>', views.detail, name='detail'),
] 

# if settings.DEBUG:
#     urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
