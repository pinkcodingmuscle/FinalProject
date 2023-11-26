class Message:
    handler = " "
    password = " "
    message = " "

    def __init__(self, handler, password, message) -> None:
        self.handler = handler
        self.password = password
        self.message = message

def save_message(message, filename):
    """This function will open file for appending. The handler
    will enter the username, password  and message for an agent.
    Args: 
        message and filename
    Returns:
        """
    messagelist = []
    with open(filename, "a"):
        messagelist.append(message)
    return messagelist

def handler_prompts(filename):
    """This function will create new message for agent.
    Args: 
        filename
    Returns:
        
        """
    agent_username = input("Enter agent username: ")
    agent_password = input("Enter agent password: ")
    agent_message = input("Enter new message: ")

    message = Message(agent_username, agent_password, agent_message)

    save_message(message, filename)