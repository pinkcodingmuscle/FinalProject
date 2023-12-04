"""
Final Project   
=======================
Course:   CS 5001

This module contains the message class that deals with the message object
"""

class Message:
    def __init__(self, agent, password, message) -> None:
        self.agent = agent
        self.password = password
        self.message = message

    def display_message(self)->None:
        """This function will display the messages in formatted way
        Args: 
            self
        """
        print("_"*30)
        print("Message: " + self.message)
        print("_"*30)

