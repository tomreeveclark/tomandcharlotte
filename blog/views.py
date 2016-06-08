from django.shortcuts import render
from models import Image

# Create your views here.

def blog(request):

	# Nothing here, yet!
	images = Image.objects.all()

	context_dict={'images':images}

	return render(request, 'blog/blog.html', context_dict)