from rest_framework import serializers
from rest_framework import viewsets
from django.db import connection
from ropendb.items.models import ItemDb
from ropendb.settings import RO_ARMOR_LOCATIONS


class CardSerializer(serializers.HyperlinkedModelSerializer):
    lootedFrom = serializers.SerializerMethodField()
    subtype = serializers.SerializerMethodField()

    class Meta:
        model = ItemDb

        fields = ['id', 'name_japanese', 'type', 'subtype', 'price_buy', 'price_sell', 'weight',
                  'script', 'lootedFrom', ]

    def get_subtype(self, obj):
            locs = []
            locs_value = obj.equip_locations
            for loc in RO_ARMOR_LOCATIONS:
                loc_value = RO_ARMOR_LOCATIONS[loc]
                if locs_value >= loc_value:
                    locs_value = locs_value - loc_value
                    locs.append(loc)
            return locs

    def get_lootedFrom(self, obj):
        # Select drop value for a given item id (obj.id)
        # OUTPUTS:
        #   data['dropRate']: Drop value percentage.
        #   data['iName']: English item's name. Switch or add kName to select korean name.

        query = "SELECT iName,\
            CASE \
                WHEN `Drop1id` = # THEN (`Drop1per`/100)\
                WHEN `Drop2id` = # THEN (`Drop2per`/100)\
                WHEN `Drop3id` = # THEN (`Drop3per`/100)\
                WHEN `Drop4id` = # THEN (`Drop4per`/100)\
                WHEN `Drop5id` = # THEN (`Drop5per`/100)\
                WHEN `Drop6id` = # THEN (`Drop6per`/100)\
                WHEN `Drop7id` = # THEN (`Drop7per`/100)\
            END AS 'dropRate'\
        FROM `mob_db` WHERE\
            `Drop1id` = # OR\
            `Drop2id` = # OR\
            `Drop3id` = # OR\
            `Drop4id` = # OR\
            `Drop5id` = # OR\
            `Drop6id` = # OR\
            `Drop7id` = #;".replace('#', str(obj.id))
        with connection.cursor() as cursor:
            cursor.execute(query)
            data = cursor.fetchall()
        return data

class CardViewSet(viewsets.ReadOnlyModelViewSet):

    serializer_class = CardSerializer

    def get_queryset(self):
        search_fields = ['slots', 'id', 'name_english']
        params = self.request.query_params
        queryset = ItemDb.objects.filter(type=6)

        for key in params:
            if key in search_fields and params[key] is not None:
                queryset = queryset.filter(**{key: params[key]})

        return queryset
