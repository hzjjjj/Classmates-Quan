from django.shortcuts import render
from django.http import HttpResponse, Http404
from django.template import loader
from classmates.models import Quan
from classmates.models import QuanTypes
from .forms import QuanForm

def quanlist(request):
    quan_list = Quan.objects.order_by('quan_created_date')
    template = loader.get_template('quan.html')
    context = {'quan_list':quan_list}

    for quan in quan_list:
        quan.quan_type = QuanTypes[quan.quan_type]

    return HttpResponse(template.render(context))

def quanlistid(request,id):
    quan_list = Quan.objects.filter(quan_type=id)
    template = loader.get_template('quan.html')
    context = {'quan_list':quan_list}

    for quan in quan_list:
        quan.quan_type = QuanTypes[quan.quan_type]

    return HttpResponse(template.render(context))

def quanread(request,id):
    try:
        quan = Quan.objects.get(pk=id)

        quan.quan_type = QuanTypes[quan.quan_type]
    except Quan.DoesNotExist:
        raise Http404("同学圈文章不存在")

    return render(request, 'read.html', {'quan':quan})

def quan_create_view(request):
    form = QuanForm(request.POST or None)
    if form.is_valid():
        form.save()
        form = QuanForm()

    context = {
        'form': form
    }

    return render(request, 'add_quan.html', context)