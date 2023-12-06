import unittest
from secretagent import showAgentMessages, load_agent_messages


class NameTestCase(unittest.TestCase):

    def test_showAgentMessages(self):
        resultOne = showAgentMessages("Elves needed at north pole!")
        resultTwo = showAgentMessages("Coast is clear...")
        resultThree = showAgentMessages("Meet handler at fountain")
        self.assertIn(resultOne, 'Message: Elves needed at north pole!')
        self.assertIn(resultTwo, 'Message: Coast is clear...')
        self.assertIn(resultThree, 'Message: Meet handler at fountain' )
    
if __name__=='__main__':
    unittest.main()


