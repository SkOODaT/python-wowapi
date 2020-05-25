# wowapi.mixins.community

## CommunityMixin
```python
CommunityMixin(self, /, *args, **kwargs)
```
All Community API methods



### get_realm_leaderboard
```python
CommunityMixin.get_realm_leaderboard(self, region, realm, **filters)
```

Challenge Mode API - realm leaderboard

### get_region_leaderboard
```python
CommunityMixin.get_region_leaderboard(self, region, **filters)
```

Challenge Mode API - region leaderboard

### get_character_profile
```python
CommunityMixin.get_character_profile(self, region, realm, character_name, **filters)
```

Character Profile API - base info or specific comma separated fields as filters

```python
api = WowApi('client-id', 'client-secret')
api.get_character_profile('eu', 'khadgar', 'patchwerk')
api.get_character_profile('eu', 'khadgar', 'patchwerk', locale='en_GB', fields='guild,mounts')
```

### get_guild_profile
```python
CommunityMixin.get_guild_profile(self, region, realm, guild_name, **filters)
```

Guild Profile API - base info or specific comma separated fields as filters

```python
api = WowApi('client-id', 'client-secret')
api.get_guild_profile('eu', 'khadgar')
api.get_guild_profile('eu', 'khadgar', locale='en_GB', fields='achievements,challenge')
```

### get_item
```python
CommunityMixin.get_item(self, region, id, **filters)
```

Item API - detail item

### get_item_set
```python
CommunityMixin.get_item_set(self, region, id, **filters)
```

Item API - detail item set

### get_mounts
```python
CommunityMixin.get_mounts(self, region, **filters)
```

Mounts API - all supported mounts

### get_pets
```python
CommunityMixin.get_pets(self, region, **filters)
```

Pets API - all supported pets

### get_pet_ability
```python
CommunityMixin.get_pet_ability(self, region, id, **filters)
```

Pets API - pet ability details

### get_pet_species
```python
CommunityMixin.get_pet_species(self, region, id, **filters)
```

Pets API - pet species details

### get_pet_stats
```python
CommunityMixin.get_pet_stats(self, region, id, **filters)
```

Pets API - pet stats details

### get_leaderboards
```python
CommunityMixin.get_leaderboards(self, region, bracket, **filters)
```

Pvp API - pvp bracket leaderboard and rbg

### get_quest
```python
CommunityMixin.get_quest(self, region, id, **filters)
```

Quest API - metadata for quests

### get_realm_status
```python
CommunityMixin.get_realm_status(self, region, **filters)
```

Realm Status API - realm status for region

### get_recipe
```python
CommunityMixin.get_recipe(self, region, id, **filters)
```

Recipe API - recipe details

### get_spell
```python
CommunityMixin.get_spell(self, region, id, **filters)
```

Spell API - spell details

### get_characters
```python
CommunityMixin.get_characters(self, region, **filters)
```

User API - List of characters of account

```python
WowApi.get_characters('us')
```

### get_zones
```python
CommunityMixin.get_zones(self, region, **filters)
```

Zone API - master list

### get_zone
```python
CommunityMixin.get_zone(self, region, id, **filters)
```

Zone API - detail zone

### get_battlegroups
```python
CommunityMixin.get_battlegroups(self, region, **filters)
```

Data Resources API - all battlegroups

### get_character_races
```python
CommunityMixin.get_character_races(self, region, **filters)
```

Data Resources API - all character races

### get_character_classes
```python
CommunityMixin.get_character_classes(self, region, **filters)
```

Data Resources API - all character classes

### get_character_achievements
```python
CommunityMixin.get_character_achievements(self, region, **filters)
```

Data Resources API - all character achievements

### get_guild_rewards
```python
CommunityMixin.get_guild_rewards(self, region, **filters)
```

Data Resources API - all guild rewards

### get_guild_perks
```python
CommunityMixin.get_guild_perks(self, region, **filters)
```

Data Resources API - all guild perks

### get_guild_achievements
```python
CommunityMixin.get_guild_achievements(self, region, **filters)
```

Data Resources API - all guild achievements

### get_item_classes
```python
CommunityMixin.get_item_classes(self, region, **filters)
```

Data Resources API - all item classes

### get_talents
```python
CommunityMixin.get_talents(self, region, **filters)
```

Data Resources API - all talents, specs and glyphs for each class

### get_pet_types
```python
CommunityMixin.get_pet_types(self, region, **filters)
```

Data Resources API - all pet types
