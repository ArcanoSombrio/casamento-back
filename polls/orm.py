from django.db.utils import IntegrityError
from django.http import JsonResponse

from polls.models import *


# Classe que realiza a ORM (operações no banco de dados)
class ORM:
    # Método que lista os convidados cadastrados no banco de dados
    @staticmethod
    def list_all_guests(queryset):
        try:
            guests = list(queryset.values())
            results = JsonResponse(guests, safe=False, status=200)
            return results
        except IntegrityError:
            return JsonResponse("Falha ao listar os convidados. Por favor, verifique se não faltam dados na requisição.", safe=False, status=400)

    # Método que cria o convidado no banco de dados
    @staticmethod
    def create_guest(queryset, json_values):
        try:
            last = queryset.all().order_by('id_guest').last()
            if not last:
                json_values["id_guest"] = 1
            else:
                json_values["id_guest"] = int(last) + 1

            queryset.create(
                id_guest=json_values["id_guest"],
                name=json_values["name"],
                phone_number=json_values["phone_number"]
            )
            return JsonResponse(json_values, safe=False, status=201)
        except IntegrityError:
            return JsonResponse("Falha ao registrar convidado. Por favor, verifique se não faltam dados na requisição.", safe=False, status=400)
        except KeyError:
            return JsonResponse("Por favor, insira os dados em formato JSON no body da requisição.", safe=False, status=400)

    # Método que atualiza os dados do convidado no banco de dados
    @staticmethod
    def update_guest_with_id(queryset, json_values):
        try:
            queryset.filter(id_guest=json_values["id_guest"]).update(
                name=json_values["name"],
                phone_number=json_values["phone_number"]
            )
            return JsonResponse(json_values, safe=False, status=201)
        except IntegrityError:
            return JsonResponse("Falha ao atualizar convidado. Por favor, verifique se não faltam dados na requisição.", safe=False, status=400)
        except KeyError:
            return JsonResponse("Por favor, insira os dados em formato JSON no body da requisição.", safe=False, status=400)

    # Método que deleta o convidado no banco de dados
    @staticmethod
    def destroy_guest_with_id(queryset, json_values):
        try:
            queryset.filter(id_guest=json_values["id_guest"]).delete()
            return JsonResponse(json_values, safe=False, status=201)
        except IntegrityError:
            return JsonResponse("Falha ao deletar convidado. Por favor, verifique se não faltam dados na requisição.", safe=False, status=400)
        except KeyError:
            return JsonResponse("Por favor, insira os dados em formato JSON no body da requisição.", safe=False, status=400)

    # Método que lista os QR Codes cadastrados no banco de dados
    @staticmethod
    def list_all_qrcodes(queryset):
        try:
            qrcodes = list(queryset.values())
            results = JsonResponse(qrcodes, safe=False, status=200)
            return results
        except IntegrityError:
            return JsonResponse("Falha ao listar os qrcodes. Por favor, verifique se não faltam dados na requisição.", safe=False, status=400)

    # Método que cria o QR Code no banco de dados
    @staticmethod
    def create_qrcode(queryset, json_values):
        try:
            last = queryset.all().order_by('id_qrcode').last()
            if not last:
                json_values["id_qrcode"] = 1
            else:
                json_values["id_qrcode"] = int(last) + 1

            queryset.create(
                id_qrcode=json_values["id_qrcode"],
                qrcode_content=json_values["qrcode_content"]
            )
            return JsonResponse(json_values, safe=False, status=201)
        except IntegrityError:
            return JsonResponse("Falha ao registrar QR Code. Por favor, verifique se não faltam dados na requisição.", safe=False, status=400)
        except KeyError:
            return JsonResponse("Por favor, insira os dados em formato JSON no body da requisição.", safe=False, status=400)

    # Método que atualiza os dados do QR Code no banco de dados
    @staticmethod
    def update_qrcode_with_id(queryset, json_values):
        try:
            queryset.filter(id_qrcode=json_values["id_qrcode"]).update(
                qrcode_content=json_values["qrcode_content"]
            )
            return JsonResponse(json_values, safe=False, status=201)
        except IntegrityError:
            return JsonResponse("Falha ao atualizar os dados do QR Code. Por favor, verifique se não faltam dados na requisição.", safe=False, status=400)
        except KeyError:
            return JsonResponse("Por favor, insira os dados em formato JSON no body da requisição.", safe=False, status=400)

    # Método que deleta um QR Code no banco de dados
    @staticmethod
    def destroy_qrcode_with_id(queryset, json_values):
        try:
            queryset.filter(id_qrcode=json_values["id_qrcode"]).delete()
            return JsonResponse(json_values, safe=False, status=201)
        except IntegrityError:
            return JsonResponse("Falha ao deletar o QR Code. Por favor, verifique se não faltam dados na requisição.", safe=False, status=400)
        except KeyError:
            return JsonResponse("Por favor, insira os dados em formato JSON no body da requisição.", safe=False, status=400)

    # Método que lista os QR Codes de um convidado específico no banco de dados
    @staticmethod
    def get_qrcode_with_guest_id(queryset, json_values):
        try:
            qrcodes_guest = list(queryset.filter(id_guest_ext=json_values["id_guest_ext"]).values())
            results = JsonResponse(qrcodes_guest, safe=False, status=200)
            return results
        except IntegrityError:
            return JsonResponse("Falha ao listar os QR Codes por convidado. Por favor, verifique se não faltam dados na requisição.", safe=False, status=400)
        except KeyError:
            return JsonResponse("Por favor, insira os dados em formato JSON no body da requisição.", safe=False, status=400)

    # Método que cria uma ligação de QR Code com convidado no banco de dados
    @staticmethod
    def create_qrcodes_with_guest(queryset, json_values):
        try:
            queryset.create(
                id_guest_ext=Guests(id_guest=json_values["id_guest_ext"]),
                id_qrcode_ext=Qrcode(id_qrcode=json_values["id_qrcode_ext"])
            )
            return JsonResponse(json_values, safe=False, status=201)
        except IntegrityError:
            return JsonResponse("Falha ao registrar QR Code para convidado. Por favor, verifique se não faltam dados na requisição.", safe=False, status=400)
        except KeyError:
            return JsonResponse("Por favor, insira os dados em formato JSON no body da requisição.", safe=False, status=400)

    # Método que atualiza os dados de QR Code para um convidado no banco de dados
    @staticmethod
    def update_qrcodes_with_guest_with_guest_id(queryset, json_values):
        try:
            queryset.filter(id_guest_ext=json_values["id_guest_ext"]).update(
                id_qrcode_ext=Qrcode(id_qrcode=json_values["id_qrcode_ext"])
            )
            return JsonResponse(json_values, safe=False, status=201)
        except IntegrityError:
            return JsonResponse("Falha ao atualizar QR Code para convidado. Por favor, verifique se não faltam dados na requisição.", safe=False, status=400)
        except KeyError:
            return JsonResponse("Por favor, insira os dados em formato JSON no body da requisição.", safe=False, status=400)

    # Método que deleta um acompanhante no banco de dados
    @staticmethod
    def destroy_qrcodes_with_guest_with_guest_id(queryset, json_values):
        try:
            queryset.filter(id_guest_ext=json_values["id_guest_ext"]).delete()
            return JsonResponse(json_values, safe=False, status=200)
        except IntegrityError:
            return JsonResponse("Falha ao deletar QR Code para convidado. Por favor, verifique se não faltam dados na requisição.", safe=False, status=400)
        except KeyError:
            return JsonResponse("Por favor, insira os dados em formato JSON no body da requisição.", safe=False, status=400)

    # Método que lista a credencial dos convidados no banco de dados
    @staticmethod
    def get_accredited_with_guest_id(queryset, json_values):
        try:
            accredited = list(queryset.filter(id_guest_acc_ext=json_values["id_guest_acc_ext"]).values())
            results = JsonResponse(accredited, safe=False, status=200)
            return results
        except IntegrityError:
            return JsonResponse("Falha ao listar a credencial do convidado. Por favor, verifique se não faltam dados na requisição.", safe=False, status=400)
        except KeyError:
            return JsonResponse("Por favor, insira os dados em formato JSON no body da requisição.", safe=False, status=400)

    # Método que cria uma credencial para um convidado no banco de dados
    @staticmethod
    def create_guest_accredited(queryset, json_values):
        try:
            queryset.create(
                id_guest_acc_ext=Guests(id_guest=json_values["id_guest_acc_ext"]),
                accredited=json_values["accredited"]
            )
            return JsonResponse({"id_guest_acc_ext": json_values["id_guest_acc_ext"], "accredited": json_values["accredited"]}, safe=False, status=201)
        except IntegrityError:
            return JsonResponse("Falha ao registrar credencial para o convidado. Por favor, verifique se não faltam dados na requisição.", safe=False, status=400)
        except KeyError:
            return JsonResponse("Por favor, insira os dados em formato JSON no body da requisição.", safe=False, status=400)

    # Método que atualiza os dados da credencial de um convidado no banco de dados
    @staticmethod
    def update_guest_accredited_with_guest_id(queryset, json_values):
        try:
            queryset.filter(id_guest_acc_ext=json_values["id_guest_acc_ext"]).update(
                accredited=json_values["accredited"]
            )
            return JsonResponse(json_values, safe=False, status=201)
        except IntegrityError:
            return JsonResponse("Falha ao atualizar a credencial para o convidado. Por favor, verifique se não faltam dados na requisição.", safe=False, status=400)
        except KeyError:
            return JsonResponse("Por favor, insira os dados em formato JSON no body da requisição.", safe=False, status=400)

    # Método que deleta a credencial de um convidado no banco de dados
    @staticmethod
    def destroy_guest_accredited_with_guest_id(queryset, json_values):
        try:
            queryset.filter(id_guest_acc_ext=json_values["id_guest_acc_ext"]).delete()
            return JsonResponse(json_values, safe=False, status=200)
        except IntegrityError:
            return JsonResponse("Falha ao deletar credencial para o convidado. Por favor, verifique se não faltam dados na requisição.", safe=False, status=400)
        except KeyError:
            return JsonResponse("Por favor, insira os dados em formato JSON no body da requisição.", safe=False, status=400)
