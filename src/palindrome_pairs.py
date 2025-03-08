from typing import List

def find_palindrome_pairs(words: List[str]) -> List[List[int]]:
    """
    Find indices of pairs of words that form palindromes when concatenated.
    
    A palindrome pair is when two words, when concatenated in a specific order, 
    form a palindrome. The function returns all such unique index pairs.
    
    Args:
        words (List[str]): Input list of words
    
    Returns:
        List[List[int]]: List of index pairs that form palindrome pairs
    
    Time Complexity: O(n^2 * k), where n is the number of words and k is the max word length
    Space Complexity: O(1) for output, O(n) for operations
    
    Examples:
        ["abcd", "dcba"] -> [[0, 1], [1, 0]]
        ["a", ""] -> [[0, 1], [1, 0]]
    """
    def is_palindrome(s: str) -> bool:
        """Helper function to check if a string is a palindrome."""
        return s == s[::-1]
    
    result = []
    n = len(words)
    
    # Check each pair of words
    for i in range(n):
        for j in range(n):
            # Skip same word pairing
            if i == j:
                continue
            
            # Check if concatenated words form a palindrome in both orders
            if is_palindrome(words[i] + words[j]):
                result.append([i, j])
    
    return result