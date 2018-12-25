import urllib.request
import datetime
from django.shortcuts import render
from django.views.generic import CreateView, ListView
from Robot.main.forms import URLForm
from Robot.main.models import Site


class URLCreateView(CreateView):
    template_name = 'create_url.html'
    form_class = URLForm
    success_url = '/list/'


class URLListView(ListView):
    model = Site
    template_name = 'url_list.html'


def main(request):
    context = {}
    if request.POST:
        date = request.POST.get('calendar', '')
        urls = Site.objects.exclude(date__gt=date)
        for site in urls:
            url = site.url
            code = urllib.request.urlopen(url).getcode()
            site.date = datetime.datetime.today().strftime('%Y-%m-%d')
            site.status = code
            site.save()
        return render(request, "main.html", context)
    else:
        return render(request, "main.html", context)
