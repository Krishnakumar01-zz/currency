from django.conf.urls import url
from . import views

urlpatterns=[
	url(r'^$',views.home,name='home'),
	url(r'conversion/$',views.conversion,name='conversion'),
	url(r'conversion/output/$',views.conversion,name='output'),
	url(r'signin/$',views.signin,name='signin'),
	url(r'signup/$',views.signup,name='signup'),
	url(r'signout/$',views.signout,name='signout')

	]