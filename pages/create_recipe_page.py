import allure
from selenium.webdriver.common.by import By

from locators.create_recipe_locators import CreateRecipeLocators as L
from pages.base_page import BasePage


class CreateRecipePage(BasePage):
    @allure.step("Открыть вкладку «Создать рецепт»")
    def open_create_tab(self):
        self.tap(L.CREATE_RECIPE_TAB)

    @allure.step("Ожидать загрузку формы создания рецепта")
    def wait_form(self):
        self.wait_for_visibility(L.FORM)

    @allure.step("Заполнить поле «Название рецепта»")
    def set_recipe_name(self, name: str):
        self.fill_field(L.RECIPE_NAME_INPUT, name)

    @allure.step("Добавить ингредиент из выпадающего списка")
    def add_ingredient(self, ingredient_name: str, weight: str | None = None):
        self.fill_field(L.INGREDIENT_INPUT, ingredient_name)
        self.wait_for_visibility(L.INGREDIENT_DROPDOWN)
        option_locator = (By.XPATH, L.INGREDIENT_OPTION_XPATH_TPL.format(name=ingredient_name))
        self.tap(option_locator)
        if weight is not None:
            self.fill_field(L.INGREDIENT_WEIGHT_INPUT, weight)

    @allure.step("Заполнить поле «Время приготовления»")
    def set_cook_time(self, minutes):
        self.fill_field(L.COOK_TIME_INPUT, minutes)

    @allure.step("Заполнить описание рецепта")
    def set_description(self, text):
        self.fill_field(L.DESCRIPTION_TEXTAREA, text)

    @allure.step("Загрузить изображение рецепта")
    def upload_image(self, file_path):
        self.get_element(L.FILE_UPLOAD_INPUT).send_keys(file_path)

    @allure.step("Нажать кнопку «Создать рецепт»")
    def submit(self):
        self.tap(L.CREATE_RECIPE_BTN)

    @allure.step("Получить заголовок созданного рецепта")
    def get_recipe_title(self):
        return self.extract_text(L.RECIPE_TITLE)

    @allure.step("Добавить ингредиентов")
    def add_ing_btn(self):
        return self.tap(L.ADD_INGREDIENT_BTN)

    @allure.step("Создать рецепт целиком")
    def create_recipe(self, name, ing_name, ing_weight, cook_time, description, image_path):
        self.open_create_tab()
        self.wait_form()
        self.set_recipe_name(name)
        self.add_ingredient(ing_name, ing_weight)
        self.add_ing_btn()
        self.set_cook_time(cook_time)
        self.set_description(description)
        self.upload_image(image_path)
        self.submit()
        self.wait_for_visibility(L.RECIPE_TITLE)
        return self.get_recipe_title()

    @allure.step("Отображение формы рецепта")
    def is_visible_title(self) -> bool:
        return self.is_visible(L.RECIPE_TITLE)

    @allure.step("Получить название рецепта")
    def get_recipe_title_equal(self):
        self.wait_for_visibility(L.RECIPE_NAME_ON_PAGE)
        return self.extract_text(L.RECIPE_NAME_ON_PAGE)
