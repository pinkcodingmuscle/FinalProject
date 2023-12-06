# Final Project Report

* Student Name: Esther Mukuye
* Github Username: pinkcodingmucle
* Semester: Fall 2023
* Course: CS 5001



## Description 
General overview of the project, what you did, why you did it, etc. 

This project focuses on the development of a message portal designed specifically for secret agents. The portal allows users to interact with encoded messages, ensuring secure communication.

The functionality of the portal is based on the user's response to the "ARE YOU AN AGENT?" prompt. If the user responds with "no," they are prompted to enter their agent username, password, and a message. This information is then saved to a file after encoding the messages for added security.

On the other hand, if the user responds with "yes," they are prompted to provide their username and password. The program then parses the file containing the encoded messages. When a match is found between the provided username and password and the stored credentials, the messages are decoded and displayed on the screen.

The motivation behind undertaking this project stems from a personal interest in action and thriller movies that feature secret agents and the pursuit of criminals. I to incorporate the knowledge gained through out this semster and this project serves as an opportunity to apply ans showcase the skills accquired. Furthermore, the experience of working with files during this course was engaging which prompted my decision to develop a project that incorporates file handling features.

Overall, this project aims to demonstrate the implemetation of a secure message portal for secrest agents as well as combining the excitment of spy movies with skills accquired this semester, with a specific emphasis on file handling operations.

## Key Features
Highlight some key features of this project that you want to show off/talk about/focus on. 

In this project some of the key features that can be highlighted are:

Message encoding: The project incorporates a feature where messages written by the handler are encoded before being saved to the file. This encoding process adds layers of security, ensuring that the messages are not easily accessed/readable by unathorized individuals.

Message decoding: The project also incorporates a feature where the messsages are decoded as the file is parsed. This allows the messages to be transformed from encoded foem to readable text. By decoding the messages, the secret messages, the secret agents can easily access and understand the content intended for them.

The encoding and decoding mechanisms implemented in the project significantly reduce the risk of messages being intercepted and read by unintended recipients. This security measure ensures that only the secret agents for whom the messages are intended can access and understand the information.

## Guide
How do we run your project? What should we do to see it in action? - Note this isn't installing, this is actual use of the project.. If it is a website, you can point towards the gui, use screenshots, etc talking about features.

To run the project and see it in action, follow these steps:

_Open the message_app.py file, which serves as the main function for the program.

_After running the script, the user will be prompted to enter "Y," "N," or "Q" in response to whether they are an agent.

_If the user enters "Y," they will be asked to provide a username and password. As an example, let's use the username "jesse" and password "12field."

_Once the correct username and password are entered, the messages associated with that agent will be loaded onto the screen. You will be able to see and interact with the messages. If the incorrect message or password are entered, the user will see no messages on the screen.

_If the user enters "N," they will be treated as a handler. As a handler, you will be prompted to enter a username, password, and a message intended for an agent. If you enter a new username and password, a new agent will be created with the provided credentials, and the message will be associated with that agent. If you enter an existing username and password, the messages associated with that agent will be displayed on the screen. To view the encoded message, open the messages.dat file.

_If the user enters "Q," the program will exit, and an end prompt will be printed on the screen.

By following these steps, you will be able to interact with the project, create agents, exchange messages, and view the messages for specific agents based on their usernames and passwords.

## Installation Instructions
If we wanted to run this project locally, what would we need to do?  If we need to get API key's include that information, and also command line startup commands to execute the project. If you have a lot of dependencies, you can also include a requirements.txt file, but make sure to include that we need to run `pip install -r requirements.txt` or something similar.

Here are the steps to run this project locally:

