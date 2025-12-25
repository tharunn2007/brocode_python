# match case statements are the alternative to using many elif statements
#       execute if value matches a "case"
#       benefits: cleaner and syntax is readable
def weekday(day):
    match day:
        case 1:
            return "Sunday"
        case 2:
            return "Monday"
        case 3:
            return "Tueday"
        case 4:
            return "Wednesday"
        case 5:
            return "Thursday"
        case 6:
            return "Friday"
        case 7:
            return "Saturday"
        #For calling that are not matching eg: 8 or 10
        case _: #ELSE ALTERNATIVE
            return "Not Valid"
print(weekday(1)) # returns Sunday
print(weekday(102))# reutnr Not valid 
                                    
                                    