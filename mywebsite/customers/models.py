from django.db import models
from django.db.models import Model 	

# Create your models here.

class Books(models.Model):
	book_id= models.AutoField(primary_key=True)
	title = models.TextField()
	pages = models.IntegerField()
	price = models.DecimalField(max_digits=5, decimal_places=2)
	created_on = models.DateTimeField(auto_now_add=True)
	author = models.TextField()
	
	class Meta:
		db_table = 'books_master'
	def __str__(self):
	    return f"{self.title} by {self.author}"