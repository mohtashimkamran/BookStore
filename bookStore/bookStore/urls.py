
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('adminV/',include('adminView.urls')),
    path('api/s1',include('students.urls')),
    path('api/b1/',include('books.urls'))
]
