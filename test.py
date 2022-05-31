from wallet import Wallet
from planet import Planet
from land import Land
import tokenomics as token

def print_indented (item) -> None:
    '''
    Prints a given value and indents it.
    '''
    print(f'    {item}')  

def print_list (li: list) -> None:
    '''
    Prints the contents of a list.
    '''

    print('List: ')
    for item in li:

        print_indented(item)

def test_classes () -> None:

    print("Testing Land Basics:")
    land_1 = Land(1, 4, 1)

    print("test Land.__str__ :")
    print_indented(land_1)

    print("test land_1.get_claimable_quid() by value:")
    print(land_1.get_claimable_quid() == 0)

    print("test land_1.set_claimable_quid() by value:")
    land_1.set_claimable_quid(1000)
    print(land_1.get_claimable_quid() == 1000)

    print("test land_1.get_id() by value:")
    print(land_1.get_id() == 1)

    print("test land_1.get_planet_id() by value:")
    print(land_1.get_planet_id() == 1)

    print("test land_1.get_owner_id() by value:")
    print(land_1.get_owner_id() == 1)

    print("test land_1.set_owner_id() by value:")
    land_1.set_owner_id(5)
    print(land_1.get_owner_id() == 5)

    print("---------------------------")
    
    print("Testing Planet Basics:")
    planet_1 = Planet(1, 4)

    print("test Planet.__str__ :")
    print(planet_1)

    print("test planet_1.get_id() by value:")
    print(planet_1.get_id() == 1)

    print("test planet_1.get_class() by value:")
    print(planet_1.get_class() == 4)

    print("test planet_1.get_owner_id() by value:")
    print(planet_1.get_owner_id() == 1)

    print("test planet_1.set_owner_id() by value:")
    planet_1.set_owner_id(5)
    print(planet_1.get_owner_id() == 5)

    print("test planet_1.get_claimable_quid() by value:")
    print(planet_1.get_claimable_quid() == 0)

    print("test planet_1.set_claimable_quid() by value:")
    planet_1.set_claimable_quid(1000)
    print(planet_1.get_claimable_quid() == 1000)

    print("test planet_1.land_available() by value:")
    print(planet_1.land_available() == True)

    print("test planet_1.calc_max_land() by value:")
    print(Planet.calc_max_land())

    print("test planet_1.discover_land() by land_list")
    land_2 = planet_1.discover_land()
    print_indented(land_2)

    print("test planet_1.discover_land() when list is full")
    while (planet_1.land_available()):
        planet_1.discover_land()

    planet_1.discover_land()
    print(planet_1.land_available() == False)

    land_list = planet_1.get_land_list()
    print_list(land_list)
    
    print("---------------------------")

    print("Testing Wallet Basics:")
    wallet_1 = Wallet(1000.0)

    print("test Wallet.__str__ :")
    print(wallet_1)

    print("test Wallet.total_wallets by value:")
    print(Wallet.total_wallets == 1)

    print("test wallet_1.get_quid() by value:")
    print(wallet_1.get_quid() == 1000)

    print("test wallet_1.get_id() by value:")
    print(wallet_1.get_id() == 1)

    print("test wallet_1.set_quid() by value:")
    wallet_1.set_quid(2000.0)
    print(wallet_1.get_quid() == 2000)
    
    print("---------------------------")

