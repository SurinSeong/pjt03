from django.db import models

# 주식 모델
class Stock(models.Model):
    name = models.CharField(max_length=100)
    code = models.CharField(max_length=6)
    updated_at = models.DateField(auto_now=True)


# 댓글 모델
class Comment(models.Model):
    # Stock 모델 가져옴.
    stock = models.ForeignKey(Stock, on_delete=models.CASCADE, related_name='comments')
    content = models.TextField()
    created_at = models.DateField(auto_now_add=True)