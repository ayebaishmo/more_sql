# query_1 = 'SELECT * FROM charactercreator_character;'

# queries.py

TOTAL_CHARACTERS = """
SELECT COUNT(*) FROM charactercreator_character;
"""

TOTAL_SUBCLASS = """
SELECT COUNT(*) FROM charactercreator_necromancer;
"""

TOTAL_ITEMS = """
SELECT COUNT(*) FROM armory_item;
"""

WEAPONS = """
SELECT COUNT(*) FROM armory_item WHERE item_id IN 
    (SELECT item_ptr_id FROM armory_weapon);
"""

NON_WEAPONS = """
SELECT COUNT(*) FROM armory_item WHERE item_id NOT IN 
    (SELECT item_ptr_id FROM armory_weapon);
"""

CHARACTER_ITEMS = """
SELECT character_id, COUNT(item_id) AS num_items
FROM charactercreator_character_inventory
GROUP BY character_id
LIMIT 20;
"""

CHARACTER_WEAPONS = """
SELECT character_id, COUNT(item_id) AS num_weapons
FROM charactercreator_character_inventory
WHERE item_id IN 
    (SELECT item_ptr_id FROM armory_weapon)
GROUP BY character_id
LIMIT 20;
"""

AVG_CHARACTER_ITEMS = """
SELECT AVG(num_items) FROM (
    SELECT COUNT(item_id) AS num_items
    FROM charactercreator_character_inventory
    GROUP BY character_id
);
"""

AVG_CHARACTER_WEAPONS = """
SELECT AVG(num_weapons) FROM (
    SELECT COUNT(item_id) AS num_weapons
    FROM charactercreator_character_inventory
    WHERE item_id IN 
        (SELECT item_ptr_id FROM armory_weapon)
    GROUP BY character_id
);
"""
