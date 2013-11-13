from django.shortcuts import render_to_response, get_object_or_404
from django.http import Http404

from .models import Book

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
