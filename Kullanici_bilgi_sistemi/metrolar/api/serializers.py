from rest_framework import serializers
from metrolar.models import Metro 


class MetroSerializers(serializers.Serializer):  
    id  = serializers.IntegerField()   
    Name = serializers.CharField()
    LineId = serializers.IntegerField()
    LineName = serializers.CharField()
    Description = serializers.CharField()
    Order = serializers.IntegerField()
    IsActive = serializers.BooleanField()
    BabyRoom =  serializers.BooleanField()
    WC = serializers.BooleanField()
    Masjid = serializers.BooleanField()
    Longitude = serializers.FloatField()
    Latitude = serializers.FloatField()


    def create(self, validated_data):
        print(validated_data)
        return Metro.objects.create(**validated_data) 
    
    """modelimizdeki verimizi güncellemek için, instance.yazar ile "yazar" verimizi al,
           validated_data.get ile yazar bölümüne yaz, EĞER  instance.yazar da bir değişiklik
           yoksa ,instance.yazar kısmını yani önceki yazar verisini yaz
    """
      
    def update(self, instance, validated_data):
        instance.id = validated_data.get('id',instance.id)
        instance.Name = validated_data.get('Name',instance.Name)
        instance.LineId = validated_data.get('LineId',instance.LineId)
        instance.LineName = validated_data.get('LineName',instance.LineName)
        instance.Description = validated_data.get('Description',instance.Description)
        instance.Order = validated_data.get('Order',instance.Order)
        instance.IsActive = validated_data.get('IsActive',instance.IsActive)
        instance.BabyRoom = validated_data.get('BabyRoom',instance.BabyRoom)
        instance.WC = validated_data.get('WC',instance.WC)
        instance.Masjid = validated_data.get('Masjid',instance.Masjid)
        instance.Longitude = validated_data.get('Longitude',instance.Longitude)
        instance.Latitude = validated_data.get('Latitude',instance.Latitude)

        instance.save()
        return instance






