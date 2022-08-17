from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns

from .views import *

# Código de relacionamento das funções de execução de ações com as requisições HTTP e rotas

guests_get_post_put = GuestsViewSet.as_view(
    {
        'get': 'get_guests',
        'post': 'register_guest',
        'put': 'modify_guest'
    }
)

guests_delete = GuestsViewSet.as_view(
    {
        'delete': 'drop_guest'
    }
)

qrcode_get_post_put = QrcodeViewSet.as_view(
    {
        'get': 'get_qrcode',
        'post': 'register_qrcode',
        'put': 'modify_qrcode'
    }
)

qrcode_delete = QrcodeViewSet.as_view(
    {
        'delete': 'drop_qrcode'
    }
)

qrcode_guest_get_delete = QrCodeGuestViewSet.as_view(
    {
        'get': 'get_qrcodes_guests',
        'delete': 'drop_qrcode_guest'
    }
)

qrcode_guest_post_put = QrCodeGuestViewSet.as_view(
    {
        'post': 'register_qrcode_guest',
        'put': 'modify_qrcode_guest'
    }
)

accredited_get_delete = AccreditedViewSet.as_view(
    {
        'get': 'get_guest_accredited',
        'delete': 'drop_guest_accredited'
    }
)

accredited_post_put = AccreditedViewSet.as_view(
    {
        'post': 'register_guest_accredited',
        'put': 'modify_guest_accredited'
    }
)

guests_data_get = GuestsDataAPIView.as_view()

# Definição das rotas
urlpatterns = [
    path(r'guests/', guests_get_post_put, name='guests'),
    path(r'guest/<int:id_guest>', guests_delete, name='guest'),
    path(r'qrcode/', qrcode_get_post_put, name='qrcode'),
    path(r'qrcode/<int:id_qrcode>', qrcode_delete, name='qrcode'),
    path(r'qrcode_guest/<int:id_guest_ext>', qrcode_guest_get_delete, name='qrcode_guest'),
    path(r'qrcode_guest/', qrcode_guest_post_put, name='qrcode_guest'),
    path(r'accredited/<int:id_guest_acc_ext>', accredited_get_delete, name='accredited'),
    path(r'accredited/', accredited_post_put, name='accredited'),
    path(r'guests_data/', guests_data_get, name='guests_data'),
    path(r'guests_data/<str:qrcode_content>', guests_data_get, name='guests_data'),
]

urlpatterns = format_suffix_patterns(urlpatterns)
