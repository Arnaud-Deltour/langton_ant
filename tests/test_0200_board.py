# ruff: noqa: D100,D103,I001,S101,PLR2004, W291
import langton_ant as la


def test_board_init() -> None:
    board = la.Board()
    assert board.str_output() == "0,0,UP\n \n"

def test_board_simulation() -> None:
    board = la.Board()
    for _i in range(10):
        board.simulate()
    assert board.str_output() == "2,0,DOWN\nXX \n XX\n XX\n"

    board1 = la.Board() # I looked for the result online
    for _i in range(10000):
        board1.simulate()
    assert board1.str_output() == """12,3,UP
           XX  XXXXXXXXXXXX  XX                  
          X  XXXX          X  XX                 
         XXX   XX            XX X                
         X X  X         X  X    X                
     XX  XX X X         XXX       X              
  XXX X  X   X     X     XX XX  XXX              
   X X  XXX  XX XXXX XX   X X  X XX  XX          
   X XXX XX  X XX  XXX X X     XXX   XXX         
 X     X   XXXXX X X  XXXX  X   XXX X X X        
XXX XX   X XXXX  XX XX XXXXXX X XXX X   X        
X XXX X XX X X XX XX XX X   XXXXX XXX XX         
    X X   X XX XXX   X   X X  XXXX    X XX       
 XXXX         XX XX   X  XX     XX X     XX      
 X XX X X XX XXX  X  XX     X   XXX XX  XX X     
   X X XX   XX XX   XXX  X    X  XX XXXX   X     
  XXXX  X X  X X XXXX XX  X XX XXX  X     X      
  X XX XX    X  X XXX  X      XXX XX X  X  XX    
   XX   X XX X XX  XX  XXXXX XXXX  XXXX XX   X   
    XX X  X XXX X X XX      XX   X X X    X   X  
      XXX  XX X   XX       XXXX XXXX   X      X  
      X   XX  XXXXXXXXXXX X  XXXX  X    X    X   
         X XXXX  XX  XXXXXXXXX  X  XX    X  XX   
     XX  X XX   XX XX XXX XXX   X  X XX  XXXX X  
    X  X XXXXXX XX X XX X X    XXX XXX   XX   X  
   X     XXXXX X XXXXX     X X  XX X    XX   X   
   X     X XX XXXXX XX  X X   X  X  XX X  X  X   
   X    X   XXXX X  XXXXX XX   XXXXXXXXXX   XX   
   X XX   XX   X  X   XXXX  X   XX XXXX XX       
    XXXXX X  XX   XX X   X    X X  X  X  X X     
     XX  XX X X X    XX XX X X XX  X  XX  XX     
           X  X    X XXXXXXXX X X XX  XXXX X     
           X  X   X       XX XX   X  X  XX X     
            X  X  X      X  XX  XX   XX XXXX     
             XX   X       XX  XX    X   X XXX    
                  X XX  XXXX    XXXX XXX XXXX    
                   XX  XXXX    XX  X XX X X  X   
                    XX    XX    XX XXX XX XXXXX  
                                   X XX X  XXXX  
                                       XX XX XX  
                                       XX        
                                     X XX  XXXX X
                                    X  X XXX  XXX
                                    X XX X  X  X 
                                     XX      XX  
                                      XX         
"""
