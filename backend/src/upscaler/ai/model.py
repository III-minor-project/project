from functools import lru_cache


@lru_cache(maxsize=1)
def load_model():
    """
    Load your ai model here.
    Now we can use our model without global declaration.
    """