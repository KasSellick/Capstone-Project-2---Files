#Program for a small business to help manage tasks assigned to each member of the team

#=====importing libraries===========
#importing date and setting today's date
from datetime import date
today = date.today()



#empty lists for usernames and passwords in user.txt
usernames = []
passwords = []


#Reading user.txt, separating usernames and passwords and adding relavant data to 'usernames' and 'passwords' lists
with open('user.txt', 'r+') as user:
  for line in user:
    line_list_user = line.split(", ")
    usernames.append(line_list_user[0])
    password = line_list_user[1]
    password = password.rstrip("\n") #to remove the 'new line' command from the password
    passwords.append(password)

#====Login Section====

#empty variable to store username of logged in user
logged_in_user = ""

#username login
user_check = False
while user_check == False:
  login_user = input("\nPlease enter your username: ")
  if login_user in usernames:
    user_check = True
    logged_in_user = login_user
  else:
    print("\nThis username does not exist. Please try again.")

#password login
index = usernames.index(logged_in_user) #needed to match index of user to index of passwords
pass_check = False
while pass_check == False:
  login_pass = input("\nPlease enter your password: ")
  if login_pass in passwords[index]:
    pass_check = True
  else:
    print("\nIncorrect password. Please try again.")


#====Menu====

#Printing menu options:
while user_check ==  True and pass_check == True:
    #Options for admin
    if logged_in_user == "admin":
      print('''\nPlease select one of the following options:
r - register a user
a - add task
va - view all tasks
vm - view my tasks
s - view statistics
e - exit
: ''')

    #Options for all other users
    else:
      print('''\nPlease select one of the following options:
a - add task
va - view all tasks
vm - view my tasks
e - exit
: ''')
    #Menu selection from user
    menu = input("").lower()

    #Register a new user (admin only)
    if menu == 'r' and logged_in_user == "admin":
      #creating new username
      new_user_check = False
      while new_user_check == False:
        new_username = input("\nPlease enter the new username you would like to register: ")
        if new_username in usernames: #check if user already exists
          print("\nThis username already exists. Please enter another username.")
        else:
          new_user_check = True
          usernames.append(new_username) #add username to usernames list
      #creating new password
      new_password = input("\nPlease enter a password for your new user: ")
      new_password_check = input("\nPlease confirm your password: ") #reenter password to verify
      while new_password != new_password_check: #checking if passwords match
        print("\nYour passwords do not match. Please try again.")
        new_password = input("\nPlease enter a password for your new user: ")
        new_password_check = input("\nPlease confirm your password: ")
      passwords.append(new_password) #add password to passwords list
      #adding new user login to user.txt
      new_user = f"\n{new_username}, {new_password}"
      with open('user.txt', 'a+') as user:
        user.write(new_user)

    #Adding a task
    elif menu == 'a':
      #Check if a valid username has been used
      task_user_check = False
      while task_user_check == False:
        task_username_new = input("\nPlease enter the username of whom the task is assigned to: ")
        if task_username_new in usernames:
          task_user_check = True
        else:
          print("\nThis username does not exist. Please try again.")
      #Getting relevant information for task
      task_title_new = input("\nPlease enter the task title: ")
      task_desc_new = input("\nPlease enter the description of the task: ")
      task_assigned_new = today.strftime("%d %b %Y")
      task_due_new = input("\nPlease enter the due date of the task: ")
      task_completion_new = "No"
      #Adding task to tasks.txt
      task_total_new = f"\n{task_username_new}, {task_title_new}, {task_desc_new}, {task_assigned_new}, {task_due_new}, {task_completion_new}"
      with open('tasks.txt', 'a+') as tasks:
          tasks.write(task_total_new)

    #View all tasks
    elif menu == 'va':
      #Reading tasks.txt, separating information in each task and printing information for each task
      with open('tasks.txt', 'r') as tasks:
        task_num = 1
        for line in tasks:
          line_list_tasks = line.split(", ")
          task_username = line_list_tasks[0]
          task_title = line_list_tasks[1]
          task_desc = line_list_tasks[2]
          task_assigned = line_list_tasks[3]
          task_due = line_list_tasks[4]
          task_completion = line_list_tasks[5]
          task_completion = task_completion.strip("\n")
          # Calculate the maximum width for the values to align the text
          max_value_width = max(len(task_title), len(task_username), len(task_assigned), len(task_due), len(task_completion))
          # Print information on separate lines with labels and values aligned
          print("_"*50)
          print(f"\n\033[1mTask {task_num}\033[0m") 
          print(f"\n\033[1m{'Task:':<20}\033[0m{task_title:<{max_value_width}}")
          print(f"\033[1m{'Assigned to:':<20}\033[0m{task_username:<{max_value_width}}")
          print(f"\033[1m{'Date assigned:':<20}\033[0m{task_assigned:<{max_value_width}}")
          print(f"\033[1m{'Due date:':<20}\033[0m{task_due:<{max_value_width}}")
          print(f"\033[1m{'Task Complete?':<20}\033[0m{task_completion:<{max_value_width}}")
          print(f"\033[1mTask description:\033[0m \n\t{task_desc}\n")
          print("_"*50)
          task_num += 1

    #View tasks of current logged in user
    elif menu == 'vm':
      #Reading tasks.txt and separating information in each task
      with open('tasks.txt', 'r') as tasks:
        task_num = 1
        for line in tasks:
          line_list_tasks = line.split(", ")
          task_username = line_list_tasks[0]
          task_title = line_list_tasks[1]
          task_desc = line_list_tasks[2]
          task_assigned = line_list_tasks[3]
          task_due = line_list_tasks[4]
          task_completion = line_list_tasks[5]
          task_completion = task_completion.strip("\n")
          #checking if task username matches logged in user and printing the task if True
          if task_username == logged_in_user:
            # Calculating the length of the longest value to align the text
            max_value_width = max(len(task_title), len(task_username), len(task_assigned), len(task_due), len(task_completion))
            # Print each line with labels and values aligned
            print("_"*50)
            print(f"\n\033[1mYour Task {task_num}\033[0m")
            print(f"\n\033[1m{'Task:':<20}\033[0m{task_title:<{max_value_width}}")
            print(f"\033[1m{'Assigned to:':<20}\033[0m{task_username:<{max_value_width}}")
            print(f"\033[1m{'Date assigned:':<20}\033[0m{task_assigned:<{max_value_width}}")
            print(f"\033[1m{'Due date:':<20}\033[0m{task_due:<{max_value_width}}")
            print(f"\033[1m{'Task Complete?':<20}\033[0m{task_completion:<{max_value_width}}")
            print(f"\033[1mTask description:\033[0m \n\t{task_desc}\n")
            print("_"*50)
            task_num += 1

    #Statistics of users and tasks (admin only)
    elif menu == 's'and logged_in_user == "admin":
      num_users = len(usernames) #calculating number of users
      num_tasks = 0 #count for tasks
      with open('tasks.txt', 'r') as tasks:
        #calculating number of tasks
        for line in tasks:
          num_tasks += 1
        #Printing stats
        print("_"*50)
        print("\n\033[1mStatistics:\033[0m\n")
        print(f"\033[1mTotal number of users:\033[0m \t {num_users}")
        print(f"\033[1mTotal number of tasks:\033[0m \t {num_tasks}")
        print("_"*50)

    #Exiting program
    elif menu == 'e':
        print('\nGoodbye!')
        exit()

    #Invalid input from user
    else:
        print("\nYou have entered an invalid input. Please try again.")
