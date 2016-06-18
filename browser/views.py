from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.views import generic
from django.conf import settings

from .models import Gtin, Brand, Owner, Search, Label, Orga
from django.db.models import Count

# --------------------------------------------------------------------
#  WEBSITE BROWSER
# --------------------------------------------------------------------
import requests

def search_gtin(request):

    if request.POST['gtin']:
        gtin_in = request.POST['gtin']
        if len(gtin_in) == 8 or len(gtin_in) == 12 or len(gtin_in) == 13:
            if len(gtin_in) == 8:
                gtin_in = '00000' + gtin_in
            if len(gtin_in) == 12:
                gtin_in = '0' + gtin_in
        else:
            return render(request, 'browser/home.html', {
                'error_message': "Please enter 8, 12 or 13 digits",
            })
    else:
        return render(request, 'browser/home.html', {
            'error_message': "please enter a correct gtin code",
        })

    if Search.objects.filter(pk=gtin_in).exists():
        search_gtin = Search.objects.get(pk=gtin_in)
        search_gtin.SEARCH_NB += 1
        search_gtin.save()
    else:
        new_entry = Search(GTIN_CD = gtin_in, SEARCH_NB = 1)
        new_entry.save()

    try:
            gtin = Gtin.objects.get(GTIN_CD=gtin_in)
    except (KeyError, Gtin.DoesNotExist):
        return render(request, 'browser/gtin-error.html', {
            'gtin': gtin_in,
        })
    else:
        return HttpResponseRedirect(reverse('browser:result', args=(gtin.GTIN_CD,)))

def search_gtin2(request,gtin):

    if gtin:
        gtin_in = gtin
        if len(gtin_in) == 8 or len(gtin_in) == 12 or len(gtin_in) == 13:
            if len(gtin_in) == 8:
                gtin_in = '00000' + gtin_in
            if len(gtin_in) == 12:
                gtin_in = '0' + gtin_in
        else:
            return render(request, 'browser/home.html', {
                'error_message': "Please enter 8, 12 or 13 digits",
            })
    else:
        return render(request, 'browser/home.html', {
            'error_message': "please enter a correct gtin code",
        })

    if Search.objects.filter(pk=gtin_in).exists():
        search_gtin = Search.objects.get(pk=gtin_in)
        search_gtin.SEARCH_NB += 1
        search_gtin.save()
    else:
        new_entry = Search(GTIN_CD = gtin_in, SEARCH_NB = 1)
        new_entry.save()

    try:
            gtin = Gtin.objects.get(GTIN_CD=gtin_in)
    except (KeyError, Gtin.DoesNotExist):
        return render(request, 'browser/gtin-error.html', {
            'gtin': gtin_in,
        })
    else:
        return HttpResponseRedirect(reverse('browser:result', args=(gtin.GTIN_CD,)))

class ViewResultGtin(generic.ListView):
    template_name = 'browser/gtin-result.html'
    context_object_name = 'gtin_list'
    model = Gtin

    def get_queryset(self):
        gtin = self.kwargs['gtin']
        return Gtin.objects.filter(GTIN_CD=gtin)


class ViewGtin(generic.DetailView):
    template_name = 'browser/gtin.html'
    model = Gtin

    queryset = Gtin.objects.all()

    def get_object(self):
        object = super(ViewGtin, self).get_object()
        if object.GTIN_CD and object.GTIN_CD[0:1] == "0":
            object.UPC_CD = object.GTIN_CD[1:12]
        object.save()
        return object

class ViewBrandList(generic.ListView):
    template_name = 'browser/brand_list.html'
    context_object_name = 'page_brand_list'
    model = Brand

    def get_queryset(self):
        return Brand.objects.filter(BRAND_DISPLAY=True).order_by('BRAND_COUNTRY_ISO','BRAND_NM')

class ViewBsin(generic.ListView):
    template_name = 'browser/bsin.html'
    context_object_name = 'gtin_list'
    model = Gtin

    def get_context_data(self, **kwargs):
        context = super(ViewBsin, self).get_context_data(**kwargs)
        context.update({
            'bsin_detail': Brand.objects.get(pk=self.kwargs['bsin']),
            #'gtin_count' : Gtin.objects.values('GCP_CD__GLN_COUNTRY_ISO_CD').annotate(dcount=Count('GTIN_CD'))
        })
        return context

    def get_queryset(self):
        bsin = self.kwargs['bsin']
        return Gtin.objects.filter(BSIN=bsin).order_by('METHOD_CD','PKG_UNIT','SIZE_CD')


class ViewStats(generic.ListView):
    template_name = 'browser/stats.html'
    context_object_name = 'stats_data'
    model = Gtin

    def get_context_data(self, **kwargs):
        context = super(ViewStats, self).get_context_data(**kwargs)
        context.update({
            'gtin_total_count' : Gtin.objects.aggregate(Count('GTIN_CD')),
            'gtin_count' : Gtin.objects.values('GCP_CD__GLN_COUNTRY_ISO_CD').annotate(dcount=Count('GRADE_CD')).order_by('dcount')
        })
        return context

    def get_queryset(self):
        return Gtin.objects.values('GCP_CD__GLN_COUNTRY_ISO_CD').annotate(dcount=Count('GTIN_CD'))


class ViewOwnerList(generic.ListView):
    template_name = 'browser/owner_list.html'
    context_object_name = 'owner_list'
    model = Owner

    def get_queryset(self):
        """Return the last five published questions."""
        return Owner.objects.order_by('OWNER_COUNTRY_ISO','OWNER_NM')

class ViewOwner(generic.ListView):
    template_name = 'browser/owner.html'
    context_object_name = 'brand_list'
    model = Brand

    def get_context_data(self, **kwargs):
        context = super(ViewOwner, self).get_context_data(**kwargs)
        context.update({
            'owner_detail': Owner.objects.get(pk=self.kwargs['owner']),
        })
        return context

    def get_queryset(self):
        owner = self.kwargs['owner']
        return Brand.objects.filter(OWNER_CD=owner).order_by('BRAND_NM')



class ViewLabelList(generic.ListView):
    template_name = 'browser/label_list.html'
    context_object_name = 'label_list'
    model = Label

    def get_queryset(self):
        return Label.objects.order_by('LABEL_COUNTRY_ISO','LABEL_NM')

class ViewLabel(generic.DetailView):
    template_name = 'browser/label.html'
    model = Label

    queryset = Label.objects.all()

class ViewOrgaList(generic.ListView):
    template_name = 'browser/orga_list.html'
    context_object_name = 'orga_list'
    model = Orga

    def get_queryset(self):
        return Orga.objects.order_by('ORGA_COUNTRY_ISO','ORGA_NM')

class ViewOrga(generic.DetailView):
    template_name = 'browser/orga.html'
    model = Orga

    queryset = Orga.objects.all()

# --------------------------------------------------------------------
#   REST API DRF
# --------------------------------------------------------------------

# gtin for test : 0836093401314    0857063002652
