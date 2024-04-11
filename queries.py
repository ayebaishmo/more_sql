# query_1 = 'SELECT * FROM charactercreator_character;'

# - `TOTAL_CHARACTERS`: How many total Characters are there?
TOTAL_CHARACTERS = '''
    SELECT name,
    COUNT(name)
    FROM charactercreator_character'''

# - `TOTAL_SUBCLASS`: How many of each specific subclass (the `necromancer` table)?
TOTAL_SUBCLASS = '''
    SELECT mage_ptr_id,
    COUNT(mage_ptr_id)
    FROM charactercreator_necromancer'''

# - `TOTAL_ITEMS`: How many total Items?

TOTAL_ITEMS = '''
    SELECT item_id,
    COUNT(item_id)
    FROM armory_item
    '''

# - `WEAPONS`: How many of the Items are weapons? 

WEAPONS_itemss = ''' 
    SELECT item_ptr_id,
    COUNT(item_ptr_id)
    FROM armory_weapon
    JOIN armory_item
    ON armory_weapon.item_ptr_id = armory_item.item_id
    WHERE armory_weapon.item_ptr_id = armory_item.item_id'''

# - `NON_WEAPONS`: How many of the items are not weapons?
NON_WEAPONS_items = '''
    '''