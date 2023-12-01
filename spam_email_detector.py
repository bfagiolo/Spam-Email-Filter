import os
import pickle

#email examples

#email_11 = "You are the newest visitor, claim your reward soon!"

email_list = []

dictionary = {} #dictionary that has ham and span count for each word

dictionary["you"] = (1,2)
dictionary["won"] = (1,0)
dictionary["lottery"] = (1,0)
dictionary["claim"] = (1,0)
dictionary["soon"] = (1,0)
dictionary["youve"] = (1,0)
dictionary["been"] = (2,0)
dictionary["selected"] = (1,0)
dictionary["special"] = (2,0)
dictionary["offer"] = (1,0)
dictionary["once"] = (1,0)
dictionary["lifetime"] = (1,0)
dictionary["opportunity"] = (1,0)
dictionary["we"] = (0,1)
dictionary["schedule"] = (0,1)
dictionary["time"] = (0,1)
dictionary["meet"] = (1,1)
dictionary["follow"] = (0,1)
dictionary["my"] = (0,1)
dictionary["linkedin"] = (0,1)
dictionary["account"] = (1,1)
dictionary["singles"] = (1,0)
dictionary["your"] = (3,1)
dictionary["area"] = (1,0)
dictionary["please"] = (1,0)
dictionary["send"] = (1,0)
dictionary["us"] = (1,0)
dictionary["password"] = (1,1)
dictionary["want"] = (0,1)
dictionary["reset"] = (0,1)
dictionary["special"] = (1,0)
dictionary["promotion"] = (1,0)
dictionary["limited"] = (1,0)
dictionary["leaked"] = (1,0)
dictionary["click"] = (1,0)
dictionary["here"] = (1,0)

email_checklist = [] #list that assigns each email to be ham or spam. 0 = ham, 1 = spam

email_1 = "You won the lottery! Claim soon"             # add each email to email_checklist to keep track of which ones are ham and spam
email_list.append(email_1)                              # add each email to email_list to filter/edit the string 
entry1 = [email_1, 1]
email_checklist.append(entry1)
email_2 = "You've been selected for a special offer"
email_list.append(email_2)
entry2 = [email_2, 1]
email_checklist.append(entry2)
email_3 = "Once in a lifetime opportunity"
email_list.append(email_3)
entry3 = [email_3, 1]
email_checklist.append(entry3)
email_4 = "Can we schedule a time to meet?"
email_list.append(email_4)
entry4 = [email_4, 0]
email_checklist.append(entry4)
email_5 = "You can follow my linkedin account"
email_list.append(email_5)
entry5 = [email_5, 0]
email_checklist.append(entry5)
email_6 = "Meet singles in your area"
email_list.append(email_6)
entry6 = [email_6, 1]
email_checklist.append(entry6)
email_7 = "Please send us your password"
email_list.append(email_7)
entry7 = [email_7, 1]
email_checklist.append(entry7)
email_8 = "Do you want to reset your password?"
email_list.append(email_8)
entry8 = [email_8, 0]
email_checklist.append(entry8)
email_9 = "Special promotion for a limited time"
email_list.append(email_9)
entry9 = [email_9, 1]
email_checklist.append(entry9)
email_10 = "Your account has been leaked! Click here"
email_list.append(email_10)
entry10 = [email_10, 1]
email_checklist.append(entry10)


# if the dictionary has already been saved to the file, load it up

if os.path.exists('dictionary.pickle'):                
    with open('dictionary.pickle', 'rb') as file:
        dictionary = pickle.load(file)

# if the list has already been saved to the file, load it up

if os.path.exists('email_checklist.pickle'):
    with open('email_checklist.pickle', 'rb') as file:
        email_checklist = pickle.load(file)



stop_words = [
    "a", "an", "and", "are", "as", "at", "for", "from", "has", "have", "in", "is", "it", "of",
    "on", "the", "to", "with", "shall", "do", "what", "when", "can" ]

# this function will transform the string into just lowercase words

def filter_string(input_string):
    # Function to remove stop words
    def remove_stop_words(text, stop_words):
        words = text.split()
        cleaned_words = [word for word in words if word.lower() not in stop_words]
        return ' '.join(cleaned_words)

    cleaned_string = ''.join(char.lower() for char in input_string if char.isalpha() or char.isspace())
    cleaned_string = remove_stop_words(cleaned_string, stop_words)
    return cleaned_string

