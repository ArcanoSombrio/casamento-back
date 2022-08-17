from django.contrib import admin
from .models import Guests, Qrcode, QrCodeGuest, Accredited

# Registro do site na página de administrador do Django
admin.site.register(Guests)
admin.site.register(Qrcode)
admin.site.register(QrCodeGuest)
admin.site.register(Accredited)
