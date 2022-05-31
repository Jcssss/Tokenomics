from wallet import Wallet
from planet import Planet
from land import Land

'''The cost (in quid) to purchase a land'''
LAND_COST = 200

'''The cost (in quid) of each class of planet'''
PLANET_COST = {
    1: 1600,
    2: 6000,
    3: 12000,
    4: 20000
}

'''The daily quid acquired by each land class'''
DAILY_QUID = {
    1: 0.2,
    1031: 0.5,
    1225: 0.5,
    2: 0.75,
    3: 1.5,
    4: 2.5
}

'''The amount of planets in each class that can be purchased'''
available_planets = {
    1: 10000,
    2: 7500,
    3: 5000,
    4: 2500
}

'''The total amount of quid that can be given out'''
available_quid = 450000000

'''Lists containing all wallets, planets, and lands in existence'''
wallets = []
planets = []
lands = []

def init_wallets (num_wallets: int, start_quid: float) -> None:

    '''
    Initializes a given number of wallets with initial starting quid
    '''

    # update available quid
    global available_quid 
    available_quid -= num_wallets * start_quid
    
    # initialize wallets
    for i in range(num_wallets):
        wallets.append(Wallet(start_quid))

def find_wallet (id: int) -> Wallet:

    '''
    Finds and returns the the wallet with the given id, 
    returns None if no wallet with the given id exists.
    '''

    for wallet in wallets:

        if wallet.get_id() == id:

            return wallet

    return None

def buy_land (planet: Planet) -> None:

    '''
    Purchases a land NFT from a given planet
    '''

    # find the wallet that owns the planet
    action_wallet_id = planet.get_owner_id()
    action_wallet = find_wallet(action_wallet_id)

    # checks that wallet can afford, and planet has discoverable land
    if (action_wallet.get_quid() >= LAND_COST and
        planet.land_available()):

        # updates wallet's quid
        balance = action_wallet.get_quid()
        action_wallet.set_quid(balance - LAND_COST)

        # creates land and adds it to the appropriate lists
        new_land = planet.discover_land()

        action_wallet.add_land(new_land)
        lands.append(new_land)

def buy_planet (action_wallet: Wallet, planet_class: int) -> None:

    '''
    Purchases a planet NFT for a given wallet
    '''

    # checks that wallet can afford, and that there are planets in stock
    if (action_wallet.get_quid() >= PLANET_COST[planet_class] and 
        available_planets[planet_class] != 0):

        # updates wallet's quid
        balance = action_wallet.get_quid()
        action_wallet.set_quid(balance - PLANET_COST[planet_class])

        # creates planet and adds it to the appropriate lists
        new_planet = Planet(action_wallet.get_id(), planet_class)
        action_wallet.add_planet(new_planet)
        planets.append(new_planet)

        # updates the amount of planets available
        available_planets[planet_class] -= 1

def claim_quid (wallet: Wallet) -> None:

    '''
    Claims all available quid for a given Wallet
    '''

    # gets required variables
    planet_list = wallet.get_planet_list()
    land_list = wallet.get_land_list()
    balance = wallet.get_quid()

    # claims quid from every planet owned by wallet
    for planet in planet_list:

        claimable_quid = planet.get_claimable_quid()
        planet.set_claimable_quid(0)

        balance += claimable_quid

    # claims quid from every land owned by wallet
    for land in land_list:

        claimable_quid = land.get_claimable_quid()
        land.set_claimable_quid(0)

        balance += claimable_quid

    # updates wallet's quid
    wallet.set_quid(balance)

def dispense_daily_quid () -> None:

    '''
    Dispenses daily quid to be claimed
    '''
    global available_quid

    # iterates through every planet
    for planet in planets:

        # gets required variables
        land_list = planet.get_land_list()
        planet_class = planet.get_class()
        planet_quid = planet.get_claimable_quid()
        daily_quid = DAILY_QUID[planet_class]

        # iterates through every land on planet
        for land in land_list:

            # updates land's quid
            land_quid = land.get_claimable_quid()
            land_quid += round(daily_quid * 0.9, 4)
            land.set_claimable_quid(land_quid)

            # increments planet's quid
            planet_quid += round(daily_quid * 0.1, 4)

            # updates available quid
            available_quid = round(available_quid - daily_quid, 4)

        # updates planet's quid
        planet.set_claimable_quid(planet_quid)