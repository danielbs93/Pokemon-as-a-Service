from pydantic import ValidationError

from CRUD.exceptions import *


class PokemonExistsException(DocumentExistsException):
    """
    Exception raised since a Pokemon is already exists.

    Attributes:
        message -- explanation of the error.
        status_code -- for returning to the user.
    """

    def __init__(self, message="Pokemon is already exists. Provide Pokemon with a different nickname."):
        self.status_code = 400
        self.message = message
        super().__init__(self.message)


class PokemonInsertionError(IndexOperationError):
    """
    Exception raised by some indexing operation error.

    Attributes:
        message -- explanation of the error.
        status_code -- for returning to the user.
    """

    def __init__(self, message="Error occurred during Pokemon insertion operation."):
        self.status_code = 404
        self.message = message
        super().__init__(self.message)


class PokemonsNotFoundException(FoundNoneException):
    """
    Exception raised by founding no Pokemons that match prefix querying.

    Attributes:
        message -- explanation of the error.
        status_code -- for returning to the user.
    """

    def __init__(self, message="No Pokemons were found under provided prefix"):
        self.status_code = 200
        self.message = message
        super().__init__(self.message)


def handle_validation_error(error: ValidationError) -> str:
    """
    Handling ValidationError output of validation fields
    :param error: the error that occurred.
    :return: msg to the user.
    """
    error_dict = error.errors()[0]

    # Handling fields
    field_missing = error_dict.get('loc')
    msg = error_dict['msg'].split(", \"<class")[0]
    return f'Field: {field_missing}, {msg}'
