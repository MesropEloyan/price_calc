from django.db import models

class Trip(models.Model):
    departure_point = models.CharField(max_length=100, verbose_name='Начальная точка')
    destination_point = models.CharField(max_length=100, verbose_name='Конечная точка ')
    distance = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Расстояние(км)')
    price_for_km = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Цена за км')
    toll_road = models.BooleanField(default=False, verbose_name='Платная дорога')
    toll_road_cost = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True, verbose_name='Стоимость дороги')



    def __str__(self):
        return f"{self.departure_point} - {self.destination_point}"
