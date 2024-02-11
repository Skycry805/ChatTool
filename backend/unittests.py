# Tests and Coverage - not pretty, but works great!

import unittest
import coverage

import atexit
import sys
import os

# Add project root to path
sc_path = os.path.dirname(os.path.realpath(__file__))
sys.path.append(sc_path)

print("Start Coverage")
# Ignore this file and dummy files
ignore = [__file__, "config.py", "backend/config.py", "*_template.py", "api_dev.py", "unittest*"]
cov = coverage.Coverage(source=[".",".."], omit=ignore)
cov.start()

# Import custom modules
import external
import api
from history import History

class UnittestExternal(unittest.TestCase):

    def test_json_select(self):
        json_element = {"Test1": {"Test2": "foo"}}
        path = ["Test1", "Test2"]
        self.assertEqual(external.json_select(json_element, path), "foo")
        # Wrong filter
        path = ["Test1", "ERROR"]
        self.assertIsNone(external.json_select(json_element, path))


    def test_unkown_url_json(self):
        # build data
        dict_data = {"model": "foo", "messages": [ {"role": "system"}, {"role": "user"}]}
        filter = ['choices', 0, 'message', 'content']

        header = {
                "Authorization": "key example",
                "User-Agent": "VS-Chat/1.0.0",
                "Content-Type": "application/json"
                }
        
        # Excetion catched by try. Expect None
        self.assertIsNone(external.send_request('http://null.niclas-sieveneck.de/', header, dict_data, filter))
        # HTTP != 200
        self.assertIsNone(external.send_request('http://niclas-sieveneck.de/test-not-exitst', header, dict_data, filter))


    def test_unkown_url_string(self):
        # build data
        dict_data = "Text=FooBar"
        filter = ['choices', 0, 'message', 'content']

        header = {
                "Authorization": "key example",
                "User-Agent": "VS-Chat/1.0.0",
                "Content-Type": "application/x-www-form-urlencoded"
                }

        # Excetion catched by try. Expect None
        self.assertIsNone(external.send_request('http://null.niclas-sieveneck.de/', header, dict_data, filter))
        # HTTP != 200
        self.assertIsNone(external.send_request('http://niclas-sieveneck.de/test-not-exitst', header, dict_data, filter))
        # Api without Post
        self.assertIsNone(external.send_request('https://httpbin.org/get', header, dict_data, filter))


    def test_request_filter(self):
        # build data
        dict_data = ""
        filter = ['choices', 0, 'message', 'content']

        header = {}

        # Wrong filter / Free api for testing
        self.assertIsNone(external.send_request('https://httpbin.org/post', header, dict_data, filter))
        # No filter
        self.assertIsInstance(external.send_request('https://httpbin.org/post', header, dict_data), dict)


    def test_translate(self):
        output = external.translate("de", "en", "Der Test.")
        self.assertIsNotNone(output)
        self.assertIsInstance(output, str)


    def test_translate_same_lang(self):
        output = external.translate("de", "de", "Der Test.")
        self.assertIsNotNone(output)
        self.assertIsInstance(output, str)


    def test_llm(self):
        output = external.llm("Just a test. Answer only with one word.")
        self.assertIsNotNone(output)
        self.assertIsInstance(output, str)


    def test_sentiment(self):
        output = external.sentiment("Good")
        self.assertIsNotNone(output)
        self.assertIsInstance(output, str)


# Test for api by using external class, neat
# For coverage: Flask functions will http-requested and will not impact coverage.
class UnittestApi(unittest.TestCase):

    header = {
            "User-Agent": "VS-Chat/1.0.0",
            "Content-Type": "application/json"
            }
    
    header_text = {
            "User-Agent": "VS-Chat/1.0.0",
            "Content-Type": "application/x-www-form-urlencoded"
            }
    

    base_url = "https://chat.niclas-sieveneck.de:5000"

    default_ok = {"status": "ok"}

    # Example message
    msg = {"message": "I am a Unittest and I'm testing units.", "sender": "foo", "language": "en"}


    def test_add_new_language_and_clear_history(self):
        api.add_new_language("fr")
        self.assertEqual(api.chat_history.language_list, ["en","fr"])
        # Clear
        api.clear_history()
        self.assertEqual(api.chat_history.language_list, ["en"])
        
    
    def test_build_messages(self):
        api.build_message(self.msg)


    def test_ask_bot(self):
        self.assertIsInstance(api.ask_bot("Respond with one digit number.", "en"), dict)


    def test_translate_message(self):
        self.assertIsInstance(api.translate_message("en", "de", "test"), str)


    # Test routes
    # Send a test message and send incomplete requests
    def test_send_message(self):
        url = self.base_url + "/send_message"
        req = external.send_request(url, self.header, self.msg)

        self.assertIsNotNone(req)
        
        self.assertEqual(req, {'status': 'ok'})

        # Direct call, for overview in Coverage
        #self.assertIsNone(api.send_message())
        # Bad request
        req = external.send_request(url, self.header)
        self.assertIsNone(req)
        

    def test_update_message(self):
        url = self.base_url + "/update_message/1"
        req = external.send_request(url, self.header)
        self.assertIsNotNone(req)
        self.assertTrue(req['1'])

        # Wrong ID
        url = self.base_url + "/update_message/-1"
        req = external.send_request(url, self.header)
        self.assertIsNone(req)

    def test_get_message_id(self):
        url = self.base_url + "/get_message_id"
        req = external.send_request(url, self.header_text, self.msg)
        self.assertIsNotNone(req)
        self.assertIsInstance(req['message_id'], int)


# Test chat history
class UnittestHistory(unittest.TestCase):

    chat_history = History()

    def test_create_history(self):
        self.chat_history = History()
        self.assertIsInstance(self.chat_history, History)
    
    def test_add_message_language(self):
        self.chat_history.messages_to_send["test"] = "test"
        self.assertEqual(self.chat_history.messages_to_send["test"], "test")
        self.chat_history.language_list.append("de")
        self.assertTrue(self.chat_history.language_list.count("de") == 1)
        self.chat_history.message_id = 1
        self.assertEqual(self.chat_history.message_id, 1)
    
    def test_clear_history(self):
        self.assertTrue(self.chat_history.reset())
        self.assertEqual(self.chat_history.messages_to_send, {})
        self.assertEqual(self.chat_history.language_list, ['en'])
        self.assertEqual(self.chat_history.message_id, 0)

# Fix for not closing coverage propperly
def additional_code():
    # Stop and generate report
    cov.stop()
    cov.report()
    # ensucre directory
    dir = os.path.dirname(os.path.realpath(__file__)) + "/coverage"
    cov.html_report(directory=dir)
    print("Stop Coverage")

if __name__ == '__main__':

    atexit.register(additional_code)
    unittest.main(verbosity=2)
