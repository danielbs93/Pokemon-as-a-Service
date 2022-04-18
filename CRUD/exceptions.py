class DocumentExistsException(Exception):
    """
    Exception raised since the given document already exists .

    Attributes:
        message -- explanation of the error.
    """

    def __init__(self, message="Document is already exists."):
        self.message = message
        super().__init__(self.message)


class IndexOperationError(Exception):
    """
    Exception raised by some indexing operation error.

    Attributes:
        message -- explanation of the error.
    """

    def __init__(self, message="Error occurred during indexing operation."):
        self.message = message
        super().__init__(self.message)


class FoundNoneException(Exception):
    """
    Exception raised by founding no results from querying.

    Attributes:
        message -- explanation of the error.
    """

    def __init__(self, message="No results were found under the provided query"):
        self.message = message
        super().__init__(self.message)
