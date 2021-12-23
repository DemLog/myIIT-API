import requests
from bs4 import BeautifulSoup


class MoodleAuth:
    def __init__(self, email, password):
        self.email = email
        self.password = password
        self.session = requests.Session()

    @staticmethod
    def get_logintoken(session):
        response = session.get('https://eu.iit.csu.ru/login/index.php/')
        soup = BeautifulSoup(response.text, 'lxml')
        return soup.find('input', {'name': 'logintoken'}).get('value')

    @staticmethod
    def get_user(session, username, password, logintoken, ancho=""):
        data_auth = {
            "ancho": ancho,
            "logintoken": logintoken,
            "username": username,
            "password": password
        }
        response = session.post('https://eu.iit.csu.ru/login/index.php/', data=data_auth)
        return response

    @staticmethod
    def get_user_data(user_session):
        params = dict(
            first_name=None,
            last_name=None,
            patronymic='Отчество',
            email='Адрес электронной почты',
            country='Страна',
            city='Город',
            status='Статус',
            study_group='Учебная группа',
            direction='Направление обучения',
            profile='Профиль',
            form_study='Форма обучения'
        )

        user = user_session.get('https://eu.iit.csu.ru/user/profile.php')
        user_data = BeautifulSoup(user.text, 'lxml')

        # Взятие имени и фамилии
        full_name = user_data.find('div', {'class': 'page-header-headings'}).find('h1').contents
        params['last_name'], params['first_name'] = full_name[0].split(' ')

        detailed_info = user_data.find('div', {'class': 'profile_tree'}).find('section').find('ul').find_all('dd')
        detailed_info_header = user_data.find('div', {'class': 'profile_tree'}).find('section').find('ul').find_all('dt')
        for key, value in params.items():
            for x in range(0, len(detailed_info_header)):
                if detailed_info_header[x].contents[0] == value:
                    if key == 'email':  # Условие для отлова email
                        params[key] = detailed_info[x].find('a').contents[0]
                        continue
                    params[key] = detailed_info[x].contents[0]

        return params

    @staticmethod
    def logout_user(user_session):
        response = user_session.get('https://eu.iit.csu.ru/login/index.php/')
        user_data = BeautifulSoup(response.text, 'lxml')
        logout_url = user_data.find('a', {'data-title': 'logout,moodle'}).get('href')

        return user_session.get(logout_url)

    def check_account(self):
        logintoken = self.get_logintoken(self.session)
        user = self.get_user(self.session, self.email, self.password, logintoken)

        context_auth = BeautifulSoup(user.text, 'lxml')
        error_message = context_auth.find('a', {'id': 'loginerrormessage'})
        if error_message is not None:
            return {'error_message': error_message.contents[0]}

        profile = self.get_user_data(self.session)

        self.logout_user(self.session)

        return profile
