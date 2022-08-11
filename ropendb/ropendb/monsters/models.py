from django.db import models

class MobDb(models.Model):
    id = models.PositiveIntegerField(db_column='ID', primary_key=True)  # Field name made lowercase.
    sprite = models.TextField(db_column='Sprite')  # Field name made lowercase.
    kname = models.TextField(db_column='kName')  # Field name made lowercase.
    iname = models.TextField(db_column='iName')  # Field name made lowercase.
    lv = models.PositiveIntegerField(db_column='LV')  # Field name made lowercase.
    hp = models.PositiveIntegerField(db_column='HP')  # Field name made lowercase.
    sp = models.PositiveIntegerField(db_column='SP')  # Field name made lowercase.
    exp = models.PositiveIntegerField(db_column='EXP')  # Field name made lowercase.
    jexp = models.PositiveIntegerField(db_column='JEXP')  # Field name made lowercase.
    range1 = models.PositiveIntegerField(db_column='Range1')  # Field name made lowercase.
    atk1 = models.PositiveSmallIntegerField(db_column='ATK1')  # Field name made lowercase.
    atk2 = models.PositiveSmallIntegerField(db_column='ATK2')  # Field name made lowercase.
    def_field = models.PositiveSmallIntegerField(db_column='DEF')  # Field name made lowercase. Field renamed because it was a Python reserved word.
    mdef = models.PositiveSmallIntegerField(db_column='MDEF')  # Field name made lowercase.
    str = models.PositiveSmallIntegerField(db_column='STR')  # Field name made lowercase.
    agi = models.PositiveSmallIntegerField(db_column='AGI')  # Field name made lowercase.
    vit = models.PositiveSmallIntegerField(db_column='VIT')  # Field name made lowercase.
    int = models.PositiveSmallIntegerField(db_column='INT')  # Field name made lowercase.
    dex = models.PositiveSmallIntegerField(db_column='DEX')  # Field name made lowercase.
    luk = models.PositiveSmallIntegerField(db_column='LUK')  # Field name made lowercase.
    range2 = models.PositiveIntegerField(db_column='Range2')  # Field name made lowercase.
    range3 = models.PositiveIntegerField(db_column='Range3')  # Field name made lowercase.
    scale = models.PositiveIntegerField(db_column='Scale')  # Field name made lowercase.
    race = models.PositiveIntegerField(db_column='Race')  # Field name made lowercase.
    element = models.PositiveIntegerField(db_column='Element')  # Field name made lowercase.
    mode = models.PositiveIntegerField(db_column='Mode')  # Field name made lowercase.
    speed = models.PositiveSmallIntegerField(db_column='Speed')  # Field name made lowercase.
    adelay = models.PositiveSmallIntegerField(db_column='aDelay')  # Field name made lowercase.
    amotion = models.PositiveSmallIntegerField(db_column='aMotion')  # Field name made lowercase.
    dmotion = models.PositiveSmallIntegerField(db_column='dMotion')  # Field name made lowercase.
    mexp = models.PositiveIntegerField(db_column='MEXP')  # Field name made lowercase.
    mvp1id = models.PositiveSmallIntegerField(db_column='MVP1id')  # Field name made lowercase.
    mvp1per = models.PositiveSmallIntegerField(db_column='MVP1per')  # Field name made lowercase.
    mvp2id = models.PositiveSmallIntegerField(db_column='MVP2id')  # Field name made lowercase.
    mvp2per = models.PositiveSmallIntegerField(db_column='MVP2per')  # Field name made lowercase.
    mvp3id = models.PositiveSmallIntegerField(db_column='MVP3id')  # Field name made lowercase.
    mvp3per = models.PositiveSmallIntegerField(db_column='MVP3per')  # Field name made lowercase.
    drop1id = models.PositiveSmallIntegerField(db_column='Drop1id')  # Field name made lowercase.
    drop1per = models.PositiveSmallIntegerField(db_column='Drop1per')  # Field name made lowercase.
    drop2id = models.PositiveSmallIntegerField(db_column='Drop2id')  # Field name made lowercase.
    drop2per = models.PositiveSmallIntegerField(db_column='Drop2per')  # Field name made lowercase.
    drop3id = models.PositiveSmallIntegerField(db_column='Drop3id')  # Field name made lowercase.
    drop3per = models.PositiveSmallIntegerField(db_column='Drop3per')  # Field name made lowercase.
    drop4id = models.PositiveSmallIntegerField(db_column='Drop4id')  # Field name made lowercase.
    drop4per = models.PositiveSmallIntegerField(db_column='Drop4per')  # Field name made lowercase.
    drop5id = models.PositiveSmallIntegerField(db_column='Drop5id')  # Field name made lowercase.
    drop5per = models.PositiveSmallIntegerField(db_column='Drop5per')  # Field name made lowercase.
    drop6id = models.PositiveSmallIntegerField(db_column='Drop6id')  # Field name made lowercase.
    drop6per = models.PositiveSmallIntegerField(db_column='Drop6per')  # Field name made lowercase.
    drop7id = models.PositiveSmallIntegerField(db_column='Drop7id')  # Field name made lowercase.
    drop7per = models.PositiveSmallIntegerField(db_column='Drop7per')  # Field name made lowercase.
    drop8id = models.PositiveSmallIntegerField(db_column='Drop8id')  # Field name made lowercase.
    drop8per = models.PositiveSmallIntegerField(db_column='Drop8per')  # Field name made lowercase.
    drop9id = models.PositiveSmallIntegerField(db_column='Drop9id')  # Field name made lowercase.
    drop9per = models.PositiveSmallIntegerField(db_column='Drop9per')  # Field name made lowercase.
    dropcardid = models.PositiveSmallIntegerField(db_column='DropCardid')  # Field name made lowercase.
    dropcardper = models.PositiveSmallIntegerField(db_column='DropCardper')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'mob_db'
