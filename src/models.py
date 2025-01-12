from tortoise import fields
from tortoise.models import Model


class Task(Model):
    id = fields.UUIDField(pk=True)
    user_id = fields.IntField()
    title = fields.CharField(max_length=255)
    description = fields.CharField(max_length=255, null=True)
    is_done = fields.BooleanField(default=False)

    # class Meta:
    #     table = "tasks"
