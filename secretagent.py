from message_class import Message

def load_agent_messages(filename)->list:
    """This function will read from a specified file and load 
        agent messages onto the screen.
    Args:
        filename
    Returns:
        list of messages
    """
    try:
        messagelist = []
        with open(filename , "r") as f:
            for line in f:
                agent = line.strip().split(":")[0].split("=")[1] 
                password = line.strip().split(":")[1].split("=")[1]
                message = line.strip().split(":")[2].split("=")[1]
                messagelist.append(Message(agent, password, message))
            return messagelist
    except FileNotFoundError:
        print("File not found!")


def showAgentMessages(messages) -> str:
    """This function will return a list of agent messages
    Args:
        messages
    Returns: 
        a list of messages assigned to the agent
    """
    username = input("Enter your name: ").strip()
    password = input("Welcome, " + username  + ". What is your password: ").strip()
    
    count = 0
    for message in messages:
        if message.agent == username and message.password == password:
            count += 1
            message.display_message()
    print("There are no more messages. ")

