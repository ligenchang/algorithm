def test_string_reverser():
    # Test Case 1: Single word
    assert string_reverser("hello") == "olleh", "Test Case 1 Failed"

    # Test Case 2: Empty string
    assert string_reverser("") == "", "Test Case 2 Failed"
    print("test_string_reverser pass")

def string_reverser(our_string):
    
    # Reverse the string using slicing
    reversed_string = our_string[::-1]
    
    return reversed_string

test_string_reverser()



