# Tests and Coverage - not pretty, but works great! - v1.0 Niclas Sieveneck

import unittest
import coverage

import atexit
import sys
import os

# Add project root to path
scPath = os.path.dirname(os.path.realpath(__file__))
sys.path.append(scPath)

print("Start Coverage")
# Ignore this file and dummy files
ignore = [__file__, "config.py", "backend/config.py", "*_dummy.py"]
cov = coverage.Coverage(source=[".",".."], omit=ignore)
cov.start()

# Import custom modules
import external

class Unittest_External(unittest.TestCase):

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
        import json
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