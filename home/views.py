from django.shortcuts import render,redirect
from django.contrib import messages
from .models import *
# Create your views here.


def home(request):
    if request.method == "POST":
        username = request.POST.get('username')
        option = request.POST.get('option')
        room_code = request.POST.get('room_code')
        
        if option == '1':
            game = Game.objects.filter(room_code = room_code).first()
            print("heloogibk")
            if game is None:
                message.success(request , "Room code not found")
                print("game ha")
                return redirect('/')
            
            if game.is_over:
                message.success(request , "Game is over")
                return redirect('/')
             
            game.game_opponent = username
            context_data = {'urchange': '2'}
            game.save()
            request.session['context_data'] = context_data

            return redirect('/play/' + room_code + '?username='+username)     

        else:
            game = Game(game_creator = username , room_code = room_code)
            game.save() 
            print("hellooooooooooooooooooo")
            context_data = {'urchange': '1'}
            urchange=1 
            request.session['context_data'] = context_data
            return redirect('/play/' + room_code + '?username='+username)     
            
    return render(request, 'home.html')



def play(request , room_code):
    username = request.GET.get('username')
    data = Game.objects.get(room_code=room_code)
    context_data = request.session.get('context_data', {})
    print(context_data)
    context = {'room_code' : room_code , 'username' : username,'data':data,'context_data':context_data}
    return render(request, 'play.html' , context)

# Create your views here.
