from django.shortcuts import render, get_object_or_404, render_to_response

# Create your views here.

from django.http import Http404
from django.template import RequestContext, loader
from django.http import HttpResponse
from .models import Law, textLaw


def index(request):
	latest_question_list = Law.objects.order_by('-date_last_revision')[:5]
	template = loader.get_template('changelist/index.html')
	output = ', '.join([p.name for p in latest_question_list])
	return HttpResponse(output)

def detaillaw(request, id):
	lawhistory = get_object_or_404(Law, id=id)
	return render_to_response('changelist/detail.html',{'lawhistory': lawhistory})
