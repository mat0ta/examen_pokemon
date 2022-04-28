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
from pokemon import Pokemon
from weapon_type import WeaponType


class PokemonEarth(Pokemon):
    """Python class to implement a basic version of a Pokemon of the game.

    This Python class implements the basic version of a Pokemon of the game.

    Syntax
    ------
      obj = PokemonEarth(id, pokemon_name, weapon_type, health_points,
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
      >>> obj_Pokemon = PokemonEarth(1, "Diglett", WeaponType.PUNCH, 100, 7, 10)
    """


    def __init__(self, pokemon_id, pokemon_name, weapon_type, health_points,
                 attack_rating, defense_rating):
        """Constructor of the class.

        This special method is executed when an object of this class is
        created.

        Syntax
        ------
          [ ] = __init__(self, id, pokemon_name, weapon_type, health_points,
                         attack_rating, defense_rating)

        Parameters
        ----------
          [in] self Python object that represents an instance of the
                    class Pokemon.
          [in] pokemon_id ID of Pokemon.
          [in] pokemon_name Name of the Pokemon.
          [in] weapon_type Type of weapon that carries out the Pokemon.
          [in] health_points Points of health that the Pokemon has.
          [in] attack_rating Attack rating of the Pokemon.
          [in] defense_rating Defense rating of the Pokemon.

        Returns
        -------
          obj Python object output parameter that represents an instance
              of the class Pokemon.

        Exceptions
        ----------
          TypeError:
            If the parameter id is NOT a int.
            If the parameter pokemon_name is NOT a String.
            If the parameter weapon_type is NOT a enum WeaponType.
            If the parameter health_points is NOT be an int.
            If the parameter attack_rating is NOT be a int.
            If the parameter defense_rating is NOT be a int.

          ValueError:
            If the parameter id is already found in other Pokemon.
            If the parameter health_points is NOT > 0 and <= 100.
            If the parameter attack_rating is NOT > 0 and <= 10.
            If the parameter defense_rating is NOT > 0 and <= 10.

        Example
        -------
          >>> from pokemon import Pokemon
          >>> from weapon_type import WeaponType
          >>> obj_Pokemon = PokemonEarth(1, "Diglett", WeaponType.PUNCH, 100, 7, 10)
        """

        super().__init__(pokemon_id, pokemon_name, weapon_type, health_points,
                         attack_rating, 10)

        if isinstance(defense_rating, int):
            if 11 <= defense_rating <= 20:
                self._defense_rating = defense_rating
            else:
                raise ValueError("The parameter defense_rating should be > 11 and <= 20.")
        else:
            raise TypeError("The parameter defense_rating should be a int.")


    def set_defense_rating(self, defense_rating_to_be_set):
        """Method to set the attribute defense_rating of the object.

        Method to set the attribute defense_rating based on a human-readable
        format of the object that is formed in this class.

        Syntax
        ------
          [ ] = obj_Pokemon.set_defense_rating( )

        Parameters
        ----------
          [in] self Python object that represents an instance of the
                    class Pokemon.
          [in] defense_rating_to_be_set String that contains the defense rating
                                        to assign to the Pokemon.

        Returns
        -------

        Exceptions
        ----------
          TypeError If the parameter defense_rating_to_be_set is NOT a int.
          ValueError If the parameter defense_rating_to_be_set is NOT > 0 and <= 10.

        Example
        -------
          >>> from Pokemon import Pokemon
          >>> obj_Pokemon = Pokemon()
          >>> obj_Pokemon.set_attack_rating(8)
        """
        if isinstance(defense_rating_to_be_set, int):
            if 11 <= defense_rating_to_be_set <= 20:
                self._defense_rating = defense_rating_to_be_set
            else:
                raise ValueError("The parameter defense_rating_to_be_set should be > 11 and <= 20.")
        else:
            raise TypeError("The parameter defense_rating_to_be_set should be a int.")


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
    pokemon_1 = PokemonEarth(1, "Diglett", WeaponType.HEADBUTT, 100, 8, 15)

    if pokemon_1.get_pokemon_name() == "Diglett":
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

    if pokemon_1.get_defense_rating() == 15:
        print("Test PASS. The parameter defense_rating has been correctly set.")
    else:
        print("Test FAIL. Check the method __init__().")


    print("=================================================================.")
    print("Test Case 2: Human-readable format of the object.")
    print("=================================================================.")
    pokemon_2 = PokemonEarth(7, "Diglett", WeaponType.HEADBUTT, 100, 7, 12)

    if str(pokemon_2) == "Pokemon ID 7 with name Diglett has as weapon HEADBUTT and health 100":
        print("Test PASS. The human-readable format of the object has been implemented correctly.")
    else:
        print("Test FAIL. Check the method __str__()." + " RESULT: " + str(pokemon_2))


    print("=================================================================.")
    print("Test Case 3: Pokemon alive?¿?.")
    print("=================================================================.")
    pokemon_3 = PokemonEarth(3, "Diglett", WeaponType.KICK, 97, 8, 15)

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
    pokemon_4 = PokemonEarth(4, "Diglett", WeaponType.ELBOW, 93, 9, 11)

    pokemon_4.fight_defense(70)

    if pokemon_4.get_health_points() == 34:
        print("Test PASS. The method fight_defense() has been implemented correctly.")
    else:
        print("Test FAIL. Check the method fight_defense().")


    print("=================================================================.")
    print("Test Case 5: Check the attack during a Fight.")
    print("=================================================================.")
    pokemon_5 = PokemonEarth(5, "Diglett", WeaponType.PUNCH, 99, 10, 20)
    pokemon_6 = PokemonEarth(6, "Diglett", WeaponType.PUNCH, 99, 9, 18)

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
