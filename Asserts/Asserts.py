import unittest
from unittest import TestCase


class Asserts(TestCase):

    def check_message(self, returned_message, sent_message):
        self.assertEqual(returned_message["application_id"], sent_message.application_id)
        self.assertEqual(returned_message["session_id"], sent_message.session_id)
        self.assertEqual(returned_message["message_id"], sent_message.message_id)
        self.assertEqual(returned_message["participants"], sent_message.participants)
        self.assertEqual(returned_message["content"], sent_message.content)

    def check_messages(self, returned_message, list_of_sent_messages):
        for sent_message in list_of_sent_messages:
            if sent_message.message_id == returned_message["message_id"]:
                self.check_message(returned_message, sent_message)
