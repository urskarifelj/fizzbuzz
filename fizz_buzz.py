# -*- coding: utf-8 -*-
#--author-- = Urska Rifelj

selected_number = int(raw_input("Select one number in range 1 to 100: "))
number = 1

while number <= selected_number:
    if number % 3 ==0 and number % 5 == 0:
        print "FizzBuzz"
    elif number % 3 == 0:
        print "fizz"
    elif number % 5 == 0:
        print "buzz"
    else:
        print number
    number += 1

a = "ThisSentenceIsWrittenCamelCase"

print a.lower(), "- not anymore!"