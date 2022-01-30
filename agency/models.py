from django.db import models

# Create your models here.
from django.utils.translation import ugettext_lazy as _


class Destination(models.Model):
    name = models.CharField(_("name"), max_length=50)
    image = models.ImageField(_("image"), upload_to='destinations')
    price = models.DecimalField(_("price"), max_digits=5, decimal_places=2)
    description = models.TextField(_("description"))
    created_at = models.DateTimeField(_("created at"),auto_now_add=True)
    

    
    class Meta:
        verbose_name = _("Destination")
        verbose_name_plural = _("Destinations")

    def __str__(self):
        return self.name

