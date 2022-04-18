# from elasticsearch import Elasticsearch
from dotenv import load_dotenv
load_dotenv()

from CRUD.es_crud import ElasticSearchCRUD
from const import POKEMON_INDEX_NAME, POKEMON_INDEX_MAPPING

INDEX_TO_MAPPING = {POKEMON_INDEX_NAME: POKEMON_INDEX_MAPPING}


def get_es_cli():
    return ElasticSearchCRUD().es_instance


def delete_index_if_exists(index_name):
    es_cli = get_es_cli()
    if es_cli.indices.exists(index_name):
        es_cli.indices.delete(index_name)


def create_index(index_name):
    es_cli = get_es_cli()
    return es_cli.indices.create(index_name, INDEX_TO_MAPPING[index_name])

if __name__ == '__main__':
    create_index(POKEMON_INDEX_NAME)
    # delete_index_if_exists(POKEMON_INDEX_NAME)