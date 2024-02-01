from django.db import models


class Record(models.Model):
	created_at = models.DateTimeField(auto_now_add=True)
	first_name = models.CharField(max_length=50)
	last_name =  models.CharField(max_length=50)
	email =  models.CharField(max_length=100)
	phone = models.CharField(max_length=15)
	address =  models.CharField(max_length=100)
	city =  models.CharField(max_length=50)
	state =  models.CharField(max_length=50)
	zipcode =  models.CharField(max_length=20)

	def __str__(self):
		return(f"{self.first_name} {self.last_name}")
	
class Lead(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField()
    phone = models.CharField(max_length=15)
    status = models.CharField(max_length=20, default='New')

    def __str__(self):
        return self.name

class Opportunity(models.Model):
    lead = models.ForeignKey(Lead, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    close_date = models.DateField()
    stage = models.CharField(max_length=20, default='Prospect')

    def __str__(self):
        return f"{self.lead.name}'s Opportunity"