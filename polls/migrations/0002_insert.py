import uuid

from django.db import migrations


# Método que insere os dados padrões na tabela tb_guests
def insert_guests_data(apps, schema_editor):
    guests_insert = apps.get_model('polls', 'Guests')
    guests = [
        guests_insert(
            name='Daniel Lucas Ferreira',
            phone_number='34991839020'
        ),
        guests_insert(
            name='Cecilia Cristina',
            phone_number='34991355188'
        )
    ]

    for i in guests:
        i.save()


# Método que insere os dados padrões na tabela tb_qrcode
def insert_qrcode_data(apps, schema_editor):
    qrcode = []
    qrcode_insert = apps.get_model('polls', 'Qrcode')
    guests = apps.get_model('polls', 'Guests')
    for guest in guests.objects.all():
        qrcode.append(
            qrcode_insert(
                qrcode_content=str(uuid.uuid4())
            )
        )

    for i in qrcode:
        i.save()


# Método que insere os dados padrões na tabela tb_accredited
def insert_accredited_data(apps, schema_editor):
    accredited = []
    accredited_insert = apps.get_model('polls', 'Accredited')
    guests = apps.get_model('polls', 'Guests')

    for guest in guests.objects.all():
        accredited.append(
            accredited_insert(
                id_guest_acc_ext=guest,
                accredited=False
            )
        )

    for i in accredited:
        i.save()


# Método que insere os dados padrões na tabela tb_qrcode_guest
def insert_qrcode_guest_data(apps, schema_editor):
    qrcode_guest = []
    qrcode_guest_insert = apps.get_model('polls', 'QrCodeGuest')
    guests = apps.get_model('polls', 'Guests')
    qrcodes = apps.get_model('polls', 'Qrcode')

    for guest in guests.objects.all():
        for qrcode in qrcodes.objects.all():
            if guest.id_guest == qrcode.id_qrcode:
                qrcode_guest.append(
                    qrcode_guest_insert(
                        id_guest_ext=guest,
                        id_qrcode_ext=qrcode
                    )
                )

    for i in qrcode_guest:
        i.save()


class Migration(migrations.Migration):
    dependencies = [
        ('polls', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(
            insert_guests_data,
            hints={
                'target_db': 'tb_guests'
            }
        ),
        migrations.RunPython(
            insert_qrcode_data,
            hints={
                'target_db': 'tb_qrcode'
            }
        ),
        migrations.RunPython(
            insert_accredited_data,
            hints={
                'target_db': 'tb_accredited'
            }
        ),
        migrations.RunPython(
            insert_qrcode_guest_data,
            hints={
                'target_db': 'tb_qrcode_guest'
            }
        )
    ]
