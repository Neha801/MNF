from django.http import HttpResponse
from django.shortcuts import redirect
from django.template.defaultfilters import slugify


def unauthenticated_user(view_func):
	def wrapper_func(request, *args, **kwargs):
		if request.user.is_authenticated:
			return redirect('palak:script_info')
		else:
			return view_func(request, *args, **kwargs)

	return wrapper_func

