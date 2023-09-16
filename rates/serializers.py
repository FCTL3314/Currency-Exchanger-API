from rest_framework import serializers


class CurrencyConverterSerializer(serializers.Serializer):
    _from = serializers.CharField()
    to = serializers.CharField()
    value = serializers.FloatField()
