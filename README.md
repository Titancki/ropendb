# Idea & objective
This API is meant to be used with Ragnarok Servers, espesially Hercules (pre-renewal) RO based. We want to make non-invasive project so **only based on what the game provide**. No extra database or data file. We want to have an API easy to maintain. 

For more information on Hercules server see : https://wiki.herc.ws/wiki/

# Getting started
This is a Python/Django app with a MariaDB provided by the game server.
If you want to install local RO Server see: https://board.herc.ws/topic/16607-ragnarok-offline-newbie-pack-2022-make-your-ro-server-in-less-then-5-minutes/

You need to [set database and allowed host](https://github.com/Titancki/ropendb/blob/main/ropendb/ropendb/settings.py).
To start the project `python manage.py runserver`

 # Routes
 Only get method is allowed. 
 
## /weapons
Get all weapons. 
/weapons/[id] to get specific weapon.
### Search fields (might change)
- subtype
- slots
- name_english

## /armor
Get all armors. 
/armor/[id] to get specific armor.
### Search fields (might change)
- equip_location
- slots
- name_english
