from rest_framework import serializers
from trainsapp.models import AllTrain

class AllTrainSerializers(serializers.ModelSerializer):
    class Meta:
        model = AllTrain
        fields = "__all__"