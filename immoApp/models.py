from django.db import models

class SiteInfo(models.Model):
    title = models.CharField(max_length=200)
    mainColor = models.CharField(max_length=200)
    fullSiteColor = models.CharField(max_length=200)

    
    class Meta():
        verbose_name = 'Site Info'
        verbose_name_plural = 'Site Infos'
    
    def __str__(self):
        return self.title


class Contact(models.Model):
    faceLink = models.CharField(max_length=100) 
    InstaLink = models.CharField(max_length=200)    
    twitterLink = models.CharField(max_length=200)    
    SiteContact= models.CharField(max_length=200)    
    WaltLink = models.CharField(max_length=200)    
    linkedLink = models.CharField(max_length=200)    
    mainPhone = models.CharField(max_length=200)    
    email = models.EmailField(max_length=200)    
    lat = models.CharField(max_length=200)    
    lomge = models.CharField(max_length=200)  
    
    class Meta():
        verbose_name = 'Contact'
        verbose_name_plural = 'Contacts'
    
    def __str__(self):
        return self.faceLink

    

class Silder(models.Model):
    title1 = models.CharField(max_length=100)
    title2 = models.CharField(max_length=200)
    title3 = models.CharField(max_length=200)
    Img1 = models.FileField()
    Img2 = models.FileField()
    Img3 = models.FileField()

    class Meta():
        verbose_name = 'Silder Image & Title'
        verbose_name_plural = 'Silder Images & Titles'
    
    
    def __str__(self):
        return self.title1



class Customers(models.Model):
    nom = models.CharField(max_length=200)
    prenom = models.CharField(max_length=100)
    email = models.EmailField(max_length=200)
    birthday = models.CharField(max_length=100)
    phone = models.CharField(max_length=100)
    image = models.FileField()
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    
    class Meta():
        verbose_name = 'Customer'
        verbose_name_plural = 'Customers'

    def __str__(self):
        return self.nom

    

class Agent(models.Model):
    biography = models.CharField(max_length=500)
    image = models.FileField()
    fb_link =  models.CharField(max_length=200) 
    insta_link = models.CharField(max_length=200) 
    twitter_link = models.CharField(max_length=200)
    
    class Meta():
        verbose_name = 'Agent'
        verbose_name_plural = 'Agents'
    
    def __str__(self):
        return self.biography 
    


class House(models.Model):
    rooms = models.CharField(max_length=100)
    garage = models.CharField(max_length=100)
    toillets = models.CharField(max_length=100)
    addressName = models.CharField(max_length=100)
    lat = models.CharField(max_length=100)
    long = models.CharField(max_length=100)


    class Meta():
        verbose_name = 'Maison'
        verbose_name_plural = 'Maisons'

    def __str__(self):
        return self.rooms


