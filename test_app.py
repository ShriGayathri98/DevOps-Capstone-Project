import unittest
import app

class TestCustomerAccounts(unittest.TestCase):

    def setUp(self):
        self.app = app.app.test_client()
        self.app.testing = True
    
    def test_create_account(self):
        response = self.app.post('/accounts', json={'id': '1', 'name': 'John Doe'})
        self.assertEqual(response.status_code, 201)
        self.assertIn('John Doe', response.get_data(as_text=True))

    def test_get_account(self):
        self.app.post('/accounts', json={'id': '1', 'name': 'John Doe'})
        response = self.app.get('/accounts/1')
        self.assertEqual(response.status_code, 200)
        self.assertIn('John Doe', response.get_data(as_text=True))

    def test_update_account(self):
        self.app.post('/accounts', json={'id': '1', 'name': 'John Doe'})
        response = self.app.put('/accounts/1', json={'id': '1', 'name': 'Jane Doe'})
        self.assertEqual(response.status_code, 200)
        self.assertIn('Jane Doe', response.get_data(as_text=True))

    def test_delete_account(self):
        self.app.post('/accounts', json={'id': '1', 'name': 'John Doe'})
        response = self.app.delete('/accounts/1')
        self.assertEqual(response.status_code, 204)

    def test_list_accounts(self):
        self.app.post('/accounts', json={'id': '1', 'name': 'John Doe'})
        response = self.app.get('/accounts')
        self.assertEqual(response.status_code, 200)
        self.assertIn('John Doe', response.get_data(as_text=True))

if __name__ == '__main__':
    unittest.main()