_Ensure that you have Python installed on your machine. You can download the latest version of Python from the official Python website (https://www.python.org) and follow the installation instructions for your operating system.

_Once Python is installed, clone or download the project's source code to your local machine. You can also launch GitHub Desktop from the command line.

_Navigate to the project directory in your terminal or command prompt.

_Once this is done, you can run the project by executing the following command in your terminal or command prompt.
    python3 message_app.py


## Code Review
Go over key aspects of code in this section. Both link to the file, include snippets in this report (make sure to use the [coding blocks](https://github.com/adam-p/markdown-here/wiki/Markdown-Cheatsheet#code)).  Grading wise, we are looking for that you understand your code and what you did.

github link - https://github.com/pinkcodingmuscle/FinalProject.git

This project is divided into 5 modules with the 6th being the one that contains the agent credentials and messages. The encryption module deals with the encoding and decoding of agent messages. 

A randonly generated cipher key and an alphabet variable containing ascii_letters and digits are used to encode and decode the message strings. In the encoding portion, the for loop loops through the message string grabbing each element and searching to see if it is in the alphabet provided. 
```
from string import ascii_letters, digits
# randomly generated cipher key 
CIPHER_KEY = "0XkDwIrGzYv17QfNiqgbZHJ5UhKEljCTRnxA9uaySWopM6emc2dP4sL83BVtFO"
ALPHABET = ascii_letters + digits

    # declare an empty string variable
    cipher_text = ""
    # iterate through message
    for i in message:
        if i in ALPHABET:
            position = ALPHABET.index(i) 
```
If it is indeed in the alphabet, the position of the element in the alphabet is captured and matched to the corresponding position in the cipher key. For example, the element at index at 17 in the alphabet is matched to the element at index 17 in the cipher key which then gives us our result. 

```
result = CIPHER_KEY[position]
cipher_text += result
```

The else statement takes into account message strings with punctuation which are added to the result string without being altered.
```
else:
    # takes into account punctuation
    cipher_text += i
return cipher_text
```


The opposite happens for the decoding portion of the code. The for loop checks to see if the encoded text is in the cipher key. The position of the element in the cipher key is captured and matched to that of the position in the alphabet. 
```
 message = ""
    # iterate through the cipher text
    for i in cipher_text:
        if i in CIPHER_KEY:
            position = CIPHER_KEY.index(i)
            result = ALPHABET[position]
            message += result
```

The result containing the decoded text is then added to the empty message string variable, the else statement takes into account punctuation.
```
    else:
            # takes into account punctuation
            message += i
return message

This portion of the code is from the loadAgentMessages function in the secretagent.py module. It parses through the file and splits each line to return a username, password and message. his information is then stored in a list. Before the messages are added to the list, they are decoded so that the agent is able to read them. This is later used by the loadAgnetMessage function to check whether the username and password exist and load the corresponding agent messages onto the screen. T
```
messagelist = []
with open(filename , "r") as f:
    for line in f:
        agent = line.strip().split(":")[0].split("=")[1] 
        password = line.strip().split(":")[1].split("=")[1]
        message = line.strip().split(":")[2].split("=")[1]
        # the meesage will be decoded as it is appended to the list containing messages
        messagelist.append(Message(agent, password, decode_message(message)))
    return messagelist
```
This snippet of code is from the handlerprompts function in the handler.py file. Once the handler enters the agent's username, password and message. This information is saved to a message variable that captures the agent username, password and message. However, before the messages are saved, to the file, they are encoded using the encode_message function from the encryption.py module. 
```
message = Message(agent_username, agent_password, encode_message(agent_message))
save_message(message, filename)
```
This for loop in the ShowAgentMessages function from the secretagent.py file, checks to see if the username and password entered by the user match the username and password in the file, then the messages for that particular agent are returned.
```
count = 0
    for message in messages:
        if message.agent == username and message.password == password:
            count += 1
            message.display_message()
    print("End of messages.")
```

### Major Challenges
Key aspects could include pieces that your struggled on and/or pieces that you are proud of and want to show off.

One of the challenges I faced during this project was testing each function, mainly because a significant number of functions included print statements. Since I couldn't utilize doctests, I had to write separate functions specifically for testing purposes. This turned out to be more difficult than anticipated and took up a considerable amount of time. However, overcoming this challenge allowed me to strengthen my testing skills and gain a deeper understanding of the project's functionality.

On the other hand, a particularly enjoyable aspect of the project was the encoding and decoding of messages. Before saving the messages to the file, I implemented encoding techniques to ensure their security and privacy. Similarly, when the messages were read by the agent, I incorporated decoding mechanisms to retrieve and interpret the original content. This part of the project not only added an interesting layer of complexity but also allowed me to demonstrate my creativity and problem-solving abilities.

## Example Runs
Explain how you documented running the project, and what we need to look for in your repository (text output from the project, small videos, links to videos on youtube of you running it, etc)

```
Are you an agent? Enter Y, N or Q to quit: Y
y
Enter your username: jesse
Welcome, jesse. What is your password: 12field
______________________________
Message: Elves needed at north pole!
______________________________
______________________________
Message: Coast is clear...
______________________________
______________________________
Message: Meet handler at fountain
______________________________
End of messages.
Are you an agent? Enter Y, N or Q to quit: Y
y
Enter your username: reindeer50
Welcome, reindeer50. What is your password: christmasatnu
______________________________
Message: We are a go for christmas!
______________________________
______________________________
Message: Elves needed urgently!
______________________________
End of messages.
Are you an agent? Enter Y, N or Q to quit: N
n
Enter agent username: Rutherford
Enter agent password: 15glazeswift
Enter new message: Mission is a go
Are you an agent? Enter Y, N or Q to quit: Y
y
Enter your username: Rutherford
Welcome, Rutherford. What is your password: 15glazeswift
______________________________
Message: Mission is a go
______________________________
End of messages.
Are you an agent? Enter Y, N or Q to quit: Q
q
Thank for using the secret agent message portal! Goodbye!
```

## Testing
How did you test your code? What did you do to make sure your code was correct? If you wrote unit tests, you can link to them here. If you did run tests, make sure you document them as text files, and include them in your submission. 

> _Make it easy for us to know you *ran the project* and *tested the project* before you submitted this report!_

_ For the encryption.py module, I used doc tests to test the encode and decode functions. The details of the test for this module are in the encryption_test.txt file.

_

## Missing Features / What's Next
Focus on what you didn't get to do, and what you would do if you had more time, or things you would implement in the future. 

If I had more time (or the opportunity to further develop this project in the future), there are several aspects I would have liked to explore and implement to enhance its functionality and user experience.

Firstly, I would have focused on creating a more secure method for the handler to write messages for the agent. Instead of requiring the agent's username and password, I would have implemented a more streamlined process where the handler enters the agent's name and message. This information would then be securely passed to the existing agent's data, including their username and password. This approach would enhance security while simplifying the message-writing process for each agent.

Additionally, I would have incorporated the use of JSON string formatting for the messages. By serializing the message data into JSON format, it would provide a standardized and structured approach to storing and retrieving message information. JSON would allow for easier data manipulation and potential integration with other systems or APIs.

Furthermore, I would have aimed to implement a graphical user interface (GUI) to enhance the overall user experience. A GUI would provide a more intuitive and visually appealing way for users to interact with the secret agent message portal. It could include features such as input fields, buttons, and visual representations of messages, making the application more user-friendly and accessible.

These ideas for further development would not only enhance the security and functionality of the project but also improve the overall user experience. Given more time or the opportunity to continue working on this project in the future, implementing these enhancements would be priorities to take the project to the next level.

## Final Reflection
Write at least a paragraph about your experience in this course. What did you learn? What do you need to do to learn more? Key takeaways? etc.

Reflecting on my experience in this course, I have gained valuable insights and developed essential skills in problem-solving through coding. Initially, I was unaware of the diverse range of problems that could be effectively addressed using code. The concept of a secret message portal, for instance, seemed daunting to tackle. However, this course has taught me to approach problems with a structured mindset and find innovative solutions through coding. I now understand the power of utilizing dictionaries, lists, and file writing techniques to achieve desired outcomes. Additionally, I have learned the importance of searching for solutions online, using appropriate keywords to find relevant resources and examples. This too is something I struggled with through out this course.

However, I acknowledge that there are areas where I can further improve. One aspect I need to focus on is enhancing my ability to explain my code to others. Communication and articulating my thought process can be challenging, but it is crucial for collaboration and sharing knowledge. I intend to actively practice explaining my code to colleagues and seeking feedback to refine my explanation skills. Furthermore, I recognize the value of patience and persistence when encountering complex problems. Instead of rushing to find quick solutions, I aim to embrace a mindset that allows me to sit with a problem, analyze it from different angles, and explore multiple potential solutions.

In conclusion, this course has been instrumental in honing my problem-solving skills through coding. It has expanded my understanding of how code can be utilized to address diverse challenges and has equipped me with valuable techniques. I understand that being a software engineer requires me to devote myself to a lifelong journey of learning because it is in the process of learning that one gets better. I have heard from several people in the tech industry that the beginning is always the hardest but I committed to persevere through this initial learning stage. Moving forward, I am committed to improving my ability to explain my code effectively and adopting a patient and persistent approach to problem-solving. I am excited to continue my learning journey and explore new avenues in the vast world of coding.