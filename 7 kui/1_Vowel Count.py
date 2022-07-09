def get_count(sentence):
    count = 0
    for i in sentence:
        if i in 'aeiou':
            count += 1
    return(count)

# Best_way
# def getCount(inputStr):
#    return sum(1 for let in inputStr if let in "aeiouAEIOU")