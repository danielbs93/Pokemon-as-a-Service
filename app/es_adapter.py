from dotenv import load_dotenv

load_dotenv()

from const import POKEMON_INDEX_NAME
from CRUD.es_crud import ElasticSearchCRUD
from CRUD.Entities import PokemonModel
from varname import nameof
from app.pokemon_exceptions import *

es_instance = ElasticSearchCRUD()


def is_pokemon_exists(pokemon: PokemonModel):
    """
    Pokemon existence validator.
    :param pokemon: (BaseModel) with all pokemon properties.
    :return: Raise PokemonExistsException if found.
    """
    try:
        es_instance.doc_exists(index=POKEMON_INDEX_NAME, doc=pokemon, by_field=nameof(pokemon.pokadex_id))
    except DocumentExistsException:
        raise PokemonExistsException()


def insert_new_pokemon(pokemon: PokemonModel):
    """
    Inserting new pokemon object to ES.
    :param pokemon: (BaseModel) with all pokemon properties.
    :return: Raise PokemonInsertionError if an error occurred while trying to insert.
    """
    try:
        es_instance.index_doc(index=POKEMON_INDEX_NAME, doc=pokemon)
    except IndexOperationError:
        raise PokemonInsertionError()


def auto_complete(prefix: str):
    """
    Retrieves pokemons which one of their fields contain a word with the given prefix.
     -- Example: prefix=ch
                results will contains the next pokemons:
                    {name: charmander ...rest of fields...},
                    {name: mega charmander ...rest of fields...},
                    {nickname: cheetos ...rest of fields...}
    :param prefix: word's prefix.
    :return: Raise PokemonsNotFoundException if there are no results for the given prefix query.
    """
    try:
        return es_instance.auto_complete(index=POKEMON_INDEX_NAME, prefix=prefix)
    except FoundNoneException:
        raise PokemonsNotFoundException()

# all_fields = list(PokemonModel.__fields__.keys())
