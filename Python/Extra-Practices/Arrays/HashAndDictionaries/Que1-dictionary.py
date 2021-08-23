# my solution for -- https://www.hackerrank.com/challenges/two-strings/problem?h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=dictionaries-hashmaps

def twoStrings(s1, s2):
    # Write your code here
    s1 = set(s1)
    s2 = set(s2)
    result = "YES" if s1.intersection(s2) else "NO"
    return result