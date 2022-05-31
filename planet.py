from land import Land
import random

class Planet:
    '''
    Planet: represents one Space Tokens Planet NFT with the following attributes:
        __claimable_quid: The available quid to be claimed from the planet
        __land_list: A list of the Land NFTs discovered on the planet
        __max_land: the maximum amount of lands to discover on the planet
        __owner_id: The id of the wallet that owns the planet
        __planet_class: The class of the planet
    '''

    '''The total number of planets in existence'''
    total_planets = 0

    def __init__ (self, owner_id: int, planet_class: int):

        self.__planet_class = planet_class
        self.__max_land = Planet.calc_max_land()
        self.__land_list = []
        self.__owner_id = owner_id
        self.__claimable_quid = 0.0

        Planet.total_planets += 1
        self.__planet_id = Planet.total_planets

    def __str__ (self):

        return f'(Planet) Id: {self.__planet_id} Class: {self.__planet_class} Owner: {self.__owner_id} Quid: {self.__claimable_quid}'

    def get_id (self) -> int:
        '''
        Returns the planet's id
        '''
        return self.__planet_id

    def get_class (self) -> int:
        '''
        Returns the planet's class
        '''
        return self.__planet_class

    def get_owner_id (self) -> int:
        '''
        Returns the id of the wallet that owns the planet
        '''
        return self.__owner_id

    def set_owner_id (self, owner_id: int) -> None:
        '''
        Sets the id of the owner wallet to a given value
        '''
        self.__owner_id = owner_id

    def get_claimable_quid (self) -> float:
        '''
        Returns the amount of claimable quid in the planet
        '''
        return self.__claimable_quid

    def set_claimable_quid (self, quid) -> None:
        '''
        Sets the amount of claimable quid in the planet to a specified value
        '''
        self.__claimable_quid = quid

    def get_land_list (self) -> list[Land]:

        return self.__land_list

    def land_available (self) -> bool:
        '''
        Returns true if land can be discovered on planet, otherwise false
        '''
        return len(self.__land_list) < self.__max_land

    def discover_land (self) -> Land:
        '''
        If possible, discovers and creates a new Land NFT from the planet
        '''
        if self.land_available():

            new_land = Land(self.__planet_id, self.__planet_class, self.__owner_id)
            self.__land_list.append(new_land)

            return new_land

        else:
            return None
    
    def calc_max_land () -> int:
        '''
        Returns a randomly chosen size for the planet
        '''
        return random.randint(3, 7)