
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/', include('djoser.urls')),
    # djoser 可以幫網址帶授權驗證
    path('api/v1/', include('djoser.urls.authtoken')),
    # 把 product 這個 app 內的 url 帶過來
    path('api/v1/', include('product.urls')),
    # 把 order 這個 app 內的 url 帶過來
    path('api/v1/', include('order.urls')),
    # 把媒體帶過去
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
