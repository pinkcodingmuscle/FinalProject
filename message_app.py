"""This will be the main function for the program."""
from secretagent import showAgentMessages, load_agent_messages
from handler import handler_prompts

WELCOME_PROMPT = """WELCOME TO THE SECRET AGENT MESSAGE PORTAL!"""
END_PROMPT = """Thank for using the secret agent message portal! Goodbye!"""
VERIFY_USER = """Are you an agent? Y or N: """
A_USERNAME = """Enter your username: """
A_PASSWORD = """Enter your password: """
INVALID_INPUT = "Invalid username and(or) password. Please try again"


def main():
    # Display the welcome prompt
    print(WELCOME_PROMPT)
    filename = "messages.dat"
    # while loop set to True
    while True:
        # get user input
        cmd = input(VERIFY_USER).casefold().strip()
        print(cmd)
        # if user is an agent
        if cmd == "yes" or cmd == "y": 
            # messages variable assigned to parsing function
            messages = load_agent_messages(filename) # this function loads and parses messages
            showAgentMessages(messages) # this function shows agent messages
        # if user is a handler
        elif cmd == "no" or cmd == "n":
            # this function asks for agent name and password and prompts handler to 
            # write message for agent which is then saved to file
            handler_prompts(filename) 
        # exit loop if the user enters quit or q
        elif cmd != "quit" or cmd != "q":
            break
    #display end prompt
    print(END_PROMPT)

if __name__ == "__main__":
    main()