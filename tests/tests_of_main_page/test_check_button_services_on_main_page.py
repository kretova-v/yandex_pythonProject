def test_check_button_services_on_main_page(main_page):
    main_page.navigate()
    main_page.check_element_visibility(element=main_page.button_services)
    main_page.button_services.click()
    main_page.check_element_visibility(element=main_page.label_market)
    main_page.label_market.click()
