from message_class import Message
from encryption import encode_message

def save_message(message, filename)->list:
    """This function will open file for appending. The handler
    will enter the username, password  and message for an agent.
    Args: 
        message and filename
    Returns:
        list containing agent messages
        """
    with open(filename, "a") as file:
        message = file.write(f"\nusername={message.agent}:password={message.password}:message={message.message}")

def handler_prompts(filename)-> None:
    """This function will create new message for agent.
    Args: 
        filename
    Returns:
        None
        """
    agent_username = input("Enter agent username: ")
    agent_password = input("Enter agent password: ")
    agent_message = input("Enter new message: ")

    message = Message(agent_username, agent_password, encode_message(agent_message))
    save_message(message, filename)