from selenium.webdriver.common.by import By


class CreateRecipeLocators:
    CREATE_RECIPE_TAB = (By.XPATH, "//*[self::a or self::button][normalize-space()='Создать рецепт']")
    FORM = (By.XPATH, "//form[contains(@class, 'styles_form')]")
    RECIPE_NAME_INPUT = (By.XPATH, "//*[normalize-space()='Название рецепта']/following::input[1]")
    INGREDIENT_INPUT = (By.XPATH, "//*[normalize-space()='Ингредиенты']/following::input[1]")
    INGREDIENT_WEIGHT_INPUT = (By.XPATH, "//input[contains(@class, 'ingredientsAmountValue')]")
    COOK_TIME_INPUT = (By.XPATH, "//*[contains(normalize-space(),'Время приготовления')]/following::input[1]")
    DESCRIPTION_TEXTAREA = (By.XPATH, "//*[normalize-space()='Описание рецепта']/following::textarea[1]")
    FILE_UPLOAD_INPUT = (By.CSS_SELECTOR, "input[type='file']")
    INGREDIENT_DROPDOWN = (By.CSS_SELECTOR, "div.styles_container__3ukwm, div.styles_container")
    INGREDIENT_OPTION_XPATH_TPL = "//div[contains(@class, 'styles_container')]/div[normalize-space()='{name}']"
    ADD_INGREDIENT_BTN = (By.XPATH, "//*[normalize-space()='Добавить ингредиент']")
    CREATE_RECIPE_BTN = (By.XPATH, ".//button[text()='Создать рецепт']")
    RECIPE_TITLE = (By.XPATH, "//*[contains(@class,'styles_single-card__info__2_cny')]")
    RECIPE_NAME_ON_PAGE = (By.CSS_SELECTOR, "h1.styles_single-card__title__2QMPq")
