"""
Create a function that takes a string as a parameter and returns the longest palindromic substring. A palindrome is a word, phrase, name, or number that reads the same forward or backward.
"""
def longest_palindromic_substring(s):
    # Store the length
    n = len(s)
    # Immediately return if less than 2 since its automatically a palindrome
    if n < 2:
        return s
    
    # Make sure to start at zero
    start = 0
    max_len = 1

    """
    Nest a function that will have two trackers one from the left and right that determines where and how long the longest palindrome begins. We want to find the center point of the word and track if the word match on each side.
    """
    def expand_around_center(left, right):
        while left >= 0 and right < n and s[left] == s[right]:
            left -= 1
            right += 1
        return right - left -1
    
    # Loop through each character to find the center of a potential palindrome
    for i in range(n):
        # See if this is a odd length
        len1 = expand_around_center(i, i)
        # Next check if its even
        len2 = expand_around_center(i, i +1)
        # Find the which word is longer
        max_curr_len > max(len1, len2)
        # Update our tracker if we found a longer palindrome
        if max_curr_len > max_len:
            max_len = max_curr_len
            start = i - (max_len - 1) // 2
    # Return the longest one found
    return s[start:start + max_len]