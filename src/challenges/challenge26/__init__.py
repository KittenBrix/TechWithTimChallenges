# PROMPT
# Coding Challenge #26
# Write a function that takes two strings as input and calculates the similarity score between them based on their token overlap.
# A token is defined as a word separated by spaces. The similarity score should be the ratio of the number of common tokens to 
# the total number of unique tokens in both strings combined. Return the score as a float between 0 and 1, where 0 means no similarity
# and 1 means identical strings.
# Test Cases
# Input: "hello world", "hello world"
# Output: 1
# Input: "hello world", "python code"
# Output: 0
# Input: "hello world python", "hello java python"
# Output: 0.5
# Input: "python programming language is fun and powerful", "python is powerful and fun"
# Output: 0.7142857142857143