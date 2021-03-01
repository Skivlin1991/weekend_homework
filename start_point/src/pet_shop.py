
def get_pet_shop_name(cc_pet_shop):
    return cc_pet_shop ["name"]

def get_total_cash(cc_pet_shop):
    return cc_pet_shop["admin"]["total_cash"]

def add_or_remove_cash(cc_pet_shop, cash):
    cc_pet_shop["admin"]["total_cash"] += cash

def get_pets_sold(cc_pet_shop):
    return cc_pet_shop["admin"]["pets_sold"]

def increase_pets_sold(cc_pet_shop, number):
    cc_pet_shop["admin"]["pets_sold"] += number 

def get_stock_count(cc_pet_shop):
    return len (cc_pet_shop["pets"])

def get_pets_by_breed(cc_pet_shop, breed):
    pets_by_breed = []
    for pet in cc_pet_shop["pets"]:
        if pet ["breed"] == breed:
            pets_by_breed.append(pet)
    return pets_by_breed
def find_pet_by_name(cc_pet_shop, name):
    for pet in cc_pet_shop["pets"]:
        if pet ["name"] == name:
           return pet 

def remove_pet_by_name(cc_pet_shop, name):
     for pet in cc_pet_shop["pets"]:
        if pet["name"] == name:
         cc_pet_shop["pets"].remove(pet)
def add_pet_to_stock (cc_pet_shop, new_pet):
    cc_pet_shop["pets"].append(new_pet)

def get_customer_cash(customer):
    return customer["cash"]
def remove_customer_cash(customer,number):
    customer["cash"] -=number 

def get_customer_pets_count(customer_pets):
    return len ("customer"["pets"]) 

def add_pet_to_customer(customer,pet):
    for customer in customer["name"]:
        list [2].append(pet)
        return (customer+pet)
#optioanl
def test_customer_can_afford_pet__sufficient_funds(costomer,cash):
        customer = [cash] .customers[0]
        can_buy_pet = customer(customer,cash.new_pet)
        return (True, can_buy_pet)
        
def test_customer_can_afford_pet__insufficient_funds(costomer,cash):
            customer = [cash].customers[1]
            can_buy_pet = customer(customer, cash.new_pet)
            (False,can_buy_pet)