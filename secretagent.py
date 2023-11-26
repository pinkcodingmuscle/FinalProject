class Message:
    def __init__(self, agent, password, message) -> None:
        self.agent = agent
        self.password = password
        self.message = message

    def display_content(self)->None:
        """This function will display the agent name, paswword and messages
        in a formatted way.
        Args:
            self
        Returns: 
            None
        """
        print("_"*30)
        print("Agent: " + self.agent)
        print("Password: " + self.password)
        print("Message: " + self.message)
        print("_"*30)

    def display_message(self)->None:
        """This function will display the messages in formatted way
        Args: 
            self
        Returns: 
            None
        """
        print("_"*30)
        print("Message: " + self.message)
        print("_"*30)

    def load_agent_messages(filename)->list:
        """This function will read from a specified file and load 
        agent messages onto the screen.
        Args:
            filename
        Returns:
            list of messages
        """
        # set variable for list of messages
        messagelist = []
        # open file
        with open(filename , "r") as f:
            # iterate through every line
            for line in f:
                fileinfo = line.split(":")
                agent = fileinfo[0].split("=")[1]
                password = fileinfo[1].split("=")[1]
                messageinfo = fileinfo[2].split("=")[1]
                message = Message(agent, password, messageinfo)
                messagelist.append(message)
            return messagelist
    
    def show_agent_message(username, password, messages)->list:
        """This function will return a list of agent messages
        Args:
            messages
        Returns: 
            a list of messages assigned to the agent"""
        # iterate through message list
        for messsage in messages:
            if message.agent == username and message.password == password:
                return "Message" + ":" + message.message
    