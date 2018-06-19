from django.db import models

from blog.models import Comment
from members.models import BlogUser

__all__ = (
    'CommentLike',
)


class CommentLike(models.Model):

    user = models.ForeignKey(
        BlogUser,
        on_delete=models.CASCADE,
        related_name='my_comment_like',
    )

    comment = models.ForeignKey(
        Comment,
        on_delete=models.CASCADE,
        related_name='like_by_user'
    )

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.user}님이 {self.comment}를 좋아합니다.'
