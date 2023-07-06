from channels.generic.websocket import WebsocketConsumer
from asgiref.sync import async_to_sync
import json
# from models import G
from home.models import Game 
import json


class GameRoom(WebsocketConsumer):
    def connect(self):
        self.room_name = self.scope['url_route']['kwargs']['room_code']
        self.room_group_name = 'room_%s' %  self.room_name
        print(self.room_group_name) 

        async_to_sync(self.channel_layer.group_add)(
            self.room_group_name,
            self.channel_name
        )
        
        self.accept()

        room_code = self.room_name

        game = Game.objects.get(room_code=room_code)

        creater = game.game_creator
        opp = game.game_opponent

        text_data ={
            'room_name':self.room_name,
            'opp':opp,
            'creater':creater,

        }

        text_data = json.dumps(text_data)

        async_to_sync(self.channel_layer.group_send)(
            self.room_group_name,{
                'type' : 'run_game',
                'payload' : text_data
            }
        )






        
    def disconnect(self,close_code):

        if close_code != 1000: 
            print("inter") # 1000 indicates a normal WebSocket closure
            async_to_sync(self.channel_layer.group_send)(
                self.room_group_name,{
                    'type' : 'redirect_user',
                    'payload' : 'redirect'
                }
            )


        async_to_sync(self.channel_layer.group_discard)(
            self.room_group_name,
            self.channel_name
        )

        
        
    def receive(self , text_data):
        print(text_data)
        async_to_sync(self.channel_layer.group_send)(
            self.room_group_name,{
                'type' : 'run_game',
                'payload' : text_data
            }
        )
        
    
    def run_game(self , event):
        data = event['payload']
        data = json.loads(data)
        print(data)

        keyeeror = False

        try:
            room_id = data['data']['romeid']
            message = data['data']['message']
            type = data['data']['type']

            print("Room ID:", room_id)
            print("Message:", message)
            if type == "over" or type == "end":
                data = Game.objects.get(room_code=room_code)
                data.delete()
            self.send(text_data= json.dumps({
                'payload' : data['data']
            }))        
        except KeyError as e:
               keyeeror = True

        if(keyeeror):
            self.send(text_data= json.dumps({
                'payload' : data
            }))  


    def redirect_user(self , event):
        data = event['payload']
        data = json.loads(data)
        print(data)

        self.send(text_data= json.dumps({
            'payload' : data
        }))  
