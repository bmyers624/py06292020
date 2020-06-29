#!/usr/bin/python3
'''
Author: b.myers624@gmail.com
The purpose of this program is to teach students how python lists work. Students studying JSON may understand a list as an "array".
'''

# Zach says all code should live inside of a function
def main():
    movies = []   # one way to create a list
    movies.append("Avatar")   # .append is a list method that applies
                              # the value passed to is at the END of list

    movies.append("Back to the Future")

    print(movies) # use the print FUNCTION to display to std out
    
    # ["Avatar", "Back to the Future"]
    print(movies[0])  # display "Avatar"

    movies.append("Ghostbusters")  # add Ghostbusters to end of list

    # ["Avatar", "Back to the Future", "Ghostbusters"]
    print(movies[2])  # print out Ghostbusters
    print(movies[-1])  # print put Ghostbusters

    print(movies.index("Ghostbusters") # print index of first instance of
                                       # Ghostbusters

   

# Zach says this is the best way to run the main function
if __name__ == "__main__":
    main()

