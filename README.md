# A QUIZ USING SOCKET PROGRAMMING

##This is a computer network based simulation of a quiz game.
The participants are the clients and the host is the server. 
##----------------------------------------------------------------
The game is played by 3 players. Whenever any one of the player gets 5 points the quiz ends. Initially the host will display a question. The player who responds "bz" fastest can answer the question. If the answer is correct then the point of the player is incremented by one, otherwise the host goes to the next question. This process is repeated till one of the player wins.

This game contains two programs- server.py and client.py server.py handles the host side of the game. client.py handles the participant side of the game.

How to play the game: First the host should run server.py ##python server.py s. The client running in the 
other system connect to the server using server's IP address and port number. Need to run the client.py ##python client.py IP PORT
