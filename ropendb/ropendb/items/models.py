from django.db import models


class ItemDb(models.Model):
    id = models.PositiveIntegerField(primary_key=True)
    name_english = models.CharField(max_length=50)
    name_japanese = models.CharField(max_length=50)
    type = models.PositiveIntegerField()
    subtype = models.PositiveIntegerField(blank=True, null=True)
    price_buy = models.IntegerField(blank=True, null=True)
    price_sell = models.IntegerField(blank=True, null=True)
    weight = models.PositiveSmallIntegerField(blank=True, null=True)
    atk = models.PositiveSmallIntegerField(blank=True, null=True)
    matk = models.PositiveSmallIntegerField(blank=True, null=True)
    defence = models.PositiveSmallIntegerField(blank=True, null=True)
    range = models.PositiveIntegerField(blank=True, null=True)
    slots = models.PositiveIntegerField(blank=True, null=True)
    equip_jobs = models.PositiveBigIntegerField(blank=True, null=True)
    equip_upper = models.PositiveIntegerField(blank=True, null=True)
    equip_genders = models.PositiveIntegerField(blank=True, null=True)
    equip_locations = models.PositiveIntegerField(blank=True, null=True)
    weapon_level = models.PositiveIntegerField(blank=True, null=True)
    equip_level_min = models.PositiveSmallIntegerField(blank=True, null=True)
    equip_level_max = models.PositiveSmallIntegerField(blank=True, null=True)
    refineable = models.PositiveIntegerField(blank=True, null=True)
    disable_options = models.PositiveIntegerField(blank=True, null=True)
    view_sprite = models.PositiveSmallIntegerField(blank=True, null=True)
    buyingstore = models.PositiveIntegerField(blank=True, null=True)
    sprite = models.PositiveIntegerField(blank=True, null=True)
    script = models.TextField(blank=True, null=True)
    equip_script = models.TextField(blank=True, null=True)
    unequip_script = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'item_db'