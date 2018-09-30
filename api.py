import requests


class ServerResponse:
    def __init__(self, response: requests.Response):
        self.status = bool(response)
        self.status_code = response.status_code
        self.text = response.text
        # self.json = response.json()


class UserApi:
    def __init__(self, base_url: str, bot_type: str):
        """
        :param url:
        :param bot_type: tg / vk / alice
        """
        self.base_url = base_url
        self.bot_type = bot_type


    # Только для Тг, юзер получает на сайте токен и отправляет
    def user_tg_login(self, token: str) -> ServerResponse:
        pass

    def user_profile(self, user_id: str) -> ServerResponse:
        pass

    # ready
    def problem_new(self, title: str, description: str, tag: str, address: str = '') -> ServerResponse:
        url = self.base_url + '/api/problems/new'
        resp = requests.get(url, params={'title':       title,
                                         'description': description,
                                         'tag':         tag,
                                         'address':     address
                                         })

        print(resp.status_code)
        print(resp.text)
        return ServerResponse(resp)


    def problem_nearest(self, address: str) -> ServerResponse:
        pass


    def problem_add_comment(self, user_id: str, com_type: str, comment: str) -> ServerResponse:
        pass


    def problem_edit(self, user_id: str, prob_type: str, value: str) -> ServerResponse:
        pass


    def problem_check(self, user_id: str, value: str) -> ServerResponse:
        pass


    def problem_stats(self, address: str) -> ServerResponse:
        pass