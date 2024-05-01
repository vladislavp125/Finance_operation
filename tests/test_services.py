import unittest
from unittest.mock import patch, MagicMock
from services.account_management import create_account


class TestCreateAccount(unittest.TestCase):

    @patch('utils.file_handler.open', create=True)
    @patch('utils.file_handler.get_data')
    @patch('utils.file_handler.pull_data')
    def test_create_account_existing_currency(self, mock_pull_data, mock_get_data, mock_open):
        mock_get_data.return_value = [
            {"id": 1, "name": "Existing Account", "user": 123, "currency": "USD", "balance": 0}]
        user_id = 123
        name = "Test Account"
        currency = "USD"
        mock_file = MagicMock()
        mock_file.read.return_value = '[{"id": 1, "name": "Existing Account", "user": 123, "currency": "USD", "balance": 0}]'  # Указываем корректные JSON данные
        mock_open.return_value.__enter__.return_value = mock_file  # Настройка мокированного объекта файла

        account_id = create_account(user_id, name, currency)
        self.assertIsNone(account_id)
        mock_pull_data.assert_not_called()


if __name__ == '__main__':
    unittest.main()