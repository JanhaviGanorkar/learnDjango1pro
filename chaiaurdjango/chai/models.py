from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.

class ChaiVariety(models.Model):
  CHAI_TYPE_CHOICES = [
    ('ML', 'MASALA'),
    ('GR', 'GINGER'),
    ('KL', 'KIWI'),
    ('PL', 'PLAIN'),
    ('EL', 'ELAICHI'),
  ]

  name = models.CharField(max_length=100)
  image = models.ImageField(upload_to='chais/')
  date_added = models.DateTimeField(default=timezone.now)
  discription = models.CharField(max_length=5000,default='')
  price = models.IntegerField()
  type = models.CharField(max_length=2, choices=CHAI_TYPE_CHOICES, default='ML')

  def __str__(self):
    return self.name
  
class ChaiReview(models.Model):
  Review_CHOICES = [
    (1, 'Very Good'),
    (2, 'Good'),
    (3, 'Not Bad'),
    (4, 'Bad'),
    (5, 'Poor'),
  ]
  chai = models.ForeignKey(ChaiVariety, on_delete=models.CASCADE, related_name='reviews')
  user = models.ForeignKey(User, on_delete=models.CASCADE)
  rating = models.IntegerField(choices=Review_CHOICES)
  comment = models.TextField()
  date_added = models.DateTimeField(default=timezone.now)
  
  def __str__(self):
     return f'{self.user.username} review for {self.chai.name}'
  
class Store(models.Model):
  name = models.CharField(max_length=100)
  location = models.CharField(max_length=100)
  chai_varieties = models.ManyToManyField(ChaiVariety, related_name='stores')

  def __str__(self):
    return self.name
    
class ChaiCertificate(models.Model):
  chai = models.OneToOneField(ChaiVariety, on_delete=models.CASCADE, related_name='certificate')
  certificate_number = models.CharField(max_length=100)
  issued_date = models.DateTimeField(default=timezone.now)
  valid_until = models.DateTimeField()

  def __str__(self):
    return f'Certificate for {self.chai.name}'