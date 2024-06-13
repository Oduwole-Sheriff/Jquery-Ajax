from rest_framework import serializers
from .models import Post

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