def test_tokenomics():

    token.init_wallets(4, 50000)
    print("test init_wallets() by value of available quid")
    print(token.available_quid == 449800000)

    print("test init_wallets() by value of contents of wallet list")
    print_list(token.wallets)

    print('')
    
    wallet_1 = token.find_wallet(1)
    wallet_2 = token.find_wallet(2)
    wallet_3 = token.find_wallet(3)
    wallet_4 = token.find_wallet(4)

    print("------------Buy Planet Test 1-------------")

    print("test buy_planet(4) by wallet.get_quid()")
    token.buy_planet(wallet_1, 4)
    print(wallet_1.get_quid() == 30000)

    print("test buy_planet(4) by length of wallet.get_planet_list()")
    print(len(wallet_1.get_planet_list()) == 1)

    print("test buy_planet(4) by contents of wallet.get_planet_list()")
    print(f'    {wallet_1.get_planet_list()[0]}')

    print("test buy_planet(4) by contents of planets")
    print_list(token.planets)

    print("test buy_planet(4) by value of available_planets")
    print(token.available_planets[4] == 2499)

    print()
    print("------------Buy Planet Test 2-------------")

    print("test buy_planet(3) by wallet.get_quid()")
    token.buy_planet(wallet_1, 3)
    print(wallet_1.get_quid() == 18000)

    print("test buy_planet(3) by length of wallet.get_planet_list()")
    print(len(wallet_1.get_planet_list()) == 2)

    print("test buy_planet(3) by contents of wallet.get_planet_list()")
    print(f'    {wallet_1.get_planet_list()[1]}')

    print("test buy_planet(3) by contents of planets")
    print_list(token.planets)

    print("test buy_planet(3) by value of available_planets")
    print(token.available_planets[3] == 4999)

    print()
    print("------------Buy Planet Test 3-------------")

    print("test buy_planet(2) by wallet.get_quid()")
    token.buy_planet(wallet_1, 2)
    print(wallet_1.get_quid() == 12000)

    print("test buy_planet(2) by length of wallet.get_planet_list()")
    print(len(wallet_1.get_planet_list()) == 3)

    print("test buy_planet(2) by contents of wallet.get_planet_list()")
    print(f'    {wallet_1.get_planet_list()[2]}')

    print("test buy_planet(2) by contents of planets")
    print_list(token.planets)

    print("test buy_planet(2) by value of available_planets")
    print(token.available_planets[2] == 7499)

    print()
    print("------------Buy Planet Test 4-------------")

    print("test buy_planet(1) by wallet_1.get_quid()")
    token.buy_planet(wallet_2, 1)
    print(wallet_2.get_quid() == 48400)

    print("test buy_planet(1) by length of wallet.get_planet_list()")
    print(len(wallet_2.get_planet_list()) == 1)

    print("test buy_planet(1) by contents of wallet.get_planet_list()")
    print(f'    {wallet_2.get_planet_list()[0]}')

    print("test buy_planet(1) by contents of planets")
    print_list(token.planets)

    print("test buy_planet(1) by value of available_planets")
    print(token.available_planets[1] == 9999)

    print()
    print("------------Buy Planet Test 5-------------")

    print("test buy_planet() when no funds via wallet quid")
    token.buy_planet(wallet_1, 4)
    print(wallet_1.get_quid() == 12000)

    print("test buy_planet() when no funds via wallet's planet list")
    print(len(wallet_1.get_planet_list()) == 3)

    print("test buy_planet() when no funds via simulator's planet list")
    print_list(token.planets)

    print("test buy_planet() when no funds via available planets")
    print(token.available_planets[4] == 2499)

    print()
    print("------------Buy Planet Test 6-------------")

    old_val = token.available_planets[1]
    token.available_planets[1] = 0

    print("test buy_planet() when no planets via wallet quid")
    token.buy_planet(wallet_1, 1)
    print(wallet_1.get_quid() == 12000)

    print("test buy_planet() when no planets via wallet's planet list")
    print(len(wallet_1.get_planet_list()) == 3)

    print("test buy_planet() when no planets via simulator's planet list")
    print_list(token.planets)

    print("test buy_planet() when no planets via available planets")
    print(token.available_planets[1] == 0)

    token.available_planets[1] == old_val

    print()
    print("------------Buy Land Test 1-------------")

    token.buy_planet(wallet_4, 4)
    planet_1 = wallet_4.get_planet_list()[0]
    token.buy_land(planet_1)

    print("test buy_land by wallet_4.get_quid()")
    print(wallet_4.get_quid() == 29800)

    print("test buy_land by simulator's land list")
    print_list(token.lands)

    print("test buy_land by wallet's land list")
    print_list(wallet_4.get_land_list())

    print("test buy_land by planet's land list")
    print_list(planet_1.get_land_list())

    print()
    print("------------Buy Land Test 2-------------")

    while (planet_1.land_available()):

        token.buy_land(planet_1)

    print("values before buying land:")
    init_balance = wallet_4.get_quid()
    print_list(planet_1.get_land_list())
    print_list(wallet_4.get_land_list())
    print_list(token.lands)

    token.buy_land(planet_1)

    print("test buy_land when no lands available by wallet_4.get_quid()")
    print(wallet_4.get_quid() == init_balance)

    print("test buy_land when no lands available by simulator's land list")
    print_list(token.lands)

    print("test buy_land when no lands available by wallet's land list")
    print_list(wallet_4.get_land_list())

    print("test buy_land when no lands available by planet's land list")
    print_list(planet_1.get_land_list())

    print()
    print("------------Buy Land Test 3-------------")

    token.buy_planet(wallet_3, 2)
    planet_2 = wallet_3.get_planet_list()[0]
    init_balance = wallet_3.get_quid()
    wallet_3.set_quid(0)

    print("values before buying land:")
    print_list(planet_2.get_land_list())
    print_list(wallet_3.get_land_list())
    print_list(token.lands)

    token.buy_land(planet_2)

    print("test buy_land when no funds by wallet_3.get_quid()")
    print(wallet_3.get_quid() == 0)

    print("test buy_land when no lands available by simulator's land list")
    print_list(token.lands)

    print("test buy_land when no lands available by wallet's land list")
    print_list(wallet_3.get_land_list())

    print("test buy_land when no lands available by planet's land list")
    print_list(planet_2.get_land_list())

    wallet_3.set_quid(init_balance)

    print()
    print("------------Dispense Quid Test 1-------------")

    token.buy_land(planet_2)
    token.buy_land(planet_2)

    print("Lands before dispense:")
    print_list(token.lands)
    print("Planets before dispense:")
    print_list(token.planets)
    print("Wallets before dispense:")
    print_list(token.wallets)
    print("Available quid before dispense")
    print(token.available_quid)

    token.dispense_daily_quid()

    print("Lands after dispense:")
    print_list(token.lands)
    print("Planets after dispense:")
    print_list(token.planets)
    print("Wallets after dispense:")
    print_list(token.wallets)
    print("Available quid after dispense")
    print(token.available_quid)

    print()
    print("------------Dispense Quid Test 2-------------")

    token.dispense_daily_quid()

    print("Lands after dispense:")
    print_list(token.lands)
    print("Planets after dispense:")
    print_list(token.planets)
    print("Wallets after dispense:")
    print_list(token.wallets)
    print("Available quid after dispense")
    print(token.available_quid)

    print()
    print("------------Claim Quid Test 1-------------")

    print("Lands before claim:")
    print_list(token.lands)
    print("Planets before claim:")
    print_list(token.planets)
    print("Wallets before claim:")
    print_list(token.wallets)
    print("Available quid before claim")
    print(token.available_quid)

    token.claim_quid(wallet_4)

    print("Lands after claim:")
    print_list(token.lands)
    print("Planets after claim:")
    print_list(token.planets)
    print("Wallets after claim:")
    print_list(token.wallets)
    print("Available quid after claim")
    print(token.available_quid)

    token.claim_quid(wallet_4)

    print()
    print("------------Claim Quid Test 2-------------")

    token.claim_quid(wallet_4)

    print("Lands after claim:")
    print_list(token.lands)
    print("Planets after claim:")
    print_list(token.planets)
    print("Wallets after claim:")
    print_list(token.wallets)
    print("Available quid after claim")
    print(token.available_quid)

    token.claim_quid(wallet_4)




    

