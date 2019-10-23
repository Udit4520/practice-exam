#1

def isAnagram(first , second):
    first = input("Enter a word :")
    second = input("Enter another word :")
    if sorted(list(first.lower())) == sorted(list(second.lower())):
        print("True")
    else:
        print("False")
isAnagram("first" , "second")
