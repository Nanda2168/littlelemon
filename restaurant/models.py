from django.db import models

# Slot choices (1 to 24 for hours)
SLOT_CHOICES = [(i, f'{i}:00') for i in range(1, 25)]

# Booking Model
class Booking(models.Model):
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    reservation_date = models.DateField()
    reservation_slot = models.IntegerField(choices=SLOT_CHOICES, default=10)

    def __str__(self):
        return f"{self.first_name} {self.last_name} - {self.reservation_date} - {self.reservation_slot}:00"


# Menu Model (WITH image support)
class Menu(models.Model):
    name = models.CharField(max_length=200)
    price = models.IntegerField(null=False)
    menu_item_description = models.TextField(max_length=1000, default='')
    image = models.CharField(max_length=255, blank=True)  # 👈 image path

    def __str__(self):
        return self.name
