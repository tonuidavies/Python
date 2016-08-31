"""In programming, a control structure is any kind of statement that
can change the path that the code execution takes. For example, a
control structure that decided to end the program if a number was
less than 5 would look something like this:"""
#!/usr/bin/env python2
import sys # Used for the sys.exit function
int_condition = 7
if int_condition < 6:
    sys.exit("int_condition must be >= 6")
else:
    print("int_condition was >= 6 - continuing")
