from netcat.message import Message
import unittest
import json


standard = "utf-8"


class MessageTest(unittest.TestCase):
    expected_msg = "Hello, Bro"
    expected_title = "greedy"
    expected_bin_str_10 = ("43        " + json.dumps({"content": expected_msg, "type": expected_title})).encode(standard)
    expected_bin_str_10_no = (json.dumps({"content": expected_msg, "type": expected_title})).encode(standard)
    expected_bin_str_8 = ("43      " + json.dumps({"content": expected_msg, "type": expected_title})).encode(standard) 
    expected_bin_str_8_no = (json.dumps({"content": expected_msg, "type": expected_title})).encode(standard) 

    def test_get_message(self):
        # exact initial form
        test_message = Message(type_msg=self.expected_title, msg=self.expected_msg)
        self.assertEqual(self.expected_msg, test_message.get_message())

        # missing msg property
        test_message = Message(type_msg=self.expected_title)
        self.assertEqual("", test_message.get_message())

        test_message = Message(type_msg=self.expected_title, b_msg=self.expected_bin_str_10_no)
        self.assertEqual("", test_message.get_message())

        # using all properties
        test_message = Message(type_msg=self.expected_title, msg=self.expected_msg, b_msg=self.expected_bin_str_10_no)
        self.assertEqual(self.expected_msg, test_message.get_message())

        # using only b_msg
        test_message = Message(b_msg=self.expected_bin_str_10_no)
        self.assertEqual(self.expected_msg, test_message.get_message())

        Message.header_size = 8
        test_message = Message(b_msg=self.expected_bin_str_8_no)
        self.assertEqual(self.expected_msg, test_message.get_message())

    def test_get_message_type(self):
        # exact initial form
        test_message = Message(type_msg=self.expected_title, msg=self.expected_msg)
        self.assertEqual(self.expected_title, test_message.get_message_type())

        # missing msg_type property 
        test_message = Message(msg=self.expected_msg)
        self.assertEqual("", test_message.get_message_type())

        test_message = Message(msg=self.expected_msg, b_msg=self.expected_bin_str_10_no)
        self.assertEqual("", test_message.get_message_type())

        # using all properties
        test_message = Message(type_msg=self.expected_title, msg=self.expected_msg, b_msg=self.expected_bin_str_10_no)
        self.assertEqual(self.expected_title, test_message.get_message_type())

        # using only b_msg
        test_message = Message(b_msg=self.expected_bin_str_10_no)
        self.assertEqual(self.expected_title, test_message.get_message_type())

        Message.header_size = 8
        test_message = Message(b_msg=self.expected_bin_str_8_no)
        self.assertEqual(self.expected_title, test_message.get_message_type())

    def test_get_encoded_message(self):
        # exact initial form
        test_message = Message(type_msg=self.expected_title, msg=self.expected_msg)
        self.assertEqual(self.expected_bin_str_10, test_message.get_encoded_message())

        # using only b_msg
        test_message = Message(b_msg=self.expected_bin_str_10_no)
        self.assertEqual(self.expected_bin_str_10, test_message.get_encoded_message())

        Message.header_size = 8
        test_message = Message(b_msg=self.expected_bin_str_8_no)
        self.assertEqual(self.expected_bin_str_8, test_message.get_encoded_message())
