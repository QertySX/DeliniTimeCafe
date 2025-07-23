from django.db import models

class BookTable(models.Model):
    name = models.CharField("Ім'я", max_length=100)
    phone = models.CharField("Номер телефону", max_length=20)
    email = models.EmailField("Електронна пошта", blank=True, null=True)
    guests = models.PositiveIntegerField("Кількість гостей")
    date = models.DateField("Дата бронювання")
    time = models.TimeField("Час бронювання")
    created_at = models.DateTimeField("Створено", auto_now_add=True)

    def __str__(self):
        return f"Заброньовано на {self.name} на {self.date} в {self.time}"