"""
ASGI config for tictac project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.1/howto/deployment/asgi/
"""

import os

# from django.core.asgi import get_asgi_application

# os.environ.setdefault("DJANGO_SETTINGS_MODULE", "tictac.settings")

# application = get_asgi_application()
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "my_app_name.settings")
django_asgi_app = get_asgi_application()

import home.routing
from django.core.asgi import get_asgi_application
import django
from channels.auth import AuthMiddlewareStack
from channels.routing import ProtocolTypeRouter, URLRouter
from channels.security.websocket import AllowedHostsOriginValidator
from django.urls import path
from home.consumers import GameRoom

# os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'tictac.settings')
# django.setup()

# application = ProtocolTypeRouter({
#     "http": get_asgi_application(),
#     "websocket": AuthMiddlewareStack(
#         URLRouter(
#                 home.routing.websocket_urlpatterns
#         )
#     ),
# })



# os.environ.setdefault("DJANGO_SETTINGS_MODULE", "tictac.settings")
# # Initialize Django ASGI application early to ensure the AppRegistry
# # is populated before importing code that may import ORM models.


# application = ProtocolTypeRouter({
#     # Django's ASGI application to handle traditional HTTP requests
#     "http": django_asgi_app,

#     # WebSocket chat handler
#     "websocket": AllowedHostsOriginValidator(
#         AuthMiddlewareStack(
#             URLRouter([
#                     path('ws/game/<room_code>' , GameRoom.as_asgi()),
#             ])
#         )
#     ),
# })
from channels.auth import AuthMiddlewareStack
from channels.routing import ProtocolTypeRouter, URLRouter
application = ProtocolTypeRouter({
    "http": django_asgi_app,
     "websocket": AuthMiddlewareStack(
         URLRouter(
                home.routing.websocket_urlpatterns
        )
    ),
})