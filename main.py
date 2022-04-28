#!/usr/bin/env python
# -*- coding: utf-8 -*-


"""
This Python method contains the application of the Game.

@contents :  This module contains the complete implementation of the application
             of the Game.
@project :  N/A
@program :  N/A
@file :  main.py
@author :  Antonio Artes Garcia (antonio.artesgarcia@ceu.es)
           Francisco Hernando Gallego (francisco.hernandogallego@ceu.es)
           Ruben Juarez Cadiz (ruben.juarezcadiz@ceu.es)

@version :  0.0.1, 08 November 2021
@information :  The Zen of Python
                  https://www.python.org/dev/peps/pep-0020/
                Style Guide for Python Code
                  https://www.python.org/dev/peps/pep-0008/
                Example NumPy Style Python Docstrings
                  http://sphinxcontrib-napoleon.readthedocs.io/en/latest/example_numpy.html
                doctest – Testing through documentation
                  https://pymotw.com/2/doctest/

@copyright :  Copyright 2021 GNU AFFERO GENERAL PUBLIC.
              All rights are reserved. Reproduction in whole or in part is
              prohibited without the written consent of the copyright owner.
"""


# Source packages.

from pokemon import Pokemon
from weapon_type import WeaponType

def get_data_from_user(name_file):
    """Function to obtain data from each user.

    This function obtains data from each user in order to set the configuration
    of the Game.

    Syntax
    ------
      [ ] = get_data_from_user(name_file)

    Parameters
    ----------
      name_file str Name of the CSV file.

    Returns
    -------
      list_pokemons List of Pokemons obtained from CSV .

    Example
    -------
      >>> list_pokemons = get_data_from_user("file.csv")
    """

    file= open(name_file, "r")
    result= []
    for line in file.readlines():
      data= line.split(",")
      id= int(data[0])
      name= data[1]
      weapon= WeaponType[data[2].upper()]
      health= int(data[3])
      attack= int(data[4])
      defense= int(data[5])
      pokemon= Pokemon(id,name,weapon,health,attack,defense)
      result.append(pokemon)
    return result

def get_pokemon_in_a_list_of_pokemons(coach_to_ask, list_of_pokemons):
    """Function to know the list of Pokemons that are associated to the Coach.

    This function is used in order to know the list of Pokemos that are
    associated to the coach. This function prints the result of this list, so
    the user can select a Pokemon.

    Syntax
    ------
       [ ] = get_pokemon_in_a_list_of_pokemons(coach_to_ask, list_of_pokemons):

    Parameters
    ----------
       [in] coach_to_ask Coach to ask for her/his list of Pokemons.
       [in] list_of_pokemons List of the Pokemons that are associated to the
                             coach.

    Returns
    -------
       List List of the Pokemons associaated to the coach that are undefeated.

    Example
    -------
       >>> get_pokemon_in_a_list_of_pokemons(1, list_of_pokemons)
    """

    result= []
    for pokemon in list_of_pokemons:
      if pokemon.is_alive():
        result.append(pokemon)

    print("Coach ",coach_to_ask, ":")
    print("Select one pokemon of the following ones")
    for pokemon in result:
      print(pokemon)
    return result
  

def coach_is_undefeated(list_of_pokemons):
    """Function to know if the Coach is still undefeated.

    This function is used in order to know if the Coach is still undefeated.

    Syntax
    ------
       [ ] = coach_is_undefeated(list_of_pokemons)

    Parameters
    ----------
       [in] list_of_pokemons List of the Pokemons that are associated to the
                             coach.

    Returns
    -------
       Boolean True if the coach has all her/his Pokemons defeated.
               False if the coach has any Pokemon that is undefeated.

    Example
    -------
       >>> coach_is_undefeated(list_of_pokemons)
    """
    is_undefeated = False
    for pokemon in list_of_pokemons:
      if pokemon.is_alive():
        is_undefeated= True
    return is_undefeated

def main():
    """Function main of the module.

    The function main of this module is used to perform the Game.

    Syntax
    ------
      [ ] = main()

    Parameters
    ----------
      Null .

    Returns
    -------
      Null .

    Example
    -------
      >>> main()
    """

    print("Welcome to the Game.")
    print("Let's start to set the configuration of each game user. \n")

    # Get configuration for Game User 1.
  
    list_of_pokemon1= get_data_from_user("coach_1_pokemons.csv")

    # Get configuration for Game User 2.
    list_of_pokemon2= get_data_from_user("coach_2_pokemons.csv")

    for pokemon in list_of_pokemon1:
      print(pokemon)
    for pokemon in list_of_pokemon2:
      print(pokemon)

    print("------------------------------------------------------------------")
    print("The Game starts...")
    print("------------------------------------------------------------------")

    # Get a copy of the list of pokemons:
    copy1= list_of_pokemon1.copy()
    copy2= list_of_pokemon2.copy()

    # Choose first pokemons
    copy1= get_pokemon_in_a_list_of_pokemons(1,copy1)
    id= int(input(""))
    pokemon1= None
    for pokemon in copy1:
      if pokemon.get_id()==id:
        pokemon1= pokemon

    copy2= get_pokemon_in_a_list_of_pokemons(2,copy2)
    id= int(input(""))
    pokemon2= None
    for pokemon in copy2:
      if pokemon.get_id()==id:
        pokemon2= pokemon

    # Main loop.

    while coach_is_undefeated(copy1) and coach_is_undefeated(copy2):
      if not pokemon1.is_alive():
        copy1= get_pokemon_in_a_list_of_pokemons(1,copy1)
        id= int(input(""))
        pokemon1= None
        for pokemon in copy1:
          if pokemon.get_id()==id:
            pokemon1= pokemon
      if not pokemon2.is_alive():
        copy2= get_pokemon_in_a_list_of_pokemons(2,copy2)
        id= int(input(""))
        pokemon2= None
        for pokemon in copy2:
          if pokemon.get_id()==id:
            pokemon2= pokemon
      pokemon1.fight_attack(pokemon2)
      pokemon2.fight_attack(pokemon1)
      

    print("------------------------------------------------------------------")
    print("The Game has end...")
    print("------------------------------------------------------------------")


    print("------------------------------------------------------------------")
    print("Statistics")
    print("------------------------------------------------------------------")
    print("Game User 1:")
    for pokemon in copy1:
      print(pokemon)

    print("Game User 2:")
    for pokemon in copy2:
      print(pokemon)


# Checking whether this module is executed just itself alone.
if __name__ == "__main__":
    main()


# EOF
