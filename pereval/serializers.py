from urllib.parse import urlparse

from .models import *
from rest_framework import serializers


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['email', 'fam', 'name', 'otc', 'phone', ]

    def save(self, **kwargs):
        self.is_valid()
        user = User.objects.filter(email=self.validated_data.get('email'))
        if user.exists():
            return user.first()
        else:
            new_user = User.objects.create(
                email=self.validated_data.get('email'),
                fam=self.validated_data.get('fam'),
                name=self.validated_data.get('name'),
                otc=self.validated_data.get('otc'),
                phone=self.validated_data.get('phone'),
            )
            return new_user


class CoordSerializer(serializers.ModelSerializer):
    class Meta:
        model = Coord
        fields = ['latitude', 'longitude', 'height']


class LevelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Level
        fields = ['winter', 'spring', 'summer', 'autumn', ]


class ImageSerializer(serializers.ModelSerializer):
    data = serializers.URLField()

    class Meta:
        model = Image
        fields = ['data', 'title']


class PerevalAddedSerializer(serializers.HyperlinkedModelSerializer):
    user = UserSerializer()
    coord = CoordSerializer()
    level = LevelSerializer(allow_null=True)
    image = serializers.URLField(required=False, allow_null=True)

    class Meta:
        model = PerevalAdded
        fields = ['id', 'beauty_title', 'title', 'other_title', 'connect', 'add_time', 'user', 'coord', 'level',
                  'image']

    def create(self, validated_data, **kwargs):
        user_data = validated_data.pop('user')
        coord_data = validated_data.pop('coord')
        level_data = validated_data.pop('level')
        image_data = validated_data.pop('image', None)

        user, created = User.objects.get_or_create(**user_data)
        coord = Coord.objects.create(**coord_data)
        level = Level.objects.create(**level_data)

        pereval = PerevalAdded.objects.create(user=user, coord=coord, level=level, status="NW", **validated_data)

        if image_data:
            for i in image_data:
                title = i.pop('title')
                data = i.pop('data')
                Image.objects.create(pereval=pereval, data=data, title=title)
        return pereval
