from rest_framework import serializers

from .models import SE,UserDetails

class SESerializer(serializers.ModelSerializer):


    class Meta:
        model = SE
        fields = ['start_time', 'end_time','start_time1', 'end_time1','start_time2', 'end_time2']

        #read_only_fields=('header',)


class UserDetailsSerializer(serializers.ModelSerializer):
    activity_periods = SESerializer(many=False)

    class Meta:
        model = UserDetails
        depth = 5
        fields = ['id','real_name', 'tz','activity_periods',]


    def create(self, validated_data):
        tracks_data = validated_data.pop('activity_periods')
        activity_periods = SE.objects.create(**tracks_data)
        u = UserDetails.objects.create(activity_periods=activity_periods, **validated_data)
        return u
