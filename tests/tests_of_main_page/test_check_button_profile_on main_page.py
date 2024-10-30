def test_check_button_profile_on_main_page(main_page):
    main_page.navigate()
    main_page.check_element_visibility(element=main_page.button_profile)
    main_page.button_profile.click()
    main_page.check_element_visibility(element=main_page.button_mail)
    main_page.button_mail.click()
