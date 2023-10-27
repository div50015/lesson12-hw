import time
from selene import browser, have
import os
import allure
from lesson12_hw.pages.registration_page import RegistrationPage
from pathlib import Path


def test_complete_todo():
    with allure.step('Open registrations form'):
        registration_page = RegistrationPage()
        registration_page.open()

    # WHEN
    with allure.step('Fill form'):
        registration_page.type_first_name('Ivan')
        registration_page.type_last_name('Petrov')
        registration_page.type_email('petrov@mail.ru')
        registration_page.click_gender('Male')
        registration_page.type_number('79287777777')
        registration_page.type_date_of_birth('1999', 'August', '09')
        registration_page.type_subjects('Biology')
        registration_page.click_hobbies('Sports')
        registration_page.download_picture(
            Path(__file__).parent.parent.joinpath(f'tests/files/ball.jpg'))
        # print(Path(__file__).parent.parent.joinpath(f'tests/files/ball.jpg'))
        registration_page.type_address('Russia Moscow')
        registration_page.type_state('NCR')
        registration_page.type_city('Noida')
        registration_page.click_submit('#submit')
        # time.sleep(10)

    # THEN
    with allure.step("Check form results"):
        registration_page.registered_user_data_should(
            'Ivan Petrov',
            'petrov@mail.ru',
            'Male',
            '7928777777',
            '09 August,1999',
            'Biology',
            'Sports',
            'ball.jpg',
            'Russia Moscow',
            'NCR Noida',
        )
