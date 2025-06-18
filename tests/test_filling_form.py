from QAguru_20_homework_9.resourses import RegistrationPage


def test_correct_filling():
    registration_page = RegistrationPage()
    registration_page.open()
    #тестовые данные
    first_name = 'Vasya'
    last_name = 'Pupkin'
    email = 'some_email@mail.ru'
    gender = 'Male'
    mobile = '1234567890'
    birthday = '01 January,2000'
    subject = 'Chemistry'
    hobby = 'Music'
    picture_name = 'my_cat_better_than_my_face.jpg'
    adress = 'Some street, 9 house'
    state = 'NCR'
    city = 'Delhi'
    # заполнение данных
    registration_page.type_first_name(first_name)
    registration_page.type_last_name(last_name)
    registration_page.type_email(email)
    registration_page.type_gender(gender)
    registration_page.type_mobile(mobile)
    registration_page.type_birthday(birthday)
    registration_page.type_subject(subject)
    registration_page.type_hobby(hobby)
    registration_page.choose_picture(picture_name)
    registration_page.type_adress(adress)
    registration_page.type_state(state)
    registration_page.type_city(city)

    # подтвердить заполнение
    registration_page.submit()

    # проверка
    registration_page.should_have_filled (first_name, last_name, email, gender, mobile, birthday,
                                          subject, hobby, picture_name, adress, state, city)

