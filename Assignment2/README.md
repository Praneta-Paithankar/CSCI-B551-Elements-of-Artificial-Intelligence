Problem 1:Pichu

Let’s consider Pichu, a somewhat simplified version of Chess that is popular among a certaincommunity of midwestern bird enthusiasts.
The game is played by two players on a board consisting of a grid of 8×8 squares.Initially, each playerhas sixteen pieces:  
8 Parakeets, 2 Robins, 2 Nighthawks, 2 Blue jays, 1 Quetzal, and 1 Kingfisher.

The two players alternate turns, with White going first.On each turn, a player moves exactly one of his or her pieces,possibly capturing (removing) a piece of the opposite player in the process, according to the following rules:

• A Parakeet may move one square forward,  if no other piece is on that square.Or,  a Parakeet maymove one square forward diagonally (one square forward and one square left or right) if a piece of the opposite player is on that square, in the process capturing that piece from the board. If a Parakeet reaches the far row of the board (closest to the opposite player), it is transformed into a Quetzal. On its very first move of the game, a Parakeet may move forward two squares as long as both are empty.

•A Robin may move any number of squares either horizontally or vertically, landing on either an emptysquare or a piece of the opposite player (which is then captured), as long as all the squares betweenthe starting and ending positions are empty.

•A Blue jay is like a Robin, but moves along diagonal flight paths instead of horizontal or vertical ones.

•A Quetzal is like a combination of a Robin and a Blue jay:  it may move any number of empty squareshorizontally, vertically, or diagonally, and land either on an empty square or on a piece of the oppositeplayer (which is then captured).

•A Kingfisher may move one square in any direction, horizontally or vertically, either to an empty squareor to capture a piece of the opposing player.

•A Nighthawk moves in L shaped patterns on the board, either two squares to the left or right followed by  one  square  forward  or  backward,  or  one  square  left  or  right  followed  by  two  squares  forward  or backward.  It may fly over any pieces on the way, but the destination square must either be empty or have a piece of the opposite player (which is then captured).

A  player  wins  by  capturing  the  other  player’s  Kingfisher.   (Note  some  of  the  differences  with  traditionalChess:  there’s no notion of check or checkmate, no en passant, and no castling.)

Your task is to write a Python program that plays Pichu well.  Use the minimax algorithm with alpha-betasearch and a suitable heuristic evaluation function.  
Your program should accept a command line argumentthat gives the current state of the board as a string of 64 characters, each of which is one of: .for an emptysquare,P or pfor a white or black Parakeet,R or r for a white or black Robin,N or n for a white or black Night hawk,Q or q for a white or black Quetzal,K or k for a white or black Kingfisher, and B or bfor a white or black Blue jay, in row-major order. 

For example, the encoding of the start state of the game would be:RNBQKBNRPPPPPPPP................................pppppppprnbqkbnr

More precisely, your program will be called with three command line parameters: (1) the current player (w orb), (2) the state of the board, encoded as above, and (3) a time limit in seconds.  Your program should thendecide a recommended single move for the given player from the given current board state, and display thenew state of the board after making that move,within the number of seconds specified.Displaying multiplelines of output is fine as long as the last line has the recommended board state.  (This is an easy way ofdealing  with  the  time  limit:  the  program  can  very  quickly  calculate  and  print  a  suggested  “rough-draft”move, and then print out better moves as it finds them; our test programs will kill your program after thetime limit has passed and look only at the last move.) 

