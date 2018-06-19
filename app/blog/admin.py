from django.contrib import admin

from members.models import BlogUser, UserInfo
from .models import Post, PostLike, Comment, CommentLike


# Register your models here.

admin.site.register(Post)
admin.site.register(BlogUser)
admin.site.register(UserInfo)
admin.site.register(PostLike)
admin.site.register(Comment)
admin.site.register(CommentLike)

