from abc import ABC

from django.db import connection
from rest_framework import serializers
from .models import Guests, Qrcode, QrCodeGuest, Accredited


# Seriador do modelo Guests
class GuestsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Guests
        fields = '__all__'


# Seriador do modelo Qrcode
class QrcodeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Qrcode
        fields = '__all__'


# Seriador do modelo QrCodeGuest
class QrCodeGuestSerializer(serializers.ModelSerializer):
    class Meta:
        model = QrCodeGuest
        fields = '__all__'


# Seriador do modelo Accredited
class AccreditedSerializer(serializers.ModelSerializer):
    class Meta:
        model = Accredited
        fields = '__all__'
