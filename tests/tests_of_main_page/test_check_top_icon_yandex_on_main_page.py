def test_check_top_icon_yandex_on_main_page(main_page):
    main_page.navigate()
    main_page.check_element_visibility(element=main_page.top_icon_yandex)
    main_page.top_icon_yandex.click()

