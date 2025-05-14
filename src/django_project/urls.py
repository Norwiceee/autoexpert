from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path
from core.views import IndexView

urlpatterns = (
    [
        path("__debug__/", include("debug_toolbar.urls")),
        path("admin/", admin.site.urls),
        path("accounts/", include("allauth.urls")),
        path("", include("core.urls")),
        path("users/", include("users.urls")),
        path("exchange/", include("exchange.urls")),
        path("services/", include("services.urls")),
        path("projects/", include("projects.urls")),
        path("orders/", include("orders.urls")),
        path('admin/', admin.site.urls),
        # корень сайта
        path('', IndexView.as_view(), name='home'),
        # все остальные ваши приложения
        path('exchange/', include(('exchange.urls', 'exchange'), namespace='exchange')),
    ]
    + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
)


# Configure Admin panel titles
admin.site.site_header = "AutoExpert – Администрирование"
admin.site.site_title = "AutoExpert – Админка"
admin.site.index_title = "AutoExpert – Админка"
