from django.db import models

from blog.models import Post
from members.models import BlogUser

__all__ = (
    'Comment',
)


class Comment(models.Model):

    user = models.ForeignKey(
        BlogUser,
        on_delete=models.CASCADE,
        related_name='my_comment',
    )

    post = models.ForeignKey(
        Post,
        on_delete=models.CASCADE,
        related_name='comments',
        blank=True,
        null=True,
    )

    content = models.TextField(null=True)

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.user} :{self.content}'

    @property
    def like_users(self):
        return f'{self.like_by_user.all()}'

