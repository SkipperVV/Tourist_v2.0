from django.db import models
from users.models import Tourist

# Create your models here.
class MountainPass(models.Model):
    CATEGORY = {"зима": "winter", "весна": "spring", "лето": "summer", "осень": "autumn"}

    """ФСТР проведут модерацию для каждого нового объекта и поменяют поле status
    new;
    pending — если модератор взял в работу;
    accepted — модерация прошла успешно;
    rejected — модерация прошла, информация не принята."""

    STATUS = {"новый": "new", "в ожидании": "pending", "подтвержден": "accepted", "отклонен": "rejected"}

    def user_directory_path(instance, filename):
        # file will be uploaded to MEDIA_ROOT/user_<id>/<filename>
        return '{0}/{1}'.format(instance.tourist.last_name, filename)

    tourist = models.ForeignKey(Tourist, on_delete=models.CASCADE)
    beauty_title = models.CharField(max_length=100, default="пер. ")
    title = models.CharField(max_length=100)
    add_time = models.DateTimeField(auto_now_add=True)
    latitude = models.DecimalField(max_digits=6, decimal_places=4)
    longitude = models.DecimalField(max_digits=6, decimal_places=4)
    height = models.IntegerField()
    level = models.CharField(choices=CATEGORY, max_length=100)
    level_category = models.CharField(max_length=100)
    image = models.ImageField(upload_to=user_directory_path, blank=True)
    pass_status = models.CharField(choices=STATUS, max_length=50,  default="new", help_text="Изменить статус после проверки")

    def __str__(self):
        return f"Перевал '{self.title}', Позиция: {self.latitude}N / {self.longitude}E, Высота: {self.height}м, Статус: {self.pass_status}"