from rest_framework import serializers
from jquery_ajax_app.models import Post
from DependentDropDownList.models import City, Person
from Language.models import Language, Entry

class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = "__all__"

    def validate_name(self, value):
        if self.instance: 
            existing_post = Post.objects.exclude(pk=self.instance.pk).filter(name=value)
            if existing_post.exists():
                raise serializers.ValidationError("A post with this name already exists.")
        else:
            if Post.objects.filter(name=value).exists():
                raise serializers.ValidationError("A post with this name already exists.")
        return value

    # def create(self, validated_data):
    #     return Post.objects.create(**validated_data)

    # def update(self, instance, validated_data):
    #     instance.name = validated_data.get('name', instance.name)
    #     instance.content = validated_data.get('content', instance.content)
    #     instance.save()
    #     return instance

class PersonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Person
        fields = "__all__"

    # def __init__(self, *args, **kwargs):
    #     super().__init__(*args, **kwargs)
    #     self.fields['city'].queryset = City.objects.none()

    #     if 'country' in self.data:
    #         try:
    #             country_id = int(self.data.get('country'))
    #             self.fields['city'].queryset = City.objects.filter(country_id=country_id).order_by('name')
    #         except (ValueError, TypeError):
    #             pass  # invalid input from the client; ignore and fallback to empty City queryset
    #     elif self.instance.pk:
    #         self.fields['city'].queryset = self.instance.country.city_set.order_by('name')

class LanguageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Entry
        fields = '__all__'