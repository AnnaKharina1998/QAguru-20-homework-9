import os

from selene import browser, command, have


def resource_path(picture_name):
    return os.path.abspath(picture_name)


class RegistrationPage:
    def register_user(self, first_name, last_name, email, gender, mobile, birthday, subject, hobby, picture_name,
                           adress, state, city):
        browser.open("/automation-practice-form")
        browser.element('#firstName').type(first_name)
        browser.element('#lastName').type(last_name)
        browser.element('#userEmail').type(email)
        browser.element(f"//label[contains(text(),'{gender}')]").click()
        browser.element('#userNumber').type(mobile)
        day, month_year = birthday.split(sep = ' ')
        month, year = month_year.split(sep = ',')
        browser.element("#dateOfBirthInput").click()
        browser.element(".react-datepicker__year-select").type(f"{year}").click()
        browser.element(".react-datepicker__month-select").type(f"{month}").click()
        browser.element(f".react-datepicker__day--0{day}").click()
        browser.element('#subjectsInput').type(subject[:2]).press_enter()
        browser.element(f"//label[contains(text(),'{hobby}')]").click()
        browser.element('#uploadPicture').send_keys(resource_path(picture_name))
        browser.element('#currentAddress').perform(command.js.scroll_into_view).type(adress)
        browser.element("//div[@id='stateCity-wrapper']/descendant::input[1]").type(state).press_enter()
        browser.element("//div[@id='stateCity-wrapper']/descendant::input[2]").type(city).press_enter()
        browser.element('#submit').perform(command.js.scroll_into_view).click()

    def should_have_filled(self, first_name, last_name, email, gender, mobile, birthday, subject, hobby, picture_name,
                           adress, state, city):
        browser.element('.table-responsive').all('td').even.should(
            have.exact_texts(f'{first_name} {last_name}', email, gender, mobile, birthday, subject,
                             hobby, picture_name, adress, f'{state} {city}'))
