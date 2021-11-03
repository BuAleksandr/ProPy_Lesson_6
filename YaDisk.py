import requests
from pprint import pprint


class YaUploader:
    API_BASE_URL = "https://cloud-api.yandex.net:443"

    def __init__(self, token, folder_name):
        self.folder_name = folder_name
        self.OAuth = token
        self.APT_BASE_URL = 'https://cloud-api.yandex.net/'
        self.headers = {'Authorization': self.OAuth}
        self.params = {'path': self.folder_name}

    def create_folder(self):

        try:
            req1 = requests.put(self.APT_BASE_URL + 'v1/disk/resources/', params=self.params, headers=self.headers)
            if req1.status_code == 201:
                return f'Папка {self.folder_name} успешно создана'
            elif req1.status_code == 409:
                return 'Папка с таким именем уже существует'
            else:
                return 'Убедитесь в правильности токена Yandex. {error}'
        except Exception as error:
            return 'Убедитесь в правильности токена Yandex. {error}'


def main():
    user_token_ya_disk = input('Введите свой токен для Яндекс.Диска: ')
    name_folder = input('Введите название папки: ')
    uploader_user = YaUploader(user_token_ya_disk, name_folder)
    print(uploader_user.create_folder())


if __name__ == '__main__':
    main()
