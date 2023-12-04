# Final Project Report

* Student Name: Esther Mukuye
* Github Username: pinkcodingmucle
* Semester: Fall 2023
* Course: CS 5001



## Description 
General overview of the project, what you did, why you did it, etc. 
This project showcases a message portal for secret agents. When the user enters "no" for "ARE YOU AN AGENT?", they are prompted to enter the agent username, password and message. Before this information is saved to a file, the messages are encoded. If the user enters "yes" for "ARE YOU AN AGENT?", the user is prompted to enter their username and password. While the file is parsed for the messages, the messages are decoded. If the username and password match, the messages are loaded onto the screen.

I thought this would be an interesting project becasue I am a huge fan of action and thriller movies that involve secret agents and catching bad guys. I wanted to do a project that incorporated all that I learnt this semster. My favorite assignment during the course was working with files and I thought it would be agood idea to do a project that incorporated files.

## Key Features
Highlight some key features of this project that you want to show off/talk about/focus on. 

Once the handler writes a message for the agent, the message is encoded before it is saved to the file. The messages are then decoded while the file is being parsed and are displayed as decoded text to the screen. This is a security measure that decreases the risk of the messages being read by someone other than the secret agent to whom they were written.

## Guide
How do we run your project? What should we do to see it in action? - Note this isn't installing, this is actual use of the project.. If it is a website, you can point towards the gui, use screenshots, etc talking about features.

The project can be run from the message_app.py file. 
This will be the main function for the program. 
The user will be prompted to enter "Y, N or Q" when asked whether they are anagent. 
If the user enters "Y", the user is prompted for a username and then password. (Use this username and password as an example: jesse, 12field)
Once the correct username and password are entered, the messages will be loaded onto the screen
If the user enters "N", the user is treated as a handler and is prompted to enter a username, password and message for an agent. If a new username and password are entered, a new agent(with a new username, password and message) will be created otherwise, the messages will be displayed for the existing agent with correspondig username and password.
If the user enters "Q", the program exists and the end prompt is printed to the screen.

## Installation Instructions
If we wanted to run this project locally, what would we need to do?  If we need to get API key's include that information, and also command line startup commands to execute the project. If you have a lot of dependencies, you can also include a requirements.txt file, but make sure to include that we need to run `pip install -r requirements.txt` or something similar.

## Code Review
Go over key aspects of code in this section. Both link to the file, include snippets in this report (make sure to use the [coding blocks](https://github.com/adam-p/markdown-here/wiki/Markdown-Cheatsheet#code)).  Grading wise, we are looking for that you understand your code and what you did.

github link - https://github.com/pinkcodingmuscle/FinalProject.git

This snippet of code is for the encoding function. The for loop iterates through the message string and then checks to see if the contents of the message string are in the alphabet. The index of the element is captured and matched to the index position in the cipher key. The elemet at that index in the cipher kery is returned and added to the cipher text string varibale. If the element is not in the alphabet, it is added to the cipher text string variable as is.
```
# declare an empty string variable
cipher_text = ""
# iterate through message
for i in message:
    if i in ALPHABET:
        position = ALPHABET.index(i) 
        result = CIPHER_KEY[position]
        cipher_text += result
    else:
        # takes into account punctuation
        cipher_text += i
return cipher_text
```
This portion of the is found in the decoding function of the encryption.py file and does the opposite of the encoding function
```
 # declare an empty string variable
    message = ""
    # iterate through the cipher text
    for i in cipher_text:
        if i in CIPHER_KEY:
            position = CIPHER_KEY.index(i)
            result = ALPHABET[position]
            message += result
        else:
            # takes into account punctuation
            message += i
    return message
```
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


### Major Challenges
Key aspects could include pieces that your struggled on and/or pieces that you are proud of and want to show off.

One of the challenges of this project was testing each function as majority of the functions included print statements. Since I could not use doctests I had to write functions to test the file. This was a lot more difficult that expected and took a lot more time. A fun part of the the project was encoding the messages as they are saved to the file and decoding them before they are read by the agent. 

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

I would have liked to create a more secure way of the handler writing messages for the agent so that instead of entering the agent's username and password, they enter the agent's name and message so that this information is passed to the existing agent information such as username and password. 

I would also have liked to write the messages in JSON string format.

I would also have liked to use imploy some sort of graphical user interface.

## Final Reflection
Write at least a paragraph about your experience in this course. What did you learn? What do you need to do to learn more? Key takeaways? etc.

The main takeaway from this course is developing problem-solving skills using code. Initially, I was unaware that even something like a secret message portal could be addressed as a problem. If I had been asked to provide a solution for such a problem before taking this course, I would have been unsure about how to proceed. However, I now realize that there are countless problems that can be effectively solved through coding. Secondly, I have learnt how to look for solutions to problems during coding I may encoounter and what words to use to search for these solutions. I have learnt many things but some of my favorite would be, how to use dictionaries, lists, how to write to a file. how to transform something from one obeject type to another. I need to work more on explaining my code as I fund it hard to explain it to other people. Another thing I think would be beneficial is learning to sit with a problem rather than wanting to solve it in one go. 