def main():
    dictionary = {}
    dictionary["learning"] = "awesome"
    dictionary["coding"] = "fun"
    # ... Fill with more data
    remove_keys_containing_string(dictionary, "learn")

"""
This Python function takes in a dict and a string and  
removes all keys containing that string from the dict
"""
def remove_keys_containing_string(dictionary, remove):
    new_dictionary = {}
    for key in dictionary:
        if remove not in key:
            new_dictionary[key] = dictionary[key]
    
    print(new_dictionary)

# Using the special variable 
# __name__
if __name__=="__main__":
    main()