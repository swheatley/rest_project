from rest_framework import serializers

from main.models import Phone


class PhoneSerializer(serializers.ModelSerializer):

    class Meta:
        model = Phone
