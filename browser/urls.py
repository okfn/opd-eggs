from django.conf.urls import url
from django.views.generic import TemplateView

from . import views

app_name = 'browser'
urlpatterns = [
    url(r'^$', TemplateView.as_view(template_name="browser/home.html")),
    url(r'^home$', TemplateView.as_view(template_name="browser/home.html"), name='home'),
    url(r'^about$', TemplateView.as_view(template_name="browser/about.html"), name='about'),
    url(r'^search$', views.search_gtin, name='search'),
    url(r'^search/(?P<gtin>[0-9a-z-]+)$', views.search_gtin2, name='search2'),
    url(r'^brand/list$', views.ViewBrandList.as_view(), name='brand_list'),
    url(r'^stats$', views.ViewStats.as_view(), name='stats'),
    url(r'^brand/(?P<bsin>[a-zA-Z0-9]+)$', views.ViewBsin.as_view(), name='bsin'),
    url(r'^gtin/(?P<pk>[0-9a-z-]+)$', views.ViewGtin.as_view(), name='gtin'),
    url(r'^result/(?P<gtin>[0-9]+)$', views.ViewResultGtin.as_view(), name='result'),
    url(r'^owner/list$', views.ViewOwnerList.as_view(), name='owner_list'),
    url(r'^owner/(?P<owner>[a-zA-Z0-9]+)$', views.ViewOwner.as_view(), name='owner'),
    url(r'^label/list$', views.ViewLabelList.as_view(), name='label_list'),
    url(r'^label/(?P<pk>[0-9]+)$', views.ViewLabel.as_view(), name='label'),
    url(r'^orga/list$', views.ViewOrgaList.as_view(), name='orga_list'),
    url(r'^orga/(?P<pk>[0-9]+)$', views.ViewOrga.as_view(), name='orga'),
]
