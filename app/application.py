from flask import Flask, request, jsonify
from flask_caching import Cache
from pydantic import ValidationError
from app.elasticsearch_utils import get_es_cli
from configurations.EndPointsConfigurations import NEW_POKEMON_URL, AUTOCOMPLETE_URL
from app.es_adapter import *
from configurations.configFlaskCache import CacheCredentials

app = Flask(__name__)
config = CacheCredentials()

app.config.from_mapping(config.dict())
cache = Cache(app)

@app.route('/')
def health():
    es_cli = get_es_cli()

    return 'My Pokemon Service is UP!'


@app.route(NEW_POKEMON_URL, methods=['POST'])
def create_new_pokemon():
    pokemon_dict = request.json

    try:
        # Pokemon Model creation and fields validation
        pokemon_model = PokemonModel(**pokemon_dict)

        # Validating that the pokemon is new and not existing in our records.
        is_pokemon_exists(pokemon_model)

        # Inserting new pokemon
        insert_new_pokemon(pokemon_model)

        return "New Pokemon has been created", 200

    except ValidationError as e:
        return handle_validation_error(e), 400
    except PokemonExistsException as e:
        return e.message, e.status_code
    except PokemonInsertionError as e:
        return e.message, e.status_code


@app.route(AUTOCOMPLETE_URL, methods=['GET'])
@cache.cached()
def autocomplete(prefix):
    try:
        respond = auto_complete(prefix)
        return jsonify(respond)
    except PokemonsNotFoundException as e:
        return e.message, e.status_code


if __name__ == '__main__':
    app.run(debug=True)
