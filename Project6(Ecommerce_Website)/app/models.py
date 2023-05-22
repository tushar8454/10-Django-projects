from django.db import models

# Create your models here.
from django.contrib.auth.models import User
from django.core.validators import MaxLengthValidator,MinLengthValidator

STATE_CHOICES=(
('Andaman & Nicobar Islands', 'Andaman & Nicobar Islands'),
 ('Andhra Pradesh', 'Andhra Pradesh'),
#  ('Arunachal Pradesh', 'Arunachal Pradesh'),
#  ('Assam', 'Assam'),
#  ('Bihar', 'Bihar'),
# ('Chandigarh', 'Chandigarh'),
#  ('Chhattisgarh', 'Chhattisgarh'),
#  ('Dadra & Nagar Haveli', 'Dadra & Nagar Haveli'),
#  ('Daman and Diu', 'Daman and Diu'),
#  ('Delhi', 'Delhi'),
# ('Goa', 'Goa'),
#  ('Gujarat', 'Gujarat'),
#  ('Haryana' 'Haryana'),
#  ('Himachal Pradesh', 'Himachal Pradesh'),
#  ('Jammu &  Kashmir', 'Jammu & Kashmir'),
#   ('Jharkhand', 'Jharkhand'),
#   ('Karnataka', 'Karnataka'),
#  ('Kerala', 'Kerala'),
#  ('Lakshadweep', 'Lakshadweep'),
#  ('Madhya Pradesh', 'Madhya Pradesh'),
#  ('Maharashtra', 'Maharashtra'),
)

class Customer(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    name=models.CharField(max_length=100)
    locality=models.CharField(max_length=300)
    city=models.CharField(max_length=100)
    zipcode=models.IntegerField()
    state=models.CharField(choices=STATE_CHOICES,max_length=100,default=None)

    def __str__(self):
        #str is used because id is a interger field and it not return interger so we converted it in string
        return str(self.id)
    
CATEGORY_CHOICES=(
    ('M', 'Mobile'),
    ('l','Laptop'),
    ('TW','Top Wear'),
    ('BW','Bottom Wear'),
)
class Product(models.Model):
    title=models.CharField(max_length=500)
    selling_price=models.FloatField()
    discount_price=models.FloatField()
    description=models.TextField()
    brand=models.CharField(max_length=100)
    #in brand why we use max_length=2 because in category_choices we have 2 length character if we increase the character we also increase the length
    category=models.CharField(choices=CATEGORY_CHOICES,max_length=2)
    product_image=models.ImageField(upload_to='producting')

    def __str__(self):
        return str(self.id)
    
class Cart(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    product=models.ForeignKey(Product,on_delete=models.CASCADE)
    quantity=models.PositiveIntegerField(default=1)

    def __str__(self):
        return str(self.id)
    
STATUS_CHOICES=( 
('Accepted', 'Accepted'),
('Packed', 'Packed'),
('On The Way', 'On The Way'),
('Delivered', 'Delivered'),
('Cancel', 'Cancel')
)

class OrderPlaced(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    customer=models.ForeignKey(Customer,on_delete=models.CASCADE)
    product=models.ForeignKey(Product,on_delete=models.CASCADE)
    quantity=models.PositiveIntegerField(default=1)
    ordered_date=models.DateTimeField(auto_now_add=True)
    status=models.CharField(max_length=50,choices=STATUS_CHOICES,default='Pending')