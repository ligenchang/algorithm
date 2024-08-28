def test_anagram_checker():
    # Test Case 1: Anagrams
    assert anagram_checker("listen", "silent") == True, "Test Case 1 Failed"

    # Test Case 2: Not anagrams
    assert anagram_checker("hello", "world") == False, "Test Case 2 Failed"

    # Test Case 3: Different lengths
    assert anagram_checker("abc", "abcd") == False, "Test Case 3 Failed"

    # Test Case 4: Anagrams with different cases
    assert anagram_checker("Dormitory", "Dirty room") == True, "Test Case 4 Failed"

    # Test Case 5: Anagrams with spaces
    assert anagram_checker("conversation", "voices rant on") == True, "Test Case 5 Failed"

    print("All test cases passed!")

# Step 2: Implement the Function

def anagram_checker(str1, str2):
    
    # Remove spaces and convert to lowercase
    str1 = str1.replace(" ", "").lower()
    str2 = str2.replace(" ", "").lower()
    
    # Sort the characters and compare
    return sorted(str1) == sorted(str2)

# Step 3: Run the Tests

test_anagram_checker()
