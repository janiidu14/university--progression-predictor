# I declare that my work contains no examples of misconduct, such as plagiarism, or collusion.
# Any code taken from other sources is referenced within my code solution.
# Student ID: 18671609
# Date: 2/12/2021

def main():
    #create a file to store the outcomes
    file = open('Progression Data.txt', 'w')

    #empty dictionary to store credit levels
    outcomes = {}

    #create variables to count credit levels
    progress = 0
    trailer = 0
    retriever = 0
    exclude = 0

    #count element of the dictionary
    counter = 0

    #variable to control while loop
    again = 'y'
    
    while again.lower() != 'q':
        #use get_credit function
        c_pass = get_credit('Pass')
        c_defer = get_credit('Defer')
        c_fail = get_credit('Fail')
        
        #sum of the credits
        total = c_pass + c_defer + c_fail

        #check validity of the total
        if total != 120:
            print('Total incorrect \n')
        #store valid data in a dictionary
        else:
            if c_pass == 120:
                print('Progress \n')
                progress += 1
                outcomes[counter] = f'Progress - {c_pass}, {c_defer}, {c_fail}'
         
            elif c_pass ==100:
                print('Progress(module trailer) \n')
                trailer += 1
                outcomes[counter] = f'Progress (module trailer) - {c_pass}, {c_defer}, {c_fail}'
                        
            elif c_pass <= 40 and c_fail >= 80:
                print('Exclude \n')
                exclude += 1
                outcomes[counter] = f'Exclude - {c_pass}, {c_defer}, {c_fail}'
                
            else:
                print('Module retriever \n')
                retriever += 1
                outcomes[counter] = f'Module retriever - {c_pass}, {c_defer}, {c_fail}'

            #iterate key of the dictionary
            counter+=1

        print("Would you like to enter another set of data?")
        again = input("Enter any key to continue or 'q' to quit and view results: ")
        print()

    #store values of the dictionary into the file        
    for value in outcomes:
        file.write(str(outcomes[value]) + '\n')

    #close file used to store the outcomes
    file.close()

    #calculate the total no of outcomes
    count = progress + trailer + exclude + retriever

    #display outcomes with horizontal histogram
    dash()
    print("Horizontal Histogram \n")
    print(f"Progress  {progress}   : {progress * '*'}")
    print(f"Trailer   {trailer}   : {trailer * '*'}")
    print(f"Retriever {retriever}   : {retriever * '*'}")
    print(f"Excluded  {exclude}   : {exclude * '*'}")
    print()
    dash()

    #display outcomes with vertical histogram
    print("Vertical Histogram \n")
    print(f'Progress {progress} | Trailer {trailer} | Retriever {retriever} | Exclude {exclude}')
    for i in range(count):
        #nested if-else loops to display asteriks
        if progress > 0:
            astericks(progress)
            progress -= 1
        else:
            blank_astericks(progress)
        
        if trailer > 0:
            astericks(trailer)
            trailer -= 1
        else:
            blank_astericks(trailer)

        if retriever > 0:
            astericks(retriever)
            retriever -= 1
        else:
            blank_astericks(retriever)

        if exclude > 0:
            astericks(exclude)
            exclude -= 1
            print()
        else:
            blank_astericks(exclude)
            print()
            
    print(count, "outcomes in total")
    dash()
    print()

    #open the file to read the outcomes
    file_read = open('Progression Data.txt', 'r')

    #read and display all the data of the file
    line = file_read.read()
    print(line)

    #close the file
    file_read.close()

    
#get credit and check for validity
def get_credit(level):
    while True:
        try:
            print("Please enter your credits at", level, ":", end = '')
            credit = int(input())
            
            if credit not in [0, 20, 40, 60, 80, 100, 120]:
                print('Out of range.')
                continue
            return credit
        
        except ValueError:
            print('Integer required.')

#print astericks
def astericks(outcome):
    astericks = int(outcome - (outcome - 1)) * '   *'
    print(f"{astericks:<13}", end='')

#print blanks
def blank_astericks(outcome):
    blank = int(outcome) * '   *'
    print(f"{blank:<13}", end='')

#print dashes
def dash():
    print('-' * 50)

#call the main function
main()
