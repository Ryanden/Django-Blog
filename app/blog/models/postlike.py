from django.db import models

from blog.models import Post
from members.models import BlogUser


__all__ = (
    'PostLike',
)


class PostLike(models.Model):

    user = models.ForeignKey(
        BlogUser,
        on_delete=models.CASCADE,
        related_name='my_post_like',
    )

    post = models.ForeignKey(
        Post,
        on_delete=models.CASCADE,
        related_name='like_comment_by_user'
    )

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.user}님이 {self.post}를 좋아합니다.'

