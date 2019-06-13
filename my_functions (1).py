
# coding: utf-8

# 
# These are my functions. insert_name and cbt_techniques are the personalized ones that differ from A3. 
# 

# In[31]:


def insert_name(): 
    """
    This helps Mantis deliver more personalized responses by asking for the user's name at the beginnning of the chat. 
    
    """
        
    name = input('Welcome! Please tell me your name.\n') 
    #name is assigned to whatever string the user says when Mantis asks for their name 
    
    print("Hi " + name + "! I am a therapist bot named Mantis here to help you with your mental health concerns.\n I can provide you with some Cognitive Behavioral Therapy techniques for you to try or we can just talk!")
    print("If you'd like some resources for Cognitive Behavioral Therapy techniques, please press A, otherwise feel free to tell me what's on your mind.")
    print ("Also, at any point during our chat if you'd like to stop, type in 'quit'")
    
    #A personalized introduction to the chatbot is then printed out with the user's name
    
    return name #name is returned


# In[32]:


def cbt_techniques():  
        """
  This is triggered if the user indicates that they want Cognitive Behavioral Therapy exercises to try by pressing 'A'. 
  Based on which concern the user wants exercises for, the user is redirected to a specific website.  
    
        """
    
        choice = input("Select which number you want some helpful exercises for.\n1.Anxiety 2.Depression")
        
#choice is assigned whatever value (1 or 2) that the user selects 
        if choice ==  "1":   #if the user selects 1 then they are redirected to a site that has exercises for anxiety
            print("https://www.psychpoint.com/mental-health/worksheets/cbt-for-anxiety/") 

        elif choice == "2": #if the user selects 2 then they are redirected to a site that has exercises for depression
            print("https://www.therapistaid.com/worksheets/decatastrophizing.pdf")


# In[33]:


def selector(input_list, check_list, return_list, name):
    """
   This helps Mantis take the user's input (input_list), check it against a list of targeted words 
   that Mantis has flagged (check_list), and select a randomized and targeted response from return_list 
   if one of the words is in check_list. 
   It also replaces default values with the user's name so the chat is more personalized.
   
   parameters: input_list, check_list, return_list, and name 
    
    """

    output = None  
    for word in input_list: #each element in input_list is looped through 
        if word in check_list:  #this conditional checks if this element (the user's word) appears in check_list
            output = random.choice(return_list).replace('XXXXX', name)
            break    #if a user's word appears in check_list, a randomized response from return_list is returned.
                     #the replace method is also called to replace 'XXXXX' in return_list with the user's name 

    return output


# In[34]:


def prepare_text(input_string):
    """
    Prepares the text for Mantis to process by making the text lowercase and also splitting the string into words  
    
    parameters: input_string
    """
    temp_string = input_string.lower() 
    out_list = temp_string.split() 
    
    return out_list   #returns out_list which carries the string that is broken into readable words.


# In[36]:


def end_chat(input_list):
    """
  This allows Mantis to know when the user wants to end the chat (through input_list) so she can 
  send a final message and end the chat. 
  
  parameters: input_list
    """
        
    #conditional that checks if user has specified that they want to end the chat through 'quit'
    if 'quit' in input_list:  
        output = True  #if the user has specified 'quit', then this will trigger the end message. 
    else:
        output = False 
        
    return output  

