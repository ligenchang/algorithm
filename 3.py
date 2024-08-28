def word_flipper(our_string):
    # Split the string into words, flip each word, and join them back together
    flipped_words = [word[::-1] for word in our_string.split()]
    return " ".join(flipped_words)

def test_word_flipper():
    # Test Case 1: Single word
    assert word_flipper("hello") == "olleh", "Test Case 1 Failed"

    # Test Case 2: Multiple words
    assert word_flipper("hello world") == "olleh dlrow", "Test Case 2 Failed"

    # Test Case 3: Empty string
    assert word_flipper("") == "", "Test Case 3 Failed"

    # Test Case 4: Sentence with punctuation
    assert word_flipper("Hello, world!") == ",olleH !dlrow", "Test Case 4 Failed"

    print("All test cases passed!")

# Step 3: Run the Tests

test_word_flipper()


