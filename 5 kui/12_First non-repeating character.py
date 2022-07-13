def first_non_repeating_letter(string):
    for i in string:
        if string.lower().count(i.lower()) == 1:
            return i
    return ''

#Best way
#def first_non_repeating_letter(string):
#    return ([a for a in string if string.lower().count(a.lower()) == 1] or [''])[0]