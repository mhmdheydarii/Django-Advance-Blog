from rest_framework import serializers
from blog.models import Post, Category
from accounts.models import Profile


class CategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = Category
        fields = ['id', 'name']

class PostSerializer(serializers.ModelSerializer):
    
    snippet = serializers.ReadOnlyField(source='get_snippet')
    absolute_url = serializers.SerializerMethodField(method_name='get_absolute_url')
    category = serializers.SlugRelatedField(many=False, slug_field='name', queryset=Category.objects.all())


    class Meta:
        model = Post
        fields = ['id','title','content','snippet','absolute_url','category','author','published_date','status']
        read_only_fields = ['author']

    # Adding the post URL on the post list page
    def get_absolute_url(self, obj):
        request = self.context.get('request')
        return request.build_absolute_uri(obj.id)
    
    # Filtering posts based on list and detail pages
    def to_representation(self, instance):
        request = self.context.get('request')
        rep = super().to_representation(instance)
        if request.parser_context.get('kwargs').get('pk'):
            rep.pop('snippet', None)
            rep.pop('absolute_url', None)
        else:
            rep.pop('content', None)
        rep['category'] = CategorySerializer(instance.category, context={'request':request}).data
        return rep
    
    # Creating a post without listing listing users
    def create(self, validated_data):
        validated_data['author'] = Profile.objects.get(user__id=self.context.get('request').user.id)
        return super().create(validated_data)




    

    