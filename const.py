ELASTICSEARCH_HOST = "elasticsearch"

POKEMON_INDEX_NAME = "pokemon"
# POKEMON_INDEX_MAPPING = {'mappings':
#                              {'properties':
#                                   {'level': {'type': 'long'},
#                                    'name': {'type': 'text',
#                                             'fields': {
#                                                 'keyword': {
#                                                     'type': 'keyword'}}},
#                                    'nickname': {'type': 'text',
#                                                 'fields': {
#                                                     'keyword': {'type': 'keyword'}}},
#                                    'pokadex_id': {'type': 'long'},
#                                    'skills': {'type': 'text',
#                                               'fields': {
#                                                   'keyword': {'type': 'keyword'}}},
#                                    'type': {'type': 'text',
#                                             'fields': {
#                                                 'keyword': {'type': 'keyword'}}}}}}

POKEMON_INDEX_MAPPING = {'mappings':
                             {'properties':
                                  {'level': {'type': 'long'},
                                   'name': {'type': 'text'},
                                   'nickname': {'type': 'text'},
                                   'pokadex_id': {'type': 'long'},
                                   'skills': {'type': 'text'},
                                   'type': {'type': 'text'}
                                   }
                              }
                         }
