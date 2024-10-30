def test_check_button_enter_on_main_page(main_page):
    main_page.navigate()
    main_page.check_element_visibility(element=main_page.button_enter)
    main_page.button_enter.click()