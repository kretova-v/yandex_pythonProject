def test_check_search_bar_on_main_page(main_page):
    main_page.navigate()
    main_page.check_element_visibility(element=main_page.search_bar)
    main_page.search_bar.click()
    main_page.search_bar.fill("Найдётся всё")
    main_page.check_element_visibility(element=main_page.button_find)
    main_page.button_find.click()



