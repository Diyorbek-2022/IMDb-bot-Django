from django.db import models




class Cinema(models.Model):
    id = models.AutoField(primary_key=True)
    cinema_url = models.TextField()
    info = models.OneToOneField("Users.Info", on_delete=models.CASCADE, related_name="cinema", null=True, blank=True)
    cinema_code = models.TextField(unique=True)
    added_time = models.DateTimeField(auto_now_add=True)
    next = models.IntegerField(null=True, blank=True)
    previous = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return self.info.name if self.info else "No info"
