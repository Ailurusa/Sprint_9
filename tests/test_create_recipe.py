import allure

from data import make_recipe
from pages.create_recipe_page import CreateRecipePage
from pages.login_page import LoginPage
from pages.registration_page import RegistrationPage


class TestCreateRecipe:
    @allure.title("Карточка созданного рецепта появляется, название совпадает с введённым")
    def test_create_recipe_card_and_title(self, driver, user_payload):
        reg = RegistrationPage(driver)
        reg.register(
            user_payload.first_name,
            user_payload.last_name,
            user_payload.username,
            user_payload.email,
            user_payload.password
        )
        login = LoginPage(driver)
        login.sign_in(user_payload.email, user_payload.password)
        recipe = make_recipe()
        page = CreateRecipePage(driver)
        page.create_recipe(
            recipe.title,
            recipe.ingredient_name,
            recipe.ingredient_weight,
            recipe.cook_time,
            recipe.description,
            recipe.image_path,
        )
        assert page.is_visible_title() and page.get_recipe_title_equal() == recipe.title
