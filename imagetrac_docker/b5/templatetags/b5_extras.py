from django import template
from django.contrib.auth.models import Group

register = template.Library()

@register.filter
def get_item(dictionary, key):
	return dictionary.get(key)

@register.filter(name='has_group') 
def has_group(user, group_name):
	try: 
		group = Group.objects.get(name__iexact=group_name)
	except:
		return False
	return True if group in user.groups.all() else False