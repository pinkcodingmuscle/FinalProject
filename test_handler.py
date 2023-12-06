import unittest
from handler import handler_prompts

class TestHandler(unittest.TestCase):
    def setUp(self):
        self.handler_prompts = handler_prompts("messages_test")
    
    def test_inputExists(self):
        self.assertIsNotNone(self.handler_prompts)


if __name__ == "__main__":
    unittest.main()