from django.db import models, connection


# Classe Modelo que cria a tabela tb_guests no banco e seus relacionamentos
class Guests(models.Model):
    id_guest = models.AutoField(primary_key=True, serialize=False)
    name = models.CharField(max_length=100, blank=True, null=True)
    phone_number = models.CharField(max_length=11, blank=False, null=False)

    objects = models.Manager()

    class Meta:
        managed = True
        db_table = 'tb_guests'

    def __int__(self):
        return self.id_guest


# Classe Modelo que cria a tabela tb_qrcode no banco e seus relacionamentos
class Qrcode(models.Model):
    id_qrcode = models.AutoField(primary_key=True, serialize=False)
    qrcode_content = models.CharField(max_length=36, blank=True, null=True)

    objects = models.Manager()

    class Meta:
        managed = True
        db_table = 'tb_qrcode'

    def __int__(self):
        return self.id_qrcode


# Classe Modelo que cria a tabela tb_qrcode_guest no banco e seus relacionamentos
class QrCodeGuest(models.Model):
    id_qrcode_guest = models.AutoField(primary_key=True, serialize=False)
    id_guest_ext = models.ForeignKey(Guests, models.DO_NOTHING, db_column='id_guest_ext')
    id_qrcode_ext = models.ForeignKey(Qrcode, models.DO_NOTHING, db_column='id_qrcode_ext')

    objects = models.Manager()

    class Meta:
        managed = True
        db_table = 'tb_qrcode_guest'

    def __int__(self):
        return self.id_qrcode_guest


# Classe Modelo que cria a tabela tb_accredited no banco e seus relacionamentos
class Accredited(models.Model):
    id_accredited = models.AutoField(primary_key=True, serialize=False)
    id_guest_acc_ext = models.ForeignKey(Guests, models.CASCADE, db_column='id_guest_acc_ext')
    accredited = models.BooleanField(default=False)

    objects = models.Manager()

    class Meta:
        managed = True
        db_table = 'tb_accredited'

    def __int__(self):
        return self.id_accredited
