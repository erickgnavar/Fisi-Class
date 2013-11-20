from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

from books.views import AuthorCreateView, AuthorDetailView, BooksListView, BooksByAuthorView


urlpatterns = patterns('',
	# url(r'^books/$', 'books.views.home', name='home'),
	url(r'^books/$', BooksListView.as_view(), name='home'),
	url(r'^books/by-author/$', BooksByAuthorView.as_view(), name='books_list_by_author'),
	url(r'^books/(?P<id>\d+)/$', 'books.views.book_detail', name='book_detail'),
	# url(r'books/author/create/$', 'books.views.author_create', name='author_create'),
	url(r'books/author/create/$', AuthorCreateView.as_view(), name='author_create'),
	url(r'books/author/(?P<id>\d+)/$', AuthorDetailView.as_view(), name='author_detail'),
    # Examples:
    # url(r'^$', 'library.views.home', name='home'),
    # url(r'^library/', include('library.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
)
