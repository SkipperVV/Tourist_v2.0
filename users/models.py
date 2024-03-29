from django.db import models
from django.contrib.auth.models import User, Group


class Tourist(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, help_text="Турист", primary_key=True)
    first_name = models.CharField(max_length=100)
    middle_name = models.CharField(max_length=100)
    last_name = models.CharField(verbose_name='last_name', max_length=100)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=100)

    # profile_pic = models.ImageField(null=True, blank=True, upload_to="images/profile/")

    def add_to_group(self):
        user = super().User.objects.filter(user=self.user)
        group = Group.objects.filter(name='tourist')
        user.groups.add(group)

    def __str__(self):
        return f" {self.last_name} {self.first_name} {self.middle_name}"
