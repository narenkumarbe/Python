def not_string(str):
    if len(str)>=3 and str[:3]== "not":
        return str
    return "not " + str

not_string("candy")

Output:
'not candy'
===========================================================================================================================================
def missing_char(str,n):
    front = str[:n]
    back = str[n+1:]
    return front + back

missing_char("kitten", 1)

Output:
'ktten'
===========================================================================================================================================
def front_back(str):
    if len(str)<=1:
        return str
    mid = str[1:len(str)-1]
    return str[len(str)-1]+mid+str[0]

front_back("code")

Output:
'eodc'
===========================================================================================================================================
def front3(str):
    front_end=3
    if len(str)<front_end:
        front_end = len(str)
    front = str[:front_end]
    return front*3

front3("Java")

Output:
'JavJavJav'
=======================================================================================================================================
