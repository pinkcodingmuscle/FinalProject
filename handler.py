"""
Final Project   
=======================
Course:   CS 5001

This module contains functions that deal with handler functions. The handler will write a 
message for an agent by entering the agent's corresponding username and password. The username,
password will be saved to a file in a formatted way and the message will be encoded before 
it is written to the file.

"""

from message_class import Message
from encryption import encode_message

def save_message(message, filename)->list:
    """This function will open file for appending and write to the file, 
    format will be (username=jesse:password=12field:message=Lv5jv'l fHTfl 5ffQfQ CEif5jHx!). 
        message and filename
    Returns:
        list: list containing agent messages
    """
    with open(filename, "a") as file:
        message = file.write(f"\nusername={message.agent}:password={message.password}:message={message.message}")

def handler_prompts(filename)-> None:
    """This function will create new message for agent. The handler
    will enter the username, password and message for an agent. Before 
    the message is caved to the file it will be encoded.
    Args: 
    Args: 
        filename
    Returns:
        str: the 
    """
    agent_username = input("Enter agent username: ")
    agent_password = input("Enter agent password: ")
    agent_message = input("Enter new message: ")

    # the message will be encoded before it is saved to the file
    message = Message(agent_username, agent_password, encode_message(agent_message))
    save_message(message, filename)