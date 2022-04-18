from enum import Enum
from pydantic import BaseModel, ValidationError, validator, Field
from typing import List, Literal


class PokemonTypesENUM(str, Enum):
    ELECTRIC = 'ELECTRIC'
    GROUND = 'GROUND'
    FIRE = 'FIRE'
    WATER = 'WATER'
    WIND = 'WIND'
    PSYCHIC = 'PSYCHIC'
    GRASS = 'GRASS'

    class Config:
        use_enum_values = True


class PokemonModel(BaseModel):
    level: int = Field(
        description="Pokemon's level",
        title="Level",
        ge=1
    )
    name: str = Field(
        description="Pokemon's name",
        title="Name"
    )
    nickname: str = Field(
        description="Pokemon's nickname",
        title="Nickname"
    )
    pokadex_id: int = Field(
        description="Pokemon's ID",
        title="Pokemon Serial Number",
        ge=1
    )
    type: PokemonTypesENUM = Field(
        description="Pokemon's type",
        title="Type",
        exclusiveMaximum=1
    )
    skills: List[str] = Field(
        description="Pokemon's skills",
        title="Skills",
        unique_items=True,
        min_items=1
    )
