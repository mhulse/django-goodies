from django.db import models
from django.contrib.localflavor.us.models import *
from django.utils.translation import ugettext_lazy as _
from goodies.helpers import get_lat_lng

class Place(models.Model):
    
    title    = models.CharField(_(u'title'), max_length=255)
    address1 = models.CharField(_(u'address'), max_length=255, blank=True)
    address2 = models.CharField(_(u'address (cont.)'), max_length=255, blank=True)
    city     = models.CharField(_(u'city'), max_length=255, blank=True)
    state    = USStateField(_(u'state'), blank=True)
    zip      = models.CharField(_(u'ZIP'), max_length=10, blank=True)
    country  = models.CharField(_(u'country'), blank=True, max_length=100)
    latlng   = models.CharField(_(u'Lat/Lon'), blank=True, max_length=100, help_text=_(u'Note: This field will be filled-in automatically based on the other address bits.'))
    phone    = PhoneNumberField(_(u'phone'), blank=True)
    email    = models.EmailField(_(u'e-mail'), blank=True)
    website  = models.URLField(_(u'website'), blank=True)
    about    = models.TextField(_(u'about'), blank=True)
    
    class Meta:
        abstract = True
    
    def save(self, *args, **kwargs):
        # If latlng has no value:
        if not self.latlng:
            # Add + between fields with values:
            location = '+'.join(filter(None, (self.address1, self.address2, self.city, self.state, self.zip, self.country)))
            # Attempt to get latitude/longitude from Google Geocoder service v.3:
            self.latlng = get_lat_lng(location)
        super(Place, self).save(*args, **kwargs)
    
    def get_lat_lng(self):
        if self.latlng:
            return self.latlng.split(',')