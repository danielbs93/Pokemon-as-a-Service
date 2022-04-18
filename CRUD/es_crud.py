from elasticsearch import Elasticsearch
from configurations.configES import EScredentials
from CRUD.exceptions import *
from pydantic import BaseModel


class ElasticSearchCRUD:

    def __init__(self):
        config = EScredentials()
        self.es_instance = Elasticsearch(
            http_auth=(config.USER_NAME, config.PASSWORD),
            cloud_id=config.CLOUD_ID
        )

    def doc_exists(self, index: str, doc: BaseModel, by_field: str):
        """
        Checks weather a document exists in the given index.
        By using 'match_phrase' filter, we are searching the exact full-text object in our index.
        :param index: The index we are querying of.
        :param doc: The BaseModel document we are searching.
        :param by_field: By what field to perform the matching.
        :return: Raise DocumentExistsException if we found a match.
        """
        resp = self.es_instance.search(index=index, body={"query": {"match_phrase": {by_field: doc.dict()[by_field]}}})
        hits = resp['hits']['total']['value']
        if hits > 0:
            raise DocumentExistsException()

    def index_doc(self, index: str, doc: BaseModel):
        """
        Inserting new document to ES instance.
        :param index: The index we are querying of.
        :param doc: The BaseModel document we are indexing.
        :return: Raise IndexOperationError exception - something went wrong with the insertion.
        """
        resp = self.es_instance.index(index=index, body=doc.dict())
        if resp['result'] != 'created':
            raise IndexOperationError()

    def auto_complete(self, index: str, prefix: str, fields=None) -> list or FoundNoneException:
        """
        Retrieves documents under the condition of including the given prefix.
        :param index: The index we are querying of.
        :param prefix: word's prefix.
        :param fields: Which fields to perform the prefix filtering.
        :return: A list of records that contain the prefix in one of their properties. Raise FoundNoneException otherwise.
        """

        if fields is None:
            fields = ["_all"]
        query = {
            "query": {
                "query_string": {
                    "query": f'{prefix}* | {prefix}((\w+)?)'
                }
            }
        }

        resp = self.es_instance.search(index=index, body=query)
        hits = resp['hits']['total']['value']

        if hits == 0:
            raise FoundNoneException()

        return [record['_source'] for record in resp['hits']['hits']]


# f'((?i)({prefix})(\w+)?)'