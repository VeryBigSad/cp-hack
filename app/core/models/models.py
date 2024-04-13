from tortoise import fields
from tortoise.models import Model


class User(Model):
    class Meta:
        table = "users"
        ordering = ["created_at"]

    user_id = fields.BigIntField(pk=True)
    username = fields.CharField(max_length=32, index=True, null=True)


class UploadedImage(Model):
    class Meta:
        table = 'uploaded_images'

    id = fields.BigIntField(pk=True)
    url = fields.CharField(max_length=1024)
