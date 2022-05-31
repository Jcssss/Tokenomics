from planet import Planet
from land import Land

class Wallet:

    '''
    Wallet: represents an NFT holder's wallet with the following properties:
        __land_list: the Land NFTs owned by the wallet
        __planet_list: the Planet NFTs owned by the wallet
        __quid: the quid owned by the wallet
        __wallet_id: the unique integer id of the wallet
    '''

    '''The total number of wallets in existence'''
    total_wallets = 0

    def __init__ (self, start_quid: float) -> None:

        Wallet.total_wallets += 1
        self.__wallet_id = Wallet.total_wallets
        self.__planet_list = []
        self.__land_list = []
        self.__quid = start_quid

    def __str__ (self) -> str:

        return f'Id: {self.__wallet_id} Balance: {self.__quid}'

    def get_id (self) -> int:
        '''
        Returns the id of the wallet
        '''
        return self.__wallet_id

    def get_quid (self) -> float:
        '''
        Returns the quid owned by the wallet
        '''
        return self.__quid

    def set_quid (self, quid: float) -> None:
        '''
        Sets the quid owned by a wallet to a specific amount
        '''
        self.__quid = quid

    def add_planet (self, planet: Planet) -> None:
        '''
        Adds a planet to the wallet's list of owned planets
        '''
        self.__planet_list.append(planet)

    def remove_planet (self, planet: Planet) -> None:
        '''
        Removes a planet from the wallet's list of owned planets
        '''
        if planet in self.__planet_list:

            self.__planet_list.remove(planet)

    def add_land (self, land: Land) -> None:
        '''
        Adds a land to the wallet's list of owned lands
        '''
        self.__land_list.append(land)

    def remove_land (self, land: Land) -> None:
        '''
        Removes a land from the wallet's list of owned lands
        '''
        if land in self.__land_list:

            self.__land_list.remove(land)

    def get_planet_list (self) -> list[Planet]:
        '''
        Return's the wallet's list of owned planets
        '''
        return self.__planet_list

    def get_land_list (self) -> list[Land]:
        '''
        Return's the wallet's list of owned lands
        '''
        return self.__land_list