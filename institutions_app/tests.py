from xml.dom import ValidationErr
from django.test import TestCase

from institutions_app.validators import validate_nif

# Create your tests here.
class NifPatternTestCase(TestCase):
    def setUp(self):
        super().setUp()
    
    def test_successfull_pattern(self):
        print("Corriendo pruebas")
        self.assertRaises(validate_nif(""), ValidationErr)
        
    def test_simple(self):
        self.assertFalse(True, True)
    
    
    
# class SubscribeModelTestCase(TestCase):

#     def test_error_if_duplicate_email_in_subscription(self):
#         Subscriptions.objects.create(full_name='user1', email='email1@test.com')
#         self.assertRaises(AttributeError, Subscriptions.objects.create, full_name='user2',
#                           email='email1@test.com')

#     def test_error_if_duplicate_email_in_users(self):
#         User.objects.create(email='email1@test.com')
#         self.assertRaises(SystemError, Subscriptions.objects.create, full_name='user2',
#                           email='email1@test.com')

#     def test_insert_ok_in_subscriptions(self):
#         User.objects.create(email='email1@test.com')
#         subscription = Subscriptions.objects.create(email='email2@test.com')
#         self.assertTrue(Subscriptions.objects.filter(email=subscription.email).exists())
