from selene import browser, have, be, command
import os


class RegistrationPage:
    def open(self):
        browser.open('/')
        browser.execute_script('document.querySelector(".body-height").style.transform = "scale(.6)"')
        # browser.all('[id^google_ads][id$=container__]').with_(timeout=10).wait_until(have.size_less_than_or_equal(3))
        # browser.all('[id^=google_ads][id$=container__]').perform(command.js.remove)

    def type_first_name(self, value):
        browser.element('#firstName').type(value)

    def type_last_name(self, value):
        browser.element('#lastName').type(value)

    def type_email(self, value):
        browser.element('#userEmail').type(value)

    def click_gender(self, value):
        # browser.element('[for="gender-radio-1"]').click()
        browser.all('[name=gender]').element_by(have.value(value)).element('..').click()

    def type_number(self, value):
        browser.element('#userNumber').type(value)
        pass

    def type_date_of_birth(self, year, month, day):
        browser.element('#dateOfBirthInput').click()
        browser.element('.react-datepicker__year-select').type(year)
        browser.element('.react-datepicker__month-select').type(month)
        browser.element(f'.react-datepicker__day--0{day}').click()

    def type_subjects(self, value):
        browser.element('#subjectsInput').type(value).press_enter()

    def click_hobbies(self, value):
        # browser.element('[for="hobbies-checkbox-1"]').click()
        browser.all('.custom-checkbox').element_by(have.exact_text(value)).click()

    def download_picture(self, file):
        browser.element("#uploadPicture").send_keys(os.path.abspath(file))

    def type_address(self, value):
        browser.element('#currentAddress').type(value)

    def type_state(self, value):
        browser.element('#react-select-3-input').type(value).press_enter()

    def type_city(self, value):
        browser.element('#react-select-4-input').type(value).press_enter()

    def click_submit(self, value):
        browser.element(value).click()

    def registered_user_data_should(self, full_name, email, gender, number, date, subject, hobbi, file, address,
                                    state_city):
        browser.element('.table').all('td').even.should(
            have.exact_texts(
                full_name, email, gender, number, date, subject, hobbi, file, address, state_city,
            )
        )