from tortoise.models import Model
from tortoise import fields

class Example(Model):
    id = fields.BigIntField(pk=True)
    name = fields.CharField(max_length=30)
    description = fields.TextField()
    created_at = fields.DatetimeField(auto_now_add=True)
    is_active = fields.BooleanField(default=True)
    
    class Meta:
        table = "example"
    
    def __str__(self):
        return self.name