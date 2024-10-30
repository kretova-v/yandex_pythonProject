from data.url import Url


def test_check_current_url_on_main_page(main_page):
    main_page.navigate()
    main_page.check_current_url(Url.YANDEX_URL)