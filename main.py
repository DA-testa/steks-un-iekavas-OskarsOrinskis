# python3

from collections import namedtuple

Bracket = namedtuple("Bracket", ["char", "position"])


def are_matching(left, right):
    return (left + right) in ["()", "[]", "{}"]


def find_mismatch(text):
    opening_brackets_stack = []
    for i, next in enumerate(text):
        
        if next in "([{":
            
            # Process opening bracket, write your code here
            opening_brackets_stack.append(Bracket(next,i+1))
        
          

        if next in ")]}":
            # Process closing bracket, write your code here
            
            if not opening_brackets_stack:
                
                return i+1
        
        else: 

            top = opening_brackets_stack.pop()
            
            if not are_matching(top.char, next):
                
                return i+1
    
    
    if opening_brackets_stack:
        
        top = opening_brackets_stack.pop()
        
        return f"(top.position+1)"    
    
    return "Success"
        

def main():
    text = input()
    
    if "I" in text:
        
        text = input()
        
    


    mismatch = find_mismatch(text)
    
    if not mismatch:
        
        point("Success")
        
    else:
    
    
    print(mismatch)
    


if __name__ == "__main__":
    main()
