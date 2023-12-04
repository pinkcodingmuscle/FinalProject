"""
Final Project   
=======================
Course:   CS 5001

This module contains the functions pertaining to the agent. The agent messages will be collected and stored 
into a list. Once the agent enters the correct username and password, their messages will be displayed on the screen.
While the messages are parsed, they will be decoded so that the agent can read them once they are displayed on the
screen.

"""

from message_class import Message
from encryption import decode_message

def load_agent_messages(filename)->list:
    """This function will read from a specified file and load 
        agent messages onto the screen.
    Args:
        filename
    Returns:
        list: will return a list containing the messages for the agent that match a 
        given username and password.
    """
    try:
        messagelist = []
        with open(filename , "r") as f:
            for line in f:
                agent = line.strip().split(":")[0].split("=")[1] 
                password = line.strip().split(":")[1].split("=")[1]
                message = line.strip().split(":")[2].split("=")[1]
                # the meesage will be decoded as it is appended to the list containing messages
                messagelist.append(Message(agent, password, decode_message(message)))
            return messagelist
    except FileNotFoundError as ex:
        print("File not found!")
    except PermissionError as ex:
        print("You do not have permission to access this file.", ex)
    except OSError as ex:
        print("File cannot be found. File might have been deleted or saved in different path.", ex)
    except TypeError as ex:
        print("Invalid type:- ", ex)


def showAgentMessages(messages) -> str:
    """This function will return a list of agent messages
    Args:
        messages
    Returns: 
        list: this will return a list of messages assigned to the agent
    """
    username = input("Enter your username: ").strip()
    password = input("Welcome, " + username  + ". What is your password: ").strip()
    
    count = 0
    for message in messages:
        if message.agent == username and message.password == password:
            count += 1
            message.display_message()
    print("End of messages.")

