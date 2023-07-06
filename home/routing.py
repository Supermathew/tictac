# from django.conf.urls import url
from django.urls import path
from home.consumers import GameRoom

websocket_urlpatterns = [
    path('ws/game/<room_code>' , GameRoom.as_asgi()),
    # url(r'^ws/play/(?P<room_code>\w+)/$', GameRoom.as_asgi()),
]