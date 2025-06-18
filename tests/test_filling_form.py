from QAguru_20_homework_9.resourses import RegistrationPage


def test_correct_filling():
    registration_page = RegistrationPage()
    # тестовые данные
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
    registration_page.register_user(first_name, last_name, email, gender, mobile, birthday,
                                          subject, hobby, picture_name, adress, state, city)

    # проверка
    registration_page.should_have_filled (first_name, last_name, email, gender, mobile, birthday,
                                          subject, hobby, picture_name, adress, state, city)

