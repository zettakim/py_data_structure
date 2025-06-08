def is_palindrome(word: str) -> bool:
    """
    Check if a word is a palindrome.

    A palindrome reads the same forwards and backwards.

    :param word: The word to check.
    :return: True if the word is a palindrome, False otherwise.
    """
    left: int = 0
    right: int = len(word)-1
    while left < right:
        if word[left] != word[right]:
            return False
        left, right = left+1, right-1
    return True

    # test cases
    words = ["racecar", "rotor", "tomato", "별똥별", "코끼리", "우영우"]
    for word in words:
        print(f"{word} is a palindrome: {is_palindrome(word)}")