stop_words = [
    "a", "an", "and", "are", "as", "at", "for", "from", "has", "have", "in", "is", "it", "of",
    "on", "the", "to", "with", "shall", "do", "what", "when", "can" ]


for item in email_list:
    item = filter_string(item)


# loop so that user can continously enter inputs

while True:
   
    invalid_words = [] 
    valid_words = []
    def remove_new_words(input_string, dictionary):  # function to remove new words
        words = input_string.split()

        for word in words:
            if word in dictionary:                  # checks original dictionary to decide if word is new or not
                valid_words.append(word)            # I made a list for all the old words and the new words (old = valid, new = invalid)
            else:
                invalid_words.append(word)

        valid_string = ' '.join(valid_words)
        return valid_string

    
    spam_emails = 0       # initiate variables to count emails
    ham_emails = 0      
    total_emails = 0


    for item in email_checklist:            # counts the spam, ham, and total emails
        element, value = item
        if value == 1:
            spam_emails += 1
        else:
            ham_emails += 1
    total_emails = spam_emails + ham_emails

    print("Enter 'erase' to reset all calculations")      # if user enters "erase", the previous history will be wiped (except original database)
    email_input = input("Enter email: ")

    if email_input.lower() == "erase":
        # Delete dictionary.pickle
        if os.path.exists('dictionary.pickle'):
            os.remove('dictionary.pickle')

        # Delete email_checklist.pickle
        if os.path.exists('email_checklist.pickle'):
            os.remove('email_checklist.pickle')

        break
        
    
    email_list.append(email_input)
    email_input = filter_string(email_input)                    # edits user input (cleans up new words, symbols, uppercase etc.)
    email_input = remove_new_words(email_input, dictionary)
   
    print()

    # performs spam calculation

    bunches = email_input.split()                           
    factor = spam_emails/total_emails
    for element in bunches:
        touple = dictionary[element]
        spam_count, ham_count = touple
        occurrences = spam_count 
        spam_probability = (occurrences + 1)/(spam_emails + total_emails)
        spam_probability = spam_probability * factor                         # gets probability for each word and then multiplies them by each other
        factor = spam_probability


    # performs ham calculation
    
    bunches = email_input.split()
    factor = ham_emails/total_emails
    for element in bunches:
        touple = dictionary[element]
        spam_count, ham_count = touple
        occurrences = ham_count
        ham_probability = (occurrences + 1)/(ham_emails + total_emails)
        ham_probability = ham_probability * factor
        factor = ham_probability
        

    # uses norm factor to get percent

    norm_factor = spam_probability + ham_probability 
    spam_percent = spam_probability/norm_factor
    spam_percentage = int(spam_percent*100)
    ham_percent = ham_probability/norm_factor
    ham_percentage = int(ham_percent*100)
    print("Probability of being a spam email:", spam_percent, " --> ", spam_percentage,"%")
    print("Probability of being a ham email:", ham_percent, " --> ", ham_percentage,"%")
    print()

    # compares percentages
    
    if spam_percent > ham_percent:
        spam_entry = [email_input, 1]
        email_checklist.append(spam_entry) # add new entry to list as a spam                  
        print("This email is most likely spam!")
        for word in invalid_words:
            dictionary[word] = (1,0)                                    # updates touple of existing words in dictionary
        for word in valid_words:                                        # adds new words to dictionary with a touple value being assigned 1 for spam
            current_value = dictionary[word]
            updated_value = (current_value[0] + 1, current_value[1])
            dictionary[word] = updated_value
            
    else:
        print("This email is most likely ham.")
        ham_entry = [email_input, 0]
        email_checklist.append(ham_entry) # add new entry to list as ham
        for word in invalid_words:
            dictionary[word] = (0,1)
        for word in valid_words:
            current_value = dictionary[word]
            updated_value = (current_value[0], current_value[1]+1)              # adds new words to dictionary with a touple value being assigned 1 for ham
            dictionary[word] = updated_value

        

    
    print()
   
    print("Spam emails history:", spam_emails)
    print("Ham emails history:", ham_emails)
    print("Total email history:", total_emails)
    print()

    with open('dictionary.pickle', 'wb') as file:       # save the dictionary to a file
        pickle.dump(dictionary, file)

    with open('email_checklist.pickle', 'wb') as file:  # save the list to another file
        pickle.dump(email_checklist, file)
