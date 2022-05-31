class Land:
    '''
    Land: represents one Space Tokens Land NFT with the following attributes:
        __claimable_quid: The available quid to be claimed from the land
        __land_class: the class of the land
        __land_id: A numerical integer unique to each land
        __owner_id: The id of the wallet that owns the land
        __planet_id: The id of the planet on which the land was discovered
    '''

    '''The total number of lands in existence'''
    total_lands = 0

    def __init__ (self, planet_id: int, land_class: int, owner_id: int):

        self.__land_class = land_class
        self.__claimable_quid = 0.0
        self.__planet_id = planet_id
        self.__owner_id = owner_id

        Land.total_lands += 1
        self.__land_id = Land.total_lands

    def __str__ (self) -> str:

        return f'(Land) Id: {self.__land_id} Class: {self.__land_class} Owner: {self.__owner_id} Quid: {self.__claimable_quid}'

    def get_claimable_quid (self) -> float:
        '''
        Returns the amount of claimable quid in the land
        '''
        return self.__claimable_quid

    def set_claimable_quid (self, new_quid: int) -> None:
        '''
        Sets the amount of claimable quid in the land to a specified value
        '''
        self.__claimable_quid = new_quid

    def get_id (self) -> int:
        '''
        Returns the land's id
        '''
        return self.__land_id

    def get_planet_id (self) -> int:
        '''
        Returns the id of the planet where the land exists
        '''
        return self.__planet_id

    def get_owner_id (self) -> int:
        '''
        Returns the id of the wallet that owns the land
        '''
        return self.__owner_id
        
    def set_owner_id (self, new_owner_id: int) -> None:
        '''
        Sets the id of the wallet that owns the land to target value
        '''
        self.__owner_id = new_owner_id