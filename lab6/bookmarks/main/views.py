from django.shortcuts import render
from django.shortcuts import render_to_response
from django.shortcuts import redirect
from django.template import RequestContext

from main.models import Link, Tag

# Create your views here.

def index(request):
	#Request context
	context = RequestContext(request)

	#Get links
	links = Link.objects.all()

	return render_to_response('main/index.html', {'links': links}, context)

def tags(request):
	context = RequestContext(request)

	#Get tags
	tags = Tag.objects.all()

	return render_to_response('main/tags.html', {'tags': tags}, context)

def tag(request, tag_name):
	context = RequestContext(request)
	the_tag = Tag.objects.get(name=tag_name)
	links = the_tag.link_set.all()
	return render_to_response('main/index.html', {'links':links, 'tag_name':'#'+tag_name})

def add_link(request):
	context = RequestContext(request)
	if request.method == 'POST':
		url = request.POST.get("url", "")
		tags = request.POST.get("tags","")
		title = request.POST.get("title", "")
		#Code here
		
		link = Link()
		link.url = url
		link.title = title
		link.save()
		
		for each in tags.split(','):
			the_tag = each.strip()
		try:
			link.tags.add(Tag.objects.get(name=the_tag))
		except:
			pass		
			
		link.save()
	return redirect(index)
