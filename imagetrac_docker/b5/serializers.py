from rest_framework import serializers
from . import models

class ProductSerializer(serializers.ModelSerializer):
	class Meta:
		model = models.RumbaProduct
		fields = ('id', 'item_no', 'mfg', 'desc', 'vendor_number', 'confirmed_placed',
		 'short_sku', 'sku', 'product_class', 'merch_to_137', 'curr_dc_oh_u', 
		 'size', 'color_desc',
		 )

class ItemSerializer(serializers.ModelSerializer):
	class Meta:
		model = models.HotItem
		fields = ('id', 'item_no', 'ad_date', 'create_date', 'item_name',
		 'comments', 'reply', 'confirmed_placed',
		 )



# # from teamtreehouse

# class ReviewSerializer(serializers.ModelSerializer):
#   class Meta:
#     extra_kwargs = {
#       'email': {'write_only': True}
#     }
#     fields = (
#       "id",
#       "course",
#       "name",
#       "email",
#       "comment",
#       "rating",
#       "created_at"
#     )
#     model = Review
    
#   def validate_rating(self, value):
#     if value in range(1,6):
#       return value
#     else:
#       raise serializers.ValidationError("Rating must be an integer between 1 and 5")
    
# class CourseSerializer(serializers.ModelSerializer):
#   reviews = serializers.HyperlinkedRelatedField( 
#     many=True, 
#     read_only=True,
#     view_name="apiv2:review-detail"
#   )
#   class Meta:
#     fields = (
#       "id",
#       "title",
#       "url",
#       "reviews",
#     )
#     model = Course