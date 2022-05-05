from pyexpat import model
from django.db import models

#Fronts table

class SiteInfo(models.Model):
    title = models.CharField(max_length=200)
    mainColor = models.CharField(max_length=200)
    fullSiteColor = models.CharField(max_length=200)

class Contact(models.Model):
    faceLink = models.CharField(max_length=200)    
    InstaLink = models.CharField(max_length=200)    
    twitterLink = models.CharField(max_length=200)    
    SiteContact= models.CharField(max_length=200)    
    WaltLink = models.CharField(max_length=200)    
    linkedLink = models.CharField(max_length=200)    
    mainPhone = models.CharField(max_length=200)    
    email = models.EmailField(max_length=200)    
    lat = models.CharField(max_length=200)    
    lomge = models.CharField(max_length=200)  

class Silder(models.Model):
    Img1 = models.ImageField()
    Img2 = models.ImageField()
    Img3 = models.ImageField()
    title1 = models.CharField(max_length=200)
    title2 = models.CharField(max_length=200)
    title3 = models.CharField(max_length=200)

#App User

class Customers(models.Model):
    nom = models.CharField(max_length=200)
    nom = models.CharField(max_length=200)
    nom = models.CharField(max_length=200)
    nom = models.CharField(max_length=200)
    nom = models.CharField(max_length=200)
    nom = models.CharField(max_length=200)
    nom = models.CharField(max_length=200)

    def __str__(self):
        return self.nom


# Create your models here.
