
from rest_framework import serializers

# import movie models
from watchlist_app.models import WatchList, StreamPlatform

#movie serializers
class WatchListSerializer(serializers.ModelSerializer):
   
    class Meta:
        model: WatchList
        fields = "__all__"

    

class StreamPlatformSerializer(serializers.ModelSerializer):
     class Meta:
        model: StreamPlatform
        fields = "__all__"