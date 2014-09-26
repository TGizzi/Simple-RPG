from Battle import Battle
from Player import Player
from Enemy import Enemy, get_enemy

player1 = Player("Haz")
player2 = Player("Ekko")
player3 = Player("Dash")



battle = Battle()
battle.fight([player1, player2, player3], get_enemy(5))
