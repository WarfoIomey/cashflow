from django.contrib import admin
from django.urls import include, path, reverse_lazy
from django.views.generic.edit import CreateView
from django.contrib.auth.forms import UserCreationForm
from django.conf.urls.static import static
from django.conf import settings


handler404 = 'cashflow.views.page_not_found'
handler500 = 'cashflow.views.failure_server'

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('cashflow.urls', namespace='cashflow')),
    path('auth/', include('django.contrib.auth.urls')),
    path(
        'auth/registration/',
        CreateView.as_view(
            template_name='registration/registration_form.html',
            form_class=UserCreationForm,
            success_url=reverse_lazy('cashflow:index'),
        ),
        name='registration',
    ),
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
