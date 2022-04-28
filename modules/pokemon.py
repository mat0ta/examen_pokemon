#!/usr/bin/env python
# -*- coding: utf-8 -*-


"""
This Python module contains not only the class Pokemon, but also the test of
this Python class.

@contents :  This module contains not only a single Python class, but also the
             test cases to probe its functionality.
@project :  N/A
@program :  N/A
@file :  pokemon.py
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

from weapon_type import WeaponType

class Pokemon():
  """Python class to implement a basic version of a Pokemon of the game.

  This Python class implements the basic version of a Pokemon of the game.

  Syntax
  ------
    obj = Pokemon(id, pokemon_name, weapon_type, health_points,
                   attack_rating, defense_rating)

  Parameters
  ----------
    [in] id ID of the Pokemon.
    [in] pokemon_name Name of the Pokemon.
    [in] weapon_type Type of weapon that carries out the Pokemon.
    [in] health_points Points of health that the Pokemon has.
    [in] attack_rating Attack rating of the Pokemon.
    [in] defense_rating Defense rating of the Pokemon.

  Returns
  -------
    obj Python object output parameter that represents an instance
        of the class Pokemon.

  Attributes
  ----------

  Example
  -------
    >>> from pokemon import Pokemon
    >>> from weapon_type import WeaponType
    >>> obj_Pokemon = Pokemon(1, "Bulbasaur", WeaponType.PUNCH, 100, 7, 10)
  """
  lista_ids= []

  def __init__ (self, id, pokemon_name, weapon_type, health_points, attack_rating, defense_rating, attack_range= range(1,11), defense_range= range(1,11)):
    if not id in Pokemon.lista_ids:
      self.id= id 
      if type (pokemon_name) is str:
        self.pokemon_name= pokemon_name
      else:
        raise ValueError("Name is not a string")
      if type (weapon_type) is WeaponType:
        self.weapon_type= weapon_type
      else:
        raise ValueError("Weapon is not a weapon type")
      if type (health_points) is int:
        if health_points>= 1 and health_points<=100:
          self.health_points= health_points
        else:
          raise ValueError("Health points is not in range (1..100)")
      else:
        raise ValueError("Health points is not a integer")
      if type (attack_rating) is int:
        if attack_rating in attack_range:
          self.attack_rating= attack_rating
        else:
          raise ValueError("Attack rating is not in range")
      else:
        raise ValueError("Attack rating is not a integer")
      if type (defense_rating) is int:
        if defense_rating in defense_range:
          self.defense_rating= defense_rating
        else:
          raise ValueError("Defense rating is not in range")
      else:
        raise ValueError("Defense rating is not a integer")

    else:
      raise ValueError("Pokemon id duplicate")
    Pokemon.lista_ids.append(id)

  def __del__ (self):
    indice= Pokemon.lista_ids.index(self.id)
    del (Pokemon.lista_ids[indice])

  def __str__ (self):
    cadena= "Pokemon ID "+ str(self.id)+ " with name "+ self.pokemon_name+ " has as weapon "+ self.weapon_type.name+ " and health "+ str(self.health_points)
    return cadena

  """No hace falta implementar los métodos set porque los
  atributos se establecen en el constructor y no hace falta 
  establecerlos de nuevo más adelante. Ninguno de ellos cambia
  salvo la salud pero esta se actualiza en el método     
  fight_defense
  """
  
  def get_id (self):
    return self.id
    
  def get_pokemon_name (self):
    return self.pokemon_name

  def get_weapon_type (self):
    return self.weapon_type

  def get_health_points (self):
    return self.health_points

  def get_attack_rating (self):
    return self.attack_rating

  def get_defense_rating (self):
    return self.defense_rating

  def is_alive (self):
    return self.health_points > 0

  def fight_defense (self,points_of_damage):
    if points_of_damage <= self.defense_rating:
      return False
    else:
      self.health_points -= (points_of_damage- self.defense_rating)
      return True

  def fight_attack (self,pokemon_to_attack):
    return pokemon_to_attack.fight_defense(self.attack_rating)
    
def main():
    """Function main of the module.

    The function main of this module is used to test the Class that is described
    in this module.

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

    print("=================================================================.")
    print("Test Case 1: Create a Pokemon.")
    print("=================================================================.")
    pokemon_1 = Pokemon(1, "Ivysaur", WeaponType.HEADBUTT, 100, 8, 9)

    if pokemon_1.get_pokemon_name() == "Ivysaur":
        print("Test PASS. The parameter pokemon_name has been correctly set.")
    else:
        print("Test FAIL. Check the method __init__().")

    if pokemon_1.get_weapon_type().name == "HEADBUTT":
        print("Test PASS. The parameter weapon_type has been correctly set.")
    else:
        print("Test FAIL. Check the method __init__().")

    if pokemon_1.get_health_points() == 100:
        print("Test PASS. The parameter health_points has been correctly set.")
    else:
        print("Test FAIL. Check the method __init__().")

    if pokemon_1.get_attack_rating() == 8:
        print("Test PASS. The parameter attack_rating has been correctly set.")
    else:
        print("Test FAIL. Check the method __init__().")

    if pokemon_1.get_defense_rating() == 9:
        print("Test PASS. The parameter defense_rating has been correctly set.")
    else:
        print("Test FAIL. Check the method __init__().")


    print("=================================================================.")
    print("Test Case 2: Human-readable format of the object.")
    print("=================================================================.")
    pokemon_2 = Pokemon(2, "Charmander", WeaponType.HEADBUTT, 100, 7, 10)

    if str(pokemon_2) == "Pokemon ID 2 with name Charmander has as weapon HEADBUTT and health 100":
        print("Test PASS. The human-readable format of the object has been implemented correctly.")
    else:
        print("Test FAIL. Check the method __str__()." + " RESULT: " + str(pokemon_2))


    print("=================================================================.")
    print("Test Case 3: Pokemon alive?¿?.")
    print("=================================================================.")
    pokemon_3 = Pokemon(3, "Wartortle", WeaponType.KICK, 97, 8, 9)

    if pokemon_3.is_alive():
        pokemon_3.fight_defense(200)  # With this the Pokemon should be retired.

        if not pokemon_3.is_alive():
            print("Test PASS. The method is_alive() has been implemented correctly.")
        else:
            print("Test FAIL. Check the method is_alive().")
    else:
        print("Test FAIL. Check the method is_alive().")


    print("=================================================================.")
    print("Test Case 4: Check the defense during a Fight.")
    print("=================================================================.")
    pokemon_4 = Pokemon(4, "Squirtle", WeaponType.ELBOW, 93, 9, 6)

    pokemon_4.fight_defense(70)

    if pokemon_4.get_health_points() == 29:
        print("Test PASS. The method fight_defense() has been implemented correctly.")
    else:
        print("Test FAIL. Check the method fight_defense().")


    print("=================================================================.")
    print("Test Case 5: Check the attack during a Fight.")
    print("=================================================================.")
    pokemon_5 = Pokemon(5, "Venusaur", WeaponType.PUNCH, 99, 10, 7)
    pokemon_6 = Pokemon(6, "Charmeleon", WeaponType.PUNCH, 99, 9, 8)

    pokemon_was_hit = pokemon_5.fight_attack(pokemon_6)

    if pokemon_was_hit:
        if pokemon_6.get_health_points() == 97:
            print("Test PASS. The method fight_attack() has been implemented correctly.")
        else:
            print("Test FAIL. Check the method fight_attack().")
    else:
        if pokemon_6.get_health_points() == 99:
            print("Test PASS. The method fight_attack() has been implemented correctly.")
        else:
            print("Test FAIL. Check the method fight_attack().")



# Checking whether this module is executed just itself alone.
if __name__ == "__main__":
    main()


# EOF
