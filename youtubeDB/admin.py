from django.contrib import admin

from .models import MyYotubeVideos,SubscriberStories,YoutubeEvents,MileStones

# Register your models here.
admin.site.register(MyYotubeVideos)
admin.site.register(SubscriberStories)
admin.site.register(YoutubeEvents)
admin.site.register(MileStones)