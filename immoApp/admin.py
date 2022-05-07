from django.contrib import admin
from .models import Contact , Customers ,Silder , SiteInfo, House, Agent
from django.utils.safestring import mark_safe


class Contactsviews(admin.ModelAdmin):
    list_display = ('faceLink', 'InstaLink', 'twitterLink','SiteContact', 'WaltLink', 'linkedLink', 'mainPhone', 'email', 'lat','lomge')
admin.site.register(Contact, Contactsviews)

class SiteViews(admin.ModelAdmin):
    list_display = ('title', 'mainColor', 'fullSiteColor')
admin.site.register(SiteInfo, SiteViews)


class Sliderviews(admin.ModelAdmin):
    list_display = ('title1', 'title2', 'title3','Img1', 'Img2', 'Img3')
    
    def views(self , obj):    
        return mark_safe(f'<img src="{obj.image.url}" style="height:100px; width:200px">')  

admin.site.register(Silder, Sliderviews)

class HouseViews(admin.ModelAdmin):
    list_display = ('rooms', 'garage', 'toillets', 'addressName', 'lat', 'long')

admin.site.register(House, HouseViews)

class Customerviews(admin.ModelAdmin):
    list_display = ('nom', 'prenom', 'email', 'birthday', 'phone', 'image', 'username', 'password')
    
    def views(self , obj):    
        return mark_safe(f'<img src="{obj.image.url}" style="height:100px; width:200px">')  

admin.site.register(Customers, Customerviews)

class AgentViews(admin.ModelAdmin):
    list_display = ('biography', 'image', 'fb_link', 'insta_link', 'twitter_link')

admin.site.register(Agent, AgentViews)

# Register your models here.
