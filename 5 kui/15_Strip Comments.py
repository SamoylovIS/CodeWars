def strip_comments(strng, markers):
    result = []
    comments = strng.split("\n")
    for comment in comments:
        for marker in markers:
            if marker in comment:
                comment = comment.split(marker)[0].strip()
        print(comment)
        result.append(comment)
    return '\n'.join(result)
strng = 'apples, pears # and bananas\ngrapes\nbananas !apples'
markers = ['#', '!']

strip_comments(strng, markers)
