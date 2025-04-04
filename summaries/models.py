from django.db import models
from crawlings.models import Comment

# Create your models here.
class Summary(models.Model):
    summary = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    related_comment = models.ForeignKey(Comment, on_delete=models.CASCADE)
    # 혹은 종목이나 다른 엔티티와 직접 연결
