from django.db import models

# Create your models here.
class Client(models.Model):
    c_id = models.AutoField(primary_key = True)
    username = models.CharField(max_length=20)
    fname = models.CharField(max_length=30)
    lname = models.CharField(max_length=30)
    contact = models.IntegerField()
    age = models.PositiveIntegerField()
    balance = models.IntegerField()
    password = models.CharField(max_length=30)

    def __str__(self):
        return self.username 

class Company(models.Model):
    company_id = models.AutoField(primary_key = True)
    username = models.CharField(max_length = 20)
    company_name = models.CharField(max_length=20)
    password = models.CharField(max_length=30)
    email = models.EmailField(max_length=30)
    website = models.CharField(max_length=30)

    def __str__(self):
        return self.company_name

class Company_assets(models.Model):
    company_id = models.ForeignKey(Company, on_delete=models.CASCADE, related_name='companyasset',primary_key = True)
    price = models.PositiveIntegerField()
    total_shares = models.IntegerField()
    net_worth = models.IntegerField()

    def __str__(self):
        return self.company_id.company_name

class Demat(models.Model):
    c_id = models.ForeignKey(Client,on_delete=models.CASCADE)
    company_id = models.ForeignKey(Company,on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()

    def __str__(self):
        return self.c_id.username

class IPO(models.Model):
    company_id = models.ForeignKey(Company, on_delete=models.CASCADE,primary_key = True)
    price = models.PositiveIntegerField()
    remaining = models.PositiveIntegerField()

    def __str__(self):
        return self.company_id.company_name


class Market(models.Model):
    Seller_id = models.ForeignKey(Client,on_delete=models.CASCADE)
    Company_id = models.ForeignKey(Company,on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()
    price = models.PositiveIntegerField()

    def __str__(self):
        return str(self.Seller_id)

class Transaction(models.Model):
    Transaction_id = models.AutoField(primary_key = True)
    Seller_id = models.ForeignKey(Market,on_delete=models.CASCADE)
    Buyer_id = models.ForeignKey(Client,on_delete=models.CASCADE)
    Company_id = models.ForeignKey(Company,on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()
    amount = models.PositiveIntegerField()

    def __str__(self):
        return str(self.Seller_id.Seller_id.username)+str(" Sells ")+str(self.quantity)+str(" ")+str(self.Company_id.company_name)+str(" shares to ")+str(self.Buyer_id.username)