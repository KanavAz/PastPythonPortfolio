#Kanav Azad
#10/24/2023
#This program will simulate a coin toss and display the result.

import random
import time

class Coin():

  def __init__(self, amount, sideup):
    self.__amount = amount
    self.__sideup = sideup

  def toss(self):
    if random.randint(0, 1) == 0:
      self.__sideup = "Heads"
    else:
      self.__sideup = "Tails"

  def get_sideup(self):
    return self.__sideup

  def set_amount(self, int):
    self.__amount += int

  def get_amount(self):
    return self.__amount


def main():

  coin1 = Coin(20, "Heads")
  coin2 = Coin(20, "Heads")

  print("Welcome to the Coin Toss Game! One of you will be player 1 and the other will be player 2, you must choose now!")

  time.sleep(5)
  
  cont = " "
  while cont != "n":

    coin1.toss()
    coin2.toss()
    
    if coin1.get_sideup() == coin2.get_sideup():
      print("\nPlayer 1 chose " + coin1.get_sideup() + " and Player 2 chose " + coin2.get_sideup() + ". Player 1 wins!")
      coin1.set_amount(1)
      coin2.set_amount(-1)
    else:
      print("\nPlayer 1 chose " + coin1.get_sideup() + " and Player 2 chose " + coin2.get_sideup() + ". Player 2 wins!")
      coin1.set_amount(-1)
      coin2.set_amount(1)

    cont = input("\nWould you like to continue playing? Enter 'y' or 'n': ")
    cont = cont.lower()

  print("\nPlayer 1 has " + str(coin1.get_amount()) + " coins, while Player 2 has " + str(coin2.get_amount()) + " coins.")


main()




    