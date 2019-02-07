from django.conf.urls import url
from hireme import views

#Template Url
app_name = 'hireme'

urlpatterns = [
    url(r'^register/$',views.register,name='register'),
    url(r'^developers/$',views.developersView.as_view(), name="developers"),
    url(r'^detail/(?P<pk>\d+)$',views.UserDetailView.as_view(), name="detail"),
]