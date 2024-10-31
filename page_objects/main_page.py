from playwright.sync_api import Page
from pytest_playwright.pytest_playwright import page

from data.url import Url
from page_objects.base_page import BasePage


class MainPage(BasePage):
    def __init__(self, page: Page):
         super().__init__(page)
         self.page = page
         self.top_icon_yandex = page.get_by_label("Яндекс", exact=True)
         self.search_bar = page.get_by_placeholder("Найдётся всё")
         self.button_find = page.get_by_role("button", name="Найти")
         self.button_services = page.get_by_label("Сервисы")
         self.label_market = page.get_by_label("Маркет", exact=True)
         self.button_enter = page.get_by_role("link", name="Войти")
         self.button_profile = page.get_by_label("Профиль, вход не выполнен")




    def navigate(self):
         self.page.goto(Url.YANDEX_URL, timeout=50000)




