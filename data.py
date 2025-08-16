from dataclasses import dataclass

from helpers import (
    get_fake_email, get_fake_password, get_fake_username,
    get_fake_first_name, get_fake_last_name
)
from pathlib import Path


@dataclass
class UserPayload:
    first_name: str
    last_name: str
    username: str
    email: str
    password: str


def make_user() -> UserPayload:
    return UserPayload(
        first_name=get_fake_first_name(),
        last_name=get_fake_last_name(),
        username=get_fake_username(),
        email=get_fake_email(),
        password=get_fake_password(),
    )


@dataclass(frozen=True)
class RecipePayload:
    title: str
    ingredient_name: str
    ingredient_weight: str
    cook_time: str
    description: str
    image_path: str


def make_recipe() -> RecipePayload:
    assets_dir = Path(__file__).resolve().parent / "tests" / "assets"
    image = assets_dir / "Good_Food.jpg"
    return RecipePayload(
        title="Рецепт «Оливье по-домашнему»",
        ingredient_name="картофель молодой",
        ingredient_weight="150",
        cook_time="30",
        description="Праздничный салат по ГОСТу.",
        image_path=str(image),
    )
