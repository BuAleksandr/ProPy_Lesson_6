import unittest
import YaDisk
from YaDisk import YaUploader

user_token_ya_disk = input('Введите свой токен для Яндекс.Диска: ')
uploader_user = YaUploader(user_token_ya_disk, 'Test_folder')


class TestAPI(unittest.TestCase):
    def test_create_folder(self):
        self.assertEqual(uploader_user.create_folder(), "Папка Test_folder успешно создана")

    def test_create_folder_exist(self):
        self.assertEqual(uploader_user.create_folder(), "Папка с таким именем уже существует")


if __name__ == '__main__':
    unittest.main()
