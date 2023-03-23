from selene import be, have
from selene import browser, command
import os
from selenium.webdriver import Keys


def test_registration_form(config_browser):
    browser.open('https://demoqa.com/automation-practice-form')
    browser.execute_script('document.querySelector("#fixedban").remove()')
    browser.element('footer').execute_script('element.remove()')
    browser.element('#firstName').should(be.blank).type('Harry')
    browser.element('#lastName').should(be.blank).type('Potter')
    browser.element('#userEmail').should(be.blank).type('hp@gmail.com')
    browser.element('[for="gender-radio-1"]').should(be.visible).click()
    browser.element('#userNumber').should(be.blank).type('8005553555')
    browser.element('#dateOfBirthInput').click()
    browser.element('.react-datepicker__month-select').click()
    browser.element('.react-datepicker__month-select>option[value="6"]').click()
    browser.element('.react-datepicker__year-select').click()
    browser.element('[value="1980"]').click()
    browser.element('[aria-label="Choose Thursday, July 31st, 1980"]').click()
    browser.element('#subjectsInput').perform(command.js.scroll_into_view)
    browser.element('#subjectsInput').click()
    browser.element('#subjectsInput').send_keys('Arts')
    browser.element('#subjectsInput').press(Keys.TAB)
    browser.driver.execute_script('window.scrollBy(0, 100)')
    browser.element('[for="hobbies-checkbox-1"]').click()
    browser.element('[id="uploadPicture"]').send_keys((os.getcwd() + '/hp.jpg'))
    browser.element('#currentAddress').should(be.blank).type("Little Winging, Surrey, England, UK")
    browser.element('#react-select-3-input').should(be.blank).type('Raj').press_enter()
    browser.element('#react-select-4-input').should(be.blank).type('Jai').press_enter()
    browser.element('#submit').perform(command.js.click)

    # checking the correctness of the code

    browser.element('//tbody/tr[1]/td[2]').should(have.text('Harry Potter'))
    browser.element('//tbody/tr[2]/td[2]').should(have.text('hp@gmail.com'))
    browser.element('//tbody/tr[3]/td[2]').should(have.text('Male'))
    browser.element('//tbody/tr[4]/td[2]').should(have.text('8005553555'))
    browser.element('//tbody/tr[5]/td[2]').should(have.text('31 July,1980'))
    browser.element('//tbody/tr[6]/td[2]').should(have.text('Arts'))
    browser.element('//tbody/tr[7]/td[2]').should(have.text('Sports'))
    browser.element('//tbody/tr[8]/td[2]').should(have.text('hp.jpg'))
    browser.element('//tbody/tr[9]/td[2]').should(have.text('Little Winging, Surrey, England, UK'))
    browser.element('//tbody/tr[10]/td[2]').should(have.text('Rajasthan Jaipur'))
