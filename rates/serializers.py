from rest_framework import serializers


class CurrencyConverterSerializer(serializers.Serializer):
    _from = serializers.CharField()
    to = serializers.CharField()
    value = serializers.FloatField()

    def get_fields(self):
        fields = super().get_fields()
        fields["from"] = fields.pop("_from")
        return fields
