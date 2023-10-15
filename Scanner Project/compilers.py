
# Identifying input and output files
#input_file = open("inputTiny.txt", 'r')
output_file = open("outputTokens.txt", "w+")

#input_file=""

#def getUrl(url):
    #input_file = open(url, 'r')
    #return input_file


#with open(url, 'r') as input_file
#data = f.read()


Reserved_words_tuple = ("if", "else", "then", "until", "read", "write", "repeat", "end")

Special_characters_dict = {
    '+': 'plus sign',
    '-': 'minus sign',
    '*': 'multiply sign',
    '/': 'division sign',
    '=': 'equal sign',
    '>': 'greater than sign',
    '<': 'less than sign',
    ';': 'semicolon',
    '(': 'open bracket',
    ')': 'closed bracket'
}
state_type = {"in_id" :"identifier", "in_num": "number", "in_assignment": "assignment"}
keys = Special_characters_dict.keys()

# Defining the class TokenRecord
class TokenRecord:
    def __init__(self, type, value):
        self.type = type
        self.value = value
    def print_token(self):
        output_file.write(self.value + "," + self.type + "\n")

# Scanning a character and determining the state
def getToken(look_ahead_char, line,input_file):
    # To store in it the value of the token to be generated
    state = "start"
    while 1:
        if(state != "done" and state != "trap"):
            if(look_ahead_char == ""):
                char = input_file.read(1)  # The character that makes us change states
                if(char == ""):

                    if(state == "in_comment" or state == "in_assign"):
                        if (state == "in_comment"):
                            token = create_token("ERROR", "Expected symbol '}' in line " + str(line))

                        else:
                            token = create_token("ERROR", "Unexpected symbol ':' in line " + str(line))
                        state = "trap"

                    elif (state == "in_num" or state == "in_id"):
                        token = create_token(state_type[state], parsed_string)
                        state = "done"
                    else:
                        return {"token": create_token("EOF", ""), "look_ahead_char": look_ahead_char, "line" :line}
            else:
                char = look_ahead_char
                look_ahead_char = ""


        if state == "start": # Start State

            parsed_string = ""
            if(char.isdigit()):
                state = "in_num"
                parsed_string = char
            elif(char.isalpha()):
                state = "in_id"
                parsed_string = char
            elif(char == ':'):
                state = "in_assignment"
                parsed_string = char
            elif(char == "{"):
                state = "in_comment"
            elif(char in keys):
                state = "done"
                token = create_token(Special_characters_dict[char], char)
            elif(char == " "or char == "\n" or char == "\t"):
                state = "start"
                if(char == "\n"):
                    line = line + 1;
            else:
                state = "trap"
                token = create_token("ERROR", "Unexpected symbol '" + char +"' in line " + str(line))

        elif state == "in_comment": # In-Comment State
            if(char == "}"):
                state = "start"
            elif (char == "\n"):
                line = line + 1
        elif state == "in_id": # In-ID State
            if (char.isalpha()):
                parsed_string = parsed_string + char
            else:
                if (parsed_string in Reserved_words_tuple):
                    token = create_token(parsed_string.upper(), parsed_string)
                else:
                    token = create_token(state_type[state], parsed_string)
                look_ahead_char = char
                state = "done"

        elif state == "in_num": # In-Num State
            if (char.isdigit()):
                parsed_string = parsed_string + char
            else:
                token = create_token(state_type[state], parsed_string)
                look_ahead_char = char
                state = "done"
        elif state == "in_assignment": # In-Assignment State
            if(char == "="):
                token = create_token(state_type[state], ":=")
                state = "done"
            else:
                state = "trap"
                token = create_token("ERROR", "Unexpected symbol ':' in line " + str(line))


        elif state == "done": # Done State

            return {"token":token,"look_ahead_char":look_ahead_char, "line" :line}

        elif state == "trap": # Trap State
            return {"token":token,"look_ahead_char":look_ahead_char, "line" :line}







def create_token(type, value):
    token = TokenRecord(type, value)
    return token


# The main --> should be a function later on
#if __name__ == '__main__':
def scannerMain(url):
    data=open(url,'r')
    # Loop to generate tokens until the end of the file
    look_ahead_char = ""
    line = 1
    token_number = 0
    while 1:
        result = getToken(look_ahead_char, line,data)
        token = result["token"]
        look_ahead_char = result["look_ahead_char"]
        line = result["line"]
        if (token.type == "ERROR"):
            output_file.close()
            return(token.value)    ###############TO BE PRINTED IN GUI
            break
        elif(token.type == "EOF"):
            output_file.close()
            return("DONE: The number of tokens = " + str(token_number))        ###############TO BE PRINTED
            break
        else:
            token.print_token()
            token_number = token_number + 1


