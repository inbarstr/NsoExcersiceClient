from unittest import TestCase
import requests
from Configurations.WebConfiguations import WebConfigurations
from DataModels.Message import Message


class TestDeleteMessages(TestCase):

    def test_delete_message_by_application_id(self):
        print("test_delete_message_by_application_id starting")
        # Cleaning before test start
        delete = requests.delete(WebConfigurations.Url() + "DeleteMessage?applicationId=6")

        # Adding messages
        message1 = Message(6, "s7", "m10", ["avi aviv", "moshe cohen"], "Hi, how are you today?")
        message2 = Message(6, "s7", "m11", ["avi aviv", "moshe cohen"], "fine, and how are you today")

        add_response1 = requests.post(WebConfigurations.Url() + "AddMessage", json=message1.to_dictionary())
        add_response2 = requests.post(WebConfigurations.Url() + "AddMessage", json=message2.to_dictionary())

        # DeleteMessages - the api to check
        delete_response = requests.delete(WebConfigurations.Url() + "DeleteMessage?applicationId=6")

        # Assert
        self.assertEqual(delete_response.status_code, 200)
        get_response = requests.get(WebConfigurations.Url() + 'GetMessage?applicationId=6').text
        self.assertIn('messages with application_id = 6 do not exist', get_response)

        print("test_delete_message_by_application_id ended")

    def test_delete_message_by_session_id(self):
        print("test_delete_message_by_session_id starting")
        # Cleaning before test start
        delete = requests.delete(WebConfigurations.Url() + "DeleteMessage?applicationId=7")

        # Adding messages
        message1 = Message(7, "s8", "m12", ["avi aviv", "moshe cohen"], "Hi, how are you today?")
        message2 = Message(7, "s8", "m13", ["avi aviv", "moshe cohen"], "fine, and how are you today")

        add_response1 = requests.post(WebConfigurations.Url() + "AddMessage", json=message1.to_dictionary())
        add_response2 = requests.post(WebConfigurations.Url() + "AddMessage", json=message2.to_dictionary())

        # DeleteMessages - the api to check
        delete_response = requests.delete(WebConfigurations.Url() + "DeleteMessage?sessionId=s8")

        # Assert
        self.assertEqual(delete_response.status_code, 200)
        get_response = requests.get(WebConfigurations.Url() + 'GetMessage?sessionId=s8').text
        self.assertIn('messages with session_id = s8 do not exist', get_response)

        print("test_delete_message_by_session_id ended")

    def test_delete_message_by_message_id(self):
        print("test_delete_message_by_message_id starting")
        # Cleaning before test start
        delete = requests.delete(WebConfigurations.Url() + "DeleteMessage?applicationId=8")

        # Adding messages
        message1 = Message(8, "s9", "m14", ["avi aviv", "moshe cohen"], "Hi, how are you today?")
        message2 = Message(8, "s9", "m15", ["avi aviv", "moshe cohen"], "fine, and how are you today")

        add_response1 = requests.post(WebConfigurations.Url() + "AddMessage", json=message1.to_dictionary())
        add_response2 = requests.post(WebConfigurations.Url() + "AddMessage", json=message2.to_dictionary())

        # DeleteMessages - the api to check
        delete_response1 = requests.delete(WebConfigurations.Url() + "DeleteMessage?messageId=m14")
        delete_response2 = requests.delete(WebConfigurations.Url() + "DeleteMessage?messageId=m15")

        # Assert
        self.assertEqual(delete_response1.status_code, 200)
        self.assertEqual(delete_response2.status_code, 200)
        get_response = requests.get(WebConfigurations.Url() + 'GetMessage?messageId=m14').text
        self.assertIn('message with message_id = m14 does not exist', get_response)
        get_response = requests.get(WebConfigurations.Url() + 'GetMessage?messageId=m15').text
        self.assertIn('message with message_id = m15 does not exist', get_response)

        print("test_delete_message_by_message_id ended")

    def test_delete_messages_by_application_id_application_id_do_not_exist_for_removal(self):
        print("test_delete_message_by_application_id_application_id_does_not_exist_for_removal starting")
        # Cleaning before test start
        delete = requests.delete(WebConfigurations.Url() + "DeleteMessage?applicationId=2000")

        # DeleteMessages - the api to check
        delete_response = requests.delete(WebConfigurations.Url() + "DeleteMessage?applicationId=2000")

        # Assert
        self.assertEqual(delete_response.status_code, 404)
        self.assertIn('messages with application_id = 2000 do not exist, for removal', delete_response.text)

        print("test_delete_message_by_application_id_application_id_does_not_exist_for_removal ended")

    def test_delete_messages_by_session_id_session_id_do_not_exist_for_removal(self):
        print("test_delete_message_by_session_id_session_id_does_not_exist_for_removal starting")
        # Cleaning before test start
        delete = requests.delete(WebConfigurations.Url() + "DeleteMessage?applicationId=2000")

        # DeleteMessages - the api to check
        delete_response = requests.delete(WebConfigurations.Url() + "DeleteMessage?sessionId=2000")

        # Assert
        self.assertEqual(delete_response.status_code, 404)
        self.assertIn('messages with session_id = 2000 do not exist, for removal', delete_response.text)

        print("test_delete_message_by_session_id_session_id_does_not_exist_for_removal ended")

    def test_delete_message_by_message_id_message_id_does_not_exist_for_removal(self):
        print("test_delete_message_by_message_id_message_id_does_not_exist_for_removal starting")
        # Cleaning before test start
        delete = requests.delete(WebConfigurations.Url() + "DeleteMessage?applicationId=2000")

        # DeleteMessages - the api to check
        delete_response = requests.delete(WebConfigurations.Url() + "DeleteMessage?messageId=2000")

        # Assert
        self.assertEqual(delete_response.status_code, 404)
        self.assertIn('message with message_id = 2000 does not exist, for removal', delete_response.text)

        print("test_delete_message_by_message_id_message_id_does_not_exist_for_removal ended")

    def test_delete_message_without_parameters(self):
        print("test_delete_message_without_parameters starting")

        # DeleteMessages - the api to check
        delete_response = requests.delete(WebConfigurations.Url() + 'DeleteMessage?')

        # Assert
        self.assertEqual(delete_response.status_code, 500)

        print("test_delete_message_without_parameters ended")

    def test_delete_message_with_too_many_parameters(self):
        print("test_delete_message_with_too_many_parameters starting")

        # DeleteMessages - the api to check
        get_response = requests.delete(WebConfigurations.Url() + 'DeleteMessage?sessionId=1000&messageId=1000')

        # Assert
        self.assertEqual(get_response.status_code, 500)

        print("test_delete_message_with_too_many_parameters ended")

    def test_delete_message_with_spelling_mistake_parameters(self):
        print("test_delete_message_with_spelling_mistake_parameters starting")

        # GetMessages - the api to check
        get_response = requests.delete(WebConfigurations.Url() + 'DeleteMessage?appId=1000')

        # Assert
        self.assertEqual(get_response.status_code, 500)

        print("test_delete_message_with_spelling_mistake_parameters ended")