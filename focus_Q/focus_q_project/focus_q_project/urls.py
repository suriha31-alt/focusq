from django.contrib import admin
from django.urls import path, include

# ✅ ADD THESE
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('analysis.urls')),
]

# ✅ ADD THIS AT THE END (VERY IMPORTANT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)