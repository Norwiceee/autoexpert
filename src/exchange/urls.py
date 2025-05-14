from django.urls import path
from exchange.views import (
    CategoryListView,
    CategoryDetailView,    # ← импорт вспомогательного DetailView
    message_create_view,
    set_user_mode,
)
app_name = "exchange"
urlpatterns = [
    path("categories/", CategoryListView.as_view(), name="category_list"),
    path(
        "categories/<int:pk>/",
        CategoryDetailView.as_view(),
        name="category_detail"
            ),
    path("set_user_mode/", set_user_mode, name="set_user_mode"),
    path("categories/", CategoryListView.as_view(), name="category_list"),
    path("messages/create/", message_create_view, name="message_create"),
]
