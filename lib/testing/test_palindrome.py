"""
This test suite follows Test-Driven Development (TDD) principles.
We write the tests BEFORE implementing the function, so we can verify
our solution actually works once it's written.
Start with the necessary imports of the function and pytest library.
"""
import pytest
from palindrome import longest_palindromic_substring


"""
Utility helper function to confirm any result we get back is truly a palindrome.
This is used across multiple tests as a sanity check.
"""
def is_palindrome(s):
    return s == s[::-1]


"""
Group basic test cases into a class — these match the examples given in the spec table.
"""
class TestBasicCases:

    # Test that 'babad' returns one of the two valid palindromes
    def test_babad_returns_valid_palindrome(self):
        result = longest_palindromic_substring("babad")
        assert result in ("bab", "aba"), f"Expected 'bab' or 'aba', got '{result}'"

    # Test that 'cbbd' returns 'bb', the only longest palindrome
    def test_cbbd_returns_bb(self):
        result = longest_palindromic_substring("cbbd")
        assert result == "bb", f"Expected 'bb', got '{result}'"

    # Test that a single character always returns itself
    def test_single_character_a(self):
        result = longest_palindromic_substring("a")
        assert result == "a"

    # Test that 'ac' returns either character since both are length-1 palindromes
    def test_two_different_characters(self):
        result = longest_palindromic_substring("ac")
        assert result in ("a", "c"), f"Expected 'a' or 'c', got '{result}'"

    # Test that 'racecar' returns the entire string since it's all a palindrome
    def test_racecar_is_full_palindrome(self):
        result = longest_palindromic_substring("racecar")
        assert result == "racecar"


"""
Group edge case tests into a separate class — these go beyond the spec table
to cover unusual or extreme inputs.
"""
class TestEdgeCases:

    # Test that a single digit string returns itself
    def test_single_digit(self):
        result = longest_palindromic_substring("7")
        assert result == "7"

    # Test that a string of all identical characters returns the whole string
    def test_all_same_characters(self):
        result = longest_palindromic_substring("aaaa")
        assert result == "aaaa"

    # Test that two identical characters return both
    def test_two_same_characters(self):
        result = longest_palindromic_substring("aa")
        assert result == "aa"

    # Test that a palindrome at the start of a string is found correctly
    def test_palindrome_at_start(self):
        result = longest_palindromic_substring("abacde")
        assert result == "aba"

    # Test that a palindrome at the end of a string is found correctly
    def test_palindrome_at_end(self):
        result = longest_palindromic_substring("xyzaba")
        assert result == "aba"

    # Test that a palindrome spanning the whole string is returned correctly
    def test_palindrome_in_middle(self):
        result = longest_palindromic_substring("abcdefdcba")
        assert result == "abcdefdcba"

    # Test that an even-length palindrome like 'abccba' is handled correctly
    def test_even_length_palindrome(self):
        result = longest_palindromic_substring("abccba")
        assert result == "abccba"

    # Test that an odd-length palindrome like 'abcba' is handled correctly
    def test_odd_length_palindrome(self):
        result = longest_palindromic_substring("abcba")
        assert result == "abcba"

    # Test that when no palindrome longer than 1 exists, a single char is returned
    def test_no_palindrome_longer_than_one(self):
        result = longest_palindromic_substring("abcde")
        assert len(result) == 1
        assert is_palindrome(result)

    # Test that a digits-only string works the same as a letters-only string
    def test_digits_only(self):
        result = longest_palindromic_substring("12321")
        assert result == "12321"

    # Test that a mixed digits and letters string finds the correct palindrome
    def test_mixed_digits_and_letters(self):
        result = longest_palindromic_substring("a1221b")
        assert result == "1221"

    # Test that a very long string with an embedded palindrome is handled correctly
    def test_long_string_with_palindrome_inside(self):
        s = "x" * 100 + "abcba" + "y" * 100
        result = longest_palindromic_substring(s)
        assert len(result) == 100
        assert is_palindrome(result)

    # Test the maximum allowed input length of 1000 characters
    def test_max_length_all_same(self):
        s = "a" * 1000
        result = longest_palindromic_substring(s)
        assert result == s

    # Test that every result across multiple inputs is always a valid palindrome
    def test_result_is_always_a_palindrome(self):
        test_strings = ["babad", "cbbd", "racecar", "abcde", "noon", "level"]
        for s in test_strings:
            result = longest_palindromic_substring(s)
            assert is_palindrome(result), (
                f"Result '{result}' for input '{s}' is not a palindrome"
            )

    # Test that every result is actually a substring found within the original input
    def test_result_is_a_substring_of_input(self):
        test_strings = ["babad", "cbbd", "racecar", "abcde", "noon"]
        for s in test_strings:
            result = longest_palindromic_substring(s)
            assert result in s, (
                f"Result '{result}' is not a substring of '{s}'"
            )