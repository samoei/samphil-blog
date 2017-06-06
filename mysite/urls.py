from django.conf.urls import url, include
from django.contrib import admin
from django.contrib.sitemaps.views import sitemap
from blog.sitemaps import PostSiteMap

sitemaps = {
	'posts': PostSiteMap,
}

urlpatterns = [
	url(r'^admin/', admin.site.urls),
	url(r'^blog/', include('blog.urls', namespace='blog', app_name='blog')),
	url(r'', sitemap, {'sitemaps': sitemaps}, name='django.contrib.sitemaps.views.sitemap'),
]
