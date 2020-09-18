from django.urls import path
from .views import indexView,postFriend,checkNickName

app_name = 'work2'

urlpatterns = [
    # ... other urls
    path('', indexView),
    path('post/ajax/friend', postFriend, name = "post_friend"),
    path('get/ajax/validate/nickname', checkNickName, name = "validate_nickname"),
    # ...
]