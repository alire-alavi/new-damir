from django.db import models

from users.models import User

# Create your models here.

class NewsTellerEmails(models.Model):
    email = models.EmailField(verbose_name="ایمیل")
    user = models.ForeignKey(User, on_delete=models.CASCADE,
                             null=True, blank=True)

    def __str__(self):
        if self.user:
            return f"{self.user.username} has mailed their email as {self.email}"
        else:
            return f"{self.email} has been mailed from anonymous user"

