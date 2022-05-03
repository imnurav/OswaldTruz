from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from oswaldtruz.views import About, Contact, Home

urlpatterns = [
    path('admin/', include('admin_honeypot.urls', namespace='admin_honeypot')),
    path('securelogin/', admin.site.urls),
    path('', Home, name='home'),
    path('about/', About, name='about'),
    # path('contact', Contact, name='contact'),
    path('contact/', include('contact.urls')),
    path('store/', include('store.urls')),
    path('cart/', include('carts.urls')),
    path('accounts/', include('accounts.urls')),

    # order URls
    path('orders/', include('orders.urls')),
]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
