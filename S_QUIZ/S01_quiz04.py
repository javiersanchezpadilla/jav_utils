"""  ANSWER: A) True
    Explanation:
    x = [1, 2, 3]
    y = x[::-1] → creates a new reversed list: y = [3, 2, 1] (snapshot, 
    not reference)
    x.reverse() → reverses x in-place: x = [3, 2, 1]
    Now both x and y are [3, 2, 1]
    x == y → [3, 2, 1] == [3, 2, 1] → True
    Key Concept: [::-1] creates a NEW reversed copy, while .reverse() modifies 
    the original list in-place. They both end up as [3, 2, 1]!
    Docstring for S_QUIZ.S01_quiz04
"""

x = [1, 2, 3]
y = x[::-1]
x.reverse()

print(x == y)
