


from playwright.sync_api import Page, expect, Locator


class BasePage:
    def __init__(self, page: Page):
        self.page = page

    def check_element_visibility(self, element: Locator):
        expect(element).to_be_visible(timeout=30000)

    def click_by_element(self, element: Locator):
        element.click(force=True)


    def check_current_url(self, url: str):
       expect(self.page).to_have_url(url)



