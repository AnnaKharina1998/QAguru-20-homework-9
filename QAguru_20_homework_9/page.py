from selene import browser, command, have

from QAguru_20_homework_9.resourses import resource_path


class RegistrationPage:
    def open(self):
        browser.open("/automation-practice-form")
    def type_first_name(self, first_name):
        browser.element('#firstName').type(first_name)

    def type_last_name(self, last_name):
        browser.element('#lastName').type(last_name)

    def type_email(self, email):
        browser.element('#userEmail').type(email)

    def choose_gender(self, gender):
        browser.element(f"//label[contains(text(),'{gender}')]").click()

    def type_mobile(self, mobile):
        browser.element('#userNumber').type(mobile)

    def type_birthday(self, birthday):
        day, month_year = birthday.split(sep = ' ')
        month, year = month_year.split(sep = ',')
        browser.element("#dateOfBirthInput").click()
        browser.element(".react-datepicker__year-select").type(f"{year}").click()
        browser.element(".react-datepicker__month-select").type(f"{month}").click()
        browser.element(f".react-datepicker__day--0{day}").click()

    def input_subject(self, subject):
        browser.element('#subjectsInput').type(subject[:2]).press_enter()

    def choose_hobby(self, hobby):
        browser.element(f"//label[contains(text(),'{hobby}')]").click()

    def choose_picture(self, picture_name):
        browser.element('#uploadPicture').send_keys(resource_path(picture_name))

    def type_adress(self, adress):
        browser.element('#currentAddress').perform(command.js.scroll_into_view).type(adress)

    def choose_state(self, state):
        browser.element("//div[@id='stateCity-wrapper']/descendant::input[1]").type(state).press_enter()

    def choose_city(self, city):
        browser.element("//div[@id='stateCity-wrapper']/descendant::input[2]").type(city).press_enter()

    def submit(self):
        browser.element('#submit').perform(command.js.scroll_into_view).click()

    def should_have_filled(self, first_name, last_name, email, gender, mobile, birthday, subject, hobby, picture_name,
                           adress, state, city):
        browser.element('.table-responsive').all('td').even.should(
            have.exact_texts(f'{first_name} {last_name}', email, gender, mobile, birthday, subject,
                             hobby, picture_name, adress, f'{state} {city}'))
