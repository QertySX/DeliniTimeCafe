from django.db import models
from django.contrib.auth.models import User

# class Table(models.Model):
#     number = models.PositiveIntegerField(unique=True)

#     def __str__(self):
#         return f"Столик №{self.number}"


class BookTable(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    # table = models.ForeignKey(Table, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=20)
    email = models.EmailField(blank=True, null=True)
    guests = models.PositiveIntegerField()
    date = models.DateField()
    time = models.TimeField()
    created_at = models.DateTimeField(auto_now_add=True)
    

    def __str__(self):
        return f"Заброньовано на: {self.name}. Дата: {self.date}. Час: {self.time}"

