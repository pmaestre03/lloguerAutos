from django.core.management.base import BaseCommand
from django.utils import timezone
from faker import Faker
from datetime import timedelta
from random import randint
from faker_vehicle import VehicleProvider


from lloguer.models import *

faker = Faker()

faker.add_provider(VehicleProvider)


class Command(BaseCommand):
    help = 'Crea automóviles y reservas falsos'

    def handle(self, *args, **options):
        print("Creando datos falsos para automóviles y reservas...")

        print("Creando automóviles...")
        for _ in range(200):
            marca = faker.vehicle_make()
            model = faker.vehicle_model()
            matricula = faker.license_plate()
            Automobil.objects.create(marca=marca, model=model, matricula=matricula)

        print("Creando reservas...")
        for _ in range(10):
            automovil = Automobil.objects.order_by('?').first()  # Selecciona un automóvil aleatorio
            fecha_inicio = faker.date_between(start_date="-30d", end_date="+30d")
            fecha_fin = fecha_inicio + timedelta(days=randint(1, 7))
            Reserva.objects.create(automovil=automovil, fecha_inicio=fecha_inicio, fecha_fin=fecha_fin)

        print("Datos falsos creados con éxito.")
