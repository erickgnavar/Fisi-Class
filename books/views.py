from django.shortcuts import render_to_response, get_object_or_404
from django.template import RequestContext
from django.http import Http404, HttpResponse
from django.views.generic import CreateView, DetailView, ListView
from django.core.urlresolvers import reverse

from .models import Book, Author
from .forms import AuthorForm

def home(request):
	# try:
	# 	q = request.GET['q']
	# except KeyError:
	# 	q = ''
	q = request.GET.get('q', '')
	context = {
		'books': Book.objects.filter(title__istartswith=q)
	}
	return render_to_response('books/home.html', context)

class BooksListView(ListView):

	template_name = 'books/home.html'
	model = Book
	context_object_name = 'books'
	paginate_by = 10

	def get_queryset(self):
		q = self.request.GET.get('q', '')
		qs = super(BooksListView, self).get_queryset()
		qs = qs.filter(title__istartswith=q)
		return qs

class BooksByAuthorView(BooksListView):

	def get_queryset(self):
		author = self.request.GET.get('author', '')
		qs = super(BooksByAuthorView, self).get_queryset()
		qs = qs.filter(authors__name__istartswith=author)
		return qs

def book_detail(request, id):
	# try:
	# 	book = Book.objects.get(id=id)
	# except Book.DoesNotExist:
	# 	raise Http404
	book = get_object_or_404(Book, id=id)
	context = {
		'book': book
	}
	
	return render_to_response('books/book_detail.html', context)

# import pdb
# pdb.set_trace()

def author_create(request):
	if request.method == 'POST':
		form = AuthorForm(request.POST)
		if form.is_valid():
			# data = form.cleaned_data
			form.save()
			return HttpResponse('se creo correctamente')
		else:
			context = {
				'form': form
			}
			return render_to_response('books/author_create.html', context, RequestContext(request))
	else:
		context = {
			'form': AuthorForm()
		}
		return render_to_response('books/author_create.html', context, RequestContext(request))


class AuthorDetailView(DetailView):

	template_name = 'books/author_detail.html'
	context_object_name = 'author' # object
	model = Author

	def get_object(self, queryset=None):
		pk = self.kwargs.get('id')
		try:
			author = self.model.objects.get(id=pk)
			return author
		except Author.DoesNotExist:
			raise Http404


class AuthorCreateView(CreateView):

	template_name = 'books/author_create.html'
	form_class = AuthorForm
	# success_url = '/'

	def get_success_url(self):
		url = reverse('author_detail', kwargs={'id': self.object.id})
		print url
		return url
