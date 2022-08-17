from django.db import connection
from rest_framework import viewsets, permissions
from rest_framework.decorators import api_view
from rest_framework.generics import GenericAPIView
from rest_framework.mixins import ListModelMixin
from rest_framework.response import Response
from rest_framework.views import APIView

from .serializers import GuestsSerializer, QrcodeSerializer, QrCodeGuestSerializer, AccreditedSerializer
from .models import Guests, Qrcode, QrCodeGuest, Accredited
from .orm import ORM


# Classe onde serão realizadas as operações de requisições no modelo Guests
class GuestsViewSet(viewsets.ModelViewSet):
    model = Guests
    queryset = Guests.objects
    serializer_class = GuestsSerializer

    # Método que executa uma requisição HTTP GET para listagem dos convidados
    def get_guests(self, request):
        return ORM.list_all_guests(GuestsViewSet.queryset)

    # Método que executa uma requisição HTTP POST para cadastro dos convidados
    def register_guest(self, request):
        return ORM.create_guest(GuestsViewSet.queryset, json_values=request.data)

    # Método que executa uma requisição HTTP PUT para atualização dos convidados
    def modify_guest(self, request):
        return ORM.update_guest_with_id(GuestsViewSet.queryset, json_values=request.data)

    # Método que executa uma requisição HTTP DELETE para exclusão dos convidados
    def drop_guest(self, request, id_guest):
        return ORM.destroy_guest_with_id(GuestsViewSet.queryset, json_values={"id_guest": id_guest})


# Classe onde serão realizadas as operações de requisições no modelo Qrcode
class QrcodeViewSet(viewsets.ModelViewSet):
    model = Qrcode
    queryset = Qrcode.objects
    serializer_class = QrcodeSerializer

    # Método que executa uma requisição HTTP GET para listagem dos qrcodes
    def get_qrcode(self, request):
        return ORM.list_all_qrcodes(QrcodeViewSet.queryset)

    # Método que executa uma requisição HTTP POST para cadastro de qrcode
    def register_qrcode(self, request):
        return ORM.create_qrcode(QrcodeViewSet.queryset, json_values=request.data)

    # Método que executa uma requisição HTTP PUT para atualização de qrcode
    def modify_qrcode(self, request):
        return ORM.update_qrcode_with_id(QrcodeViewSet.queryset, json_values=request.data)

    # Método que executa uma requisição HTTP DELETE para exclusão de qrcode
    def drop_qrcode(self, request, id_qrcode):
        return ORM.destroy_qrcode_with_id(QrcodeViewSet.queryset, json_values={"id_qrcode": id_qrcode})


# Classe onde serão realizadas as operações de requisições no modelo QrCodeGuest
class QrCodeGuestViewSet(viewsets.ModelViewSet):
    model = QrCodeGuest
    queryset = QrCodeGuest.objects
    serializer_class = QrCodeGuestSerializer

    # Método que executa uma requisição HTTP GET para listagem dos qrcodes associados a um convidado específico
    def get_qrcodes_guests(self, request, id_guest_ext):
        return ORM.get_qrcode_with_guest_id(QrCodeGuestViewSet.queryset, json_values={"id_guest_ext": id_guest_ext})

    # Método que executa uma requisição HTTP POST para cadastro dos qrcodes associados a um convidado específico
    def register_qrcode_guest(self, request):
        return ORM.create_qrcodes_with_guest(QrCodeGuestViewSet.queryset, json_values=request.data)

    # Método que executa uma requisição HTTP PUT para atualização dos qrcodes associados a um convidado específico
    def modify_qrcode_guest(self, request):
        return ORM.update_qrcodes_with_guest_with_guest_id(QrCodeGuestViewSet.queryset, json_values=request.data)

    # Método que executa uma requisição HTTP DELETE para exclusão dos qrcodes associados a um convidado específico
    def drop_qrcode_guest(self, request, id_guest_ext):
        return ORM.destroy_qrcodes_with_guest_with_guest_id(QrCodeGuestViewSet.queryset, json_values={"id_guest_ext": id_guest_ext})


# Classe onde serão realizadas as operações de requisições no modelo Accredited
class AccreditedViewSet(viewsets.ModelViewSet):
    model = Accredited
    queryset = Accredited.objects
    serializer_class = AccreditedSerializer

    # Método que executa uma requisição HTTP GET para listagem de confirmações de credenciamento
    def get_guest_accredited(self, request, id_guest_acc_ext):
        return ORM.get_accredited_with_guest_id(AccreditedViewSet.queryset, json_values={"id_guest_acc_ext": id_guest_acc_ext})

    # Método que executa uma requisição HTTP POST para cadastro das confirmações de credenciamento
    def register_guest_accredited(self, request):
        return ORM.create_guest_accredited(AccreditedViewSet.queryset, json_values=request.data)

    # Método que executa uma requisição HTTP PUT para atualização de confirmação de credenciamento
    def modify_guest_accredited(self, request):
        return ORM.update_guest_accredited_with_guest_id(AccreditedViewSet.queryset, json_values=request.data)

    # Método que executa uma requisição HTTP DELETE para exclusão  de confirmação de credenciamento
    def drop_guest_accredited(self, request, id_guest_acc_ext):
        return ORM.destroy_guest_accredited_with_guest_id(AccreditedViewSet.queryset, json_values={"id_guest_acc_ext": id_guest_acc_ext})


# Classe onde serão realizadas as operações de querys
class GuestsDataAPIView(APIView):
    permission_classes = (permissions.AllowAny,)
    http_method_names = ['get']

    def get(self, request, qrcode_content=None):
        try:
            with connection.cursor() as cursor:
                query = """
                    select tg.id_guest as id_guest, tg."name" as "name", tg.phone_number as phone_number, tq.qrcode_content as qrcode_content, ta.accredited as accredited
                    from tb_guests tg 
                    inner join tb_qrcode_guest tqg on tg.id_guest = tqg.id_guest_ext
                    inner join tb_qrcode tq on tqg.id_qrcode_ext  = tq.id_qrcode
                    inner join tb_accredited ta on ta.id_guest_acc_ext  = tg.id_guest
                    """

                if qrcode_content is None:
                    cursor.execute(query)
                else:
                    query_joined = """
                                    select tg.id_guest as id_guest, tg."name" as "name", tg.phone_number as phone_number, tq.qrcode_content as qrcode_content, ta.accredited as accredited
                                    from tb_guests tg 
                                    inner join tb_qrcode_guest tqg on tg.id_guest = tqg.id_guest_ext
                                    inner join tb_qrcode tq on tqg.id_qrcode_ext  = tq.id_qrcode
                                    inner join tb_accredited ta on ta.id_guest_acc_ext  = tg.id_guest
                                    {str_1}
                                    """.format(str_1="where tq.qrcode_content = '{str_2}'".format(str_2=qrcode_content))

                    cursor.execute(query_joined)

                columns = [col[0] for col in cursor.description]
                data = [dict(zip(columns, row)) for row in cursor.fetchall()]
                return Response(data)
        except Exception as e:
            return Response("Falha ao buscar convidados. Por favor, verifique os dados da consulta ou se os registros existem no banco de dados.", status=400)
