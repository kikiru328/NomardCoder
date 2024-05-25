from rest_framework import serializers


class CategorySerializer(serializers.Serializer):
    # 노출 할 property
    pk = serializers.IntegerField()
    name = serializers.CharField(required=True)
    kind = serializers.CharField()
    created_at = serializers.DateTimeField()
