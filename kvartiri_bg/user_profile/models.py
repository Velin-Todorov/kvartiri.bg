from django.db import models
from auth_views.models import Profile, LandlordProfile


class Messages(models.Model):
    sender = models.ForeignKey(Profile, on_delete=models.CASCADE)
    recipient = models.ForeignKey(LandlordProfile, on_delete=models.CASCADE)
    msg_content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)