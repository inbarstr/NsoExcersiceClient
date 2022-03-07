import json
from flask import json
from unittest import TestCase
import requests
from Asserts.Asserts import Asserts
from Configurations.WebConfiguations import WebConfigurations
from DataModels.Message import Message


class TestGetMessages(TestCase):

    def test_get_message_by_application_id(self):
        print("test_get_message_by_application_id starting")
        # Cleaning before test start
        delete = requests.delete(WebConfigurations.Url() + "DeleteMessage?applicationId=1")

        # Adding messages
        message1 = Message(1, "s1", "m1", ["avi aviv", "moshe cohen"], "Hi, how are you today?")
        message2 = Message(1, "s1", "m2", ["avi aviv", "moshe cohen"], "fine, and how are you today")
        message3 = Message(1, "s1", "m3", ["avi aviv", "moshe cohen"], "great")
        list_of_sent_messages = [message1, message2, message3]

        m1 = requests.post(WebConfigurations.Url() + "AddMessage", json=message1.to_dictionary())
        m2 = requests.post(WebConfigurations.Url() + "AddMessage", json=message2.to_dictionary())
        m3 = requests.post(WebConfigurations.Url() + "AddMessage", json=message3.to_dictionary())

        # GetMessages - the api to check
        get_response = requests.get(WebConfigurations.Url() + 'GetMessage?applicationId=1').text
        returned_messages = json.loads(get_response)

        # Assert
        self.assertEqual(3, len(returned_messages))
        # check every message
        asserts = Asserts()
        for returned_message in returned_messages:
            asserts.check_messages(returned_message, list_of_sent_messages)

        print("test_get_message_by_application_id ended")

    def test_get_message_by_session_id(self):
        print("test_get_message_by_session_id starting")
        # Cleaning before test start
        delete = requests.delete(WebConfigurations.Url() + "DeleteMessage?applicationId=2")
        delete = requests.delete(WebConfigurations.Url() + "DeleteMessage?applicationId=3")

        # Adding messages
        message1 = Message(2, "s2", "m4", ["avi aviv", "moshe cohen"], "Hi, how are you today?")
        message2 = Message(3, "s2", "m5", ["avi aviv", "moshe cohen"], "fine, and how are you today")
        message3 = Message(3, "s3", "m6", ["avi aviv", "moshe cohen"], "great")
        list_of_sent_messages = [message1, message2, message3]

        m4 = requests.post(WebConfigurations.Url() + "AddMessage", json=message1.to_dictionary())
        m5 = requests.post(WebConfigurations.Url() + "AddMessage", json=message2.to_dictionary())
        m6 = requests.post(WebConfigurations.Url() + "AddMessage", json=message3.to_dictionary())

        # GetMessages - the api to check
        get_response = requests.get(WebConfigurations.Url() + 'GetMessage?sessionId=s2').text
        returned_messages = json.loads(get_response)

        # Assert
        self.assertEqual(2, len(returned_messages))
        # check every message
        asserts = Asserts()
        for returned_message in returned_messages:
            asserts.check_messages(returned_message, list_of_sent_messages)

        print("test_get_message_by_session_id ended")

    def test_get_message_by_message_id(self):
        print("test_get_message_by_message_id starting")
        # Cleaning before test start
        delete = requests.delete(WebConfigurations.Url() + "DeleteMessage?applicationId=4")

        # Adding messages
        message1 = Message(4, "s4", "m7", ["avi aviv", "moshe cohen"], "Hi, how are you today?")
        message2 = Message(4, "s5", "m8", ["avi aviv", "moshe cohen"], "fine, and how are you today")
        list_of_sent_messages = [message1, message2]

        m4 = requests.post(WebConfigurations.Url() + "AddMessage", json=message1.to_dictionary())
        m5 = requests.post(WebConfigurations.Url() + "AddMessage", json=message2.to_dictionary())

        # GetMessages - the api to check
        get_response = requests.get(WebConfigurations.Url() + 'GetMessage?messageId=m7').text
        returned_messages = json.loads(get_response)

        # Assert
        self.assertEqual(1, len(returned_messages))
        # check every message
        asserts = Asserts()
        for returned_message in returned_messages:
            asserts.check_messages(returned_message, list_of_sent_messages)

        print("test_get_message_by_message_id ended")

    def test_get_message_by_application_id_does_not_exist(self):
        print("test_get_message_by_application_id_does_not_exist starting")
        # Cleaning before test start
        delete = requests.delete(WebConfigurations.Url() + "DeleteMessage?applicationId=1000")

        # GetMessages - the api to check
        get_response = requests.get(WebConfigurations.Url() + 'GetMessage?applicationId=1000')

        # Assert
        self.assertEqual(get_response.status_code, 404)
        self.assertIn('messages with application_id = 1000 do not exist', get_response.text)

        print("test_get_message_by_application_id_does_not_exist starting")

    def test_get_message_by_session_id_does_not_exist(self):
        print("test_get_message_by_session_id_does_not_exist starting")
        # Cleaning before test start
        delete = requests.delete(WebConfigurations.Url() + "DeleteMessage?applicationId=1000")

        # GetMessages - the api to check
        get_response = requests.get(WebConfigurations.Url() + 'GetMessage?sessionId=1000')

        # Assert
        self.assertEqual(get_response.status_code, 404)
        self.assertIn('messages with session_id = 1000 do not exist', get_response.text)

        print("test_get_message_by_session_id_does_not_exist starting")

    def test_get_message_by_message_id_does_not_exist(self):
        print("test_get_message_by_message_id_does_not_exist starting")
        # Cleaning before test start
        delete = requests.delete(WebConfigurations.Url() + "DeleteMessage?applicationId=1000")

        # GetMessages - the api to check
        get_response = requests.get(WebConfigurations.Url() + 'GetMessage?messageId=1000')

        # Assert
        self.assertEqual(get_response.status_code, 404)
        self.assertIn('message with message_id = 1000 does not exist', get_response.text)

        print("test_get_message_by_message_id_does_not_exist starting")

    def test_get_message_without_parameters(self):
        print("test_get_message_without_parameters starting")

        # GetMessages - the api to check
        get_response = requests.get(WebConfigurations.Url() + 'GetMessage?')

        # Assert
        self.assertEqual(get_response.status_code, 500)

        print("test_get_message_without_parameters ended")

    def test_get_message_with_too_many_parameters(self):
        print("test_get_message_with_too_many_parameters starting")

        # GetMessages - the api to check
        get_response = requests.get(WebConfigurations.Url() + 'GetMessage?applicationId=1000&sessionId=1000')

        # Assert
        self.assertEqual(get_response.status_code, 500)

        print("test_get_message_without_parameters ended")

    def test_get_message_with_spelling_mistake_parameters(self):
        print("test_get_message_with_spelling_mistake_parameters starting")

        # GetMessages - the api to check
        get_response = requests.get(WebConfigurations.Url() + 'GetMessage?msgId=1000')

        # Assert
        self.assertEqual(get_response.status_code, 500)

        print("test_get_message_with_spelling_mistake_parameters ended")