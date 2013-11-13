from django.db import models

class Author(models.Model):

	name = models.CharField(
		max_length=100
	)
	citizenship = models.CharField(
		max_length=100
	)

	created = models.DateTimeField(auto_now_add=True)
	modified = models.DateTimeField(auto_now=True)

	class Meta:
		app_label = 'books'

	def __unicode__(self):
		# return self.name + ' ' + self.citizenship
		return '%s %s' % (self.name, self.citizenship)
		# return '{name} {citizenship}'.format(name=self.name, citizenship=self.citizenship)

class Book(models.Model):

	title = models.CharField(
		max_length=100
	)
	isbn = models.IntegerField(
		unique=True
	)
	pages_number = models.IntegerField()
	authors = models.ManyToManyField('Author')
	editorial = models.ForeignKey('Editorial') # editorial_id

	created = models.DateTimeField(auto_now_add=True)
	modified = models.DateTimeField(auto_now=True)

	class Meta:
		app_label = 'books'

	def __unicode__(self):
		return self.title


class Editorial(models.Model):

	name = models.CharField(
		max_length=100
	)

	created = models.DateTimeField(auto_now_add=True)
	modified = models.DateTimeField(auto_now=True)

	class Meta:
		app_label = 'books'

	def __unicode__(self):
		return self.name
