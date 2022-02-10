from django.db import models
import random
import string
from django.template.defaultfilters import slugify
# Create your models here.

class UserRecord(models.Model):
    Selling_Key = models.CharField(max_length=1000,blank=True,null=True)
    Order_Revenue_Date = models.DateField(auto_now=False, auto_now_add=False)
    Funds_Cleared_Date = models.DateField(auto_now=False, auto_now_add=False)
    From = models.CharField(max_length=50)
    Percentage_For_Tahir = models.FloatField()
    Percentage_For_Sohail = models.FloatField()
    Total_Price = models.FloatField()
    Getting_Price = models.FloatField()
    Is_Blocked = models.BooleanField("Is Blocked")


    def save(self, *args, **kwargs):
        if(self.Selling_Key is None):
            self.Selling_Key = self.WithoutRepeat(26)
        print(self.Selling_Key)
        super(UserRecord, self).save(*args, **kwargs)
    def WithoutRepeat(self,length):
        letters = string.ascii_lowercase # define the specific string
        # define the condition for random.sample() method
        result = ''.join((random.sample(letters, length)))
        return result
    def __str__(self):
        return self.From

class Options(models.Model):
    title = models.CharField(max_length=250,blank=True,null=True)
    included = models.CharField(max_length=250,blank=True,null=True)
    def __str__(self):
        return self.title
    
class Order(models.Model):
    user_record = models.ForeignKey(UserRecord, on_delete=models.CASCADE)
    title = models.CharField(max_length=50,blank=True,null=True)
    amount = models.FloatField()
    days = models.IntegerField(blank=True,null=True)
    requirments = models.CharField(max_length=250)
    options = models.ManyToManyField(Options,blank=True,null=True)
    slug = models.SlugField(null=True,blank=True,)
    
    
    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(Order, self).save(*args, **kwargs)
        
    def __str__(self):
        return self.title