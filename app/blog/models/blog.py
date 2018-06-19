from django.db import models

from members.models import BlogUser

__all__ = (
    'Post',
)


class Post(models.Model):

    user = models.ForeignKey(
        BlogUser,
        on_delete=models.CASCADE,
        related_name='my_post',
    )

    title = models.CharField(max_length=50, default=None)

    content = models.TextField(null=True)

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    @property
    def like_users(self):
        return f'{self.like_comment_by_user.all()}'
