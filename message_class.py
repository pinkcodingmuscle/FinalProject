class Message:
    def __init__(self, agent, password, message) -> None:
        self.agent = agent
        self.password = password
        self.message = message

    def display_content(self)->None:
            """This function will display the agent name, paswword and messages
            in a formatted way.
            Args:
                message
            Returns: 
                None
            """
            print("*"*40)
            print("Agent: " + self.agent)
            print("Password: " + self.password)
            print("Message: " + self.message)
            print("*"*40)

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

