"""
Kayla Day
M2Lab_CaseStudy.py
The function of this program is
"""
# Constant variables
DEANS_LIST: float = 3.5
HONOR_ROLL: float = 3.25
QUIT: str = 'Q'

# Establish variables needed for program
gpa: float = 0.0
first_name: str = ''
last_name: str = ''

# Establish loop to be controlled by quit process
while last_name != QUIT:
    last_name = input('Enter last name or "Q" to quit: ') # Get input of student's last name
    if last_name == QUIT: # Check if last name equals the quit process, if it does, break the loop
        break
    first_name = input('Enter first name or "Q" to quit: ') # Get the input of the student's first name
    if first_name == QUIT: # Check if first name equals the quit process, if it does, break the loop
        break
    gpa = input('Enter student gpa: ') # Get input of student's gpa
    try:
        gpa = float(gpa) # Convert to a float 
    except ValueError: # Handling of value error is expected
        continue # Continue processing the loop
    """
    The next section begins the logic to determine if student is on honor roll or dean's list.
    This is kept inside the while loop so that these statements do not run if the quit process is used.
    Since each decision concludes the program, each statement that runs includes a break, to stop further and unneccessary processing.
    """
    # Begin logic to determine if student meets the required gpa for deans list/honor roll
    if gpa >= DEANS_LIST : # GPA must be equal to or higher than 3.5 
        # Let the student know that they made the dean's list
        print(f"Great work, {first_name} {last_name}! You are on the Dean's List!")
        break # Terminate loop because no further processing is needed
    elif (gpa < DEANS_LIST) and (gpa >= HONOR_ROLL):
        print(f"Great work, {first_name} {last_name}! You are on the Honor Roll!")
        break # Terminate loop because no further processing is needed
    else: # If this statement runs, then the student's gpa was under 3.25
        # Encourage student to keep trying
        print(f"Keep studying {first_name} {last_name} to raise your GPA!")
        break # Terminate loop, all decisions are finished.