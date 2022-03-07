import json
from flask import json
from unittest import TestCase
import requests

from Asserts.Asserts import Asserts
from Configurations.WebConfiguations import WebConfigurations
from DataModels.Message import Message, MessageEncoder


class TestAddMessage(TestCase):

    def test_add_message(self):
        print("test_add_message starting")

        # Cleaning before test start
        delete = requests.delete(WebConfigurations.Url() + "DeleteMessage?applicationId=5")

        # Adding messages
        message1 = Message(5, "s6", "m9", ["avi aviv", "moshe cohen"], "Hi, how are you today?")
        list_of_sent_messages = [message1]

        # AddMessage - the api to check
        add_response = requests.post(WebConfigurations.Url() + "AddMessage", json=message1.to_dictionary())

        # Assert
        get_response = requests.get(WebConfigurations.Url() + 'GetMessage?messageId=m9').text
        returned_messages = json.loads(get_response)

        self.assertEqual(1, len(returned_messages))
        # check every message
        asserts = Asserts()
        for returned_message in returned_messages:
            asserts.check_messages(returned_message, list_of_sent_messages)

        print("test_add_message ended")

    def test_add_message_message_already_exist(self):
        print("test_add_message_message_already_exist starting")

        # Cleaning before test start
        delete = requests.delete(WebConfigurations.Url() + "DeleteMessage?applicationId=5")

        # Adding messages
        message1 = Message(10, "s100", "m1000", ["avi aviv", "moshe cohen"], "Hi, how are you today?")
        add_response = requests.post(WebConfigurations.Url() + "AddMessage", json=message1.to_dictionary())

        # AddMessage - the api to check
        add_response = requests.post(WebConfigurations.Url() + "AddMessage", json=message1.to_dictionary())

        # Assert
        self.assertEqual(add_response.status_code, 404)
        self.assertIn('message_id = m1000 already exist', add_response.text)

        print("test_add_message_message_already_exist ended")

    def test_add_message_without_body(self):
        print("test_add_message_without_body starting")

        # AddMessage - the api to check
        add_response = requests.post(WebConfigurations.Url() + "AddMessage")

        # Assert
        self.assertEqual(add_response.status_code, 500)

        print("test_add_message_without_body ended")
