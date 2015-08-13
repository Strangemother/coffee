from django.views.generic import TemplateView, ListView, CreateView, DetailView
from django.views.generic.detail import BaseDetailView
from models import Company, Venue, Booking, Location, Event, Menu, Product, Category, OpeningTime
from forms import VenueForm

from simple_rest.auth.decorators import login_required, admin_required
from django.http import HttpResponse
from django.core import serializers
#from json import dumps
# import json
# from simple_rest.response import RESTfulResponse
from django.contrib import messages
from django import http
from django.utils import simplejson as json
from datetime import datetime
from django.core import serializers


class JSONResponseMixin(object):
    def render_to_response(self, context):
        "Returns a JSON response containing 'context' as payload"
        return self.get_json_response(self.convert_context_to_json(context))

    def get_json_response(self, content, **httpresponse_kwargs):
        "Construct an `HttpResponse` object."
        return http.HttpResponse(content,
                                 content_type='application/json',
                                 **httpresponse_kwargs)

    def convert_context_to_json(self, context):
        "Convert the context dictionary into a JSON object"
        # Note: This is *EXTREMELY* naive; in reality, you'll need
        # to do much more complex handling to ensure that arbitrary
        # objects -- such as Django model instances or querysets
        # -- can be serialized as JSON.
        return json.dumps(self.json_data(context))

    def json_data(self, content):
        return {}

class JSONDetailView(JSONResponseMixin, TemplateView):

    def render_to_response(self, context):
        return JSONResponseMixin.render_to_response(self, context)


class IndexView(TemplateView):
    template_name ='reserved/index.html'


class ContactView(TemplateView):
    template_name = 'reserved/contact.html'

    def open_times(self):
        op = OpeningTime.objects.filter(active=True)
        return op

    def address(self):
        l = Location.objects.get(location_id='default')
        return l

base_keys = ['id', 'name', 'active', 'icon_name']
product_keys = base_keys + ['categories', 'price']
category_keys = base_keys + ['parent']

def short_object(object, keys, *args, **kw):
    '''
    return an object of defined keys
        short_object(o, ['', ...])
        short_object(o, ['', ...], 'key', 'key', ... )
    '''
    o = {}
    def key(object, k):
        decoder = kw.get(k)
        d = getattr(object, k)
        if decoder is not None and d is not None:
            d = decoder(d, object)
        return d
    ks =  [x for x in args] + keys

    for k in ks:
        o[k] = key(object, k)
    return o


def short_models(filtered, keys):
    o =[]
    for m in filtered:
        p = short_object(m, keys, **decoders)
        o.append(p)
    return o


def categories_decoder(object, parent):
    res = []
    for cat in object.all():
        c= short_object(cat, base_keys, **decoders)
        res.append(c)
    return res

def category_decoder(object, parent):
    o = {}
    for k in category_keys:
        o[k] = getattr(object, k)
    return o


decoders = {
    'categories': categories_decoder,
    'category': category_decoder,
    'parent': category_decoder,
}

def menu_json():

    menus = Menu.objects.filter()
    products = Product.objects.filter()
    categories = Category.objects.filter()

    o = {}
    o['menu'] = short_models(menus, base_keys)
    o['products'] = short_models(products, product_keys)
    o['categories'] = short_models(categories, category_keys)

    return o


class MenuJson(JSONDetailView):
    model = Menu

    def json_data(self, context):
        return menu_json()


class MenuData(TemplateView):
    template_name = 'reserved/menu_data.js'
    content_type = 'application/javascript'

    def json(self, **kw):
        return json.dumps( menu_json() )

class MenuList(ListView):
    model = Menu


class CompanyList(ListView):
    model = Company


class VenueCreate(CreateView):
    model = Venue
    form_class = VenueForm

    def form_valid(self, form):
        # This method is called when valid form data has been POSTed.
        # It should return an HttpResponse.
        # form.send_email()
        venue = form.save()
        self.form_id = venue.id
        ll = form.cleaned_data.get('latlng', None)
        full_address = form.cleaned_data.get('full_address', None)
        # import pdb; pdb.set_trace()
        if ll and full_address:
            lat, lng = ll.split(',')

            location, created = Location.objects.get_or_create(address=full_address)
            if created is True:
                location.name=venue.name
                location.latitude=lat
                location.longitude=lng
                location.save()
            venue.address = location
        venue.owner = self.request.user
        venue.save()
        messages.success(self.request, 'New venue \'%s\' created' % (venue))
        return super(VenueCreate, self).form_valid(form)

    def get_success_url(self):
        return '/venues/'
        return '/venues/created/%s' % self.form_id


class VenueList(ListView):
    model = Venue

    def get_context_data(self, **kwargs):
        kwargs['venues_owned'] = self.model.objects.filter(owner=self.request.user)
        kwargs['venues_other'] = self.model.objects.filter(contact__email=self.request.user.email)
        return kwargs


class VenueCalendarView(TemplateView):
    template_name = 'reserved/venue_calendar.html'


class EventList(ListView):
    model = Event


class BookingList(ListView):
    model = Booking

    def get_queryset(self):
        return self.model.objects.all()


class BookingCreate(CreateView):
    model = Booking
    success_url = '/bookings/'

class EventCreate(CreateView):
    model = Event
    success_url = '/events/'


class BookingDetail(DetailView):
    slug_field = 'name'
    model = Booking

