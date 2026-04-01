class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        cache = {}
        
        def dfs(i, j):
            # If we reached the end of the pattern, then match if we reached end of string too, otherwise no
            # NOTE: We could reach end of string and still have a .* or char* left in the pattern and still be a match
            # as these a*'s can match zero chars. So, we could have many things like "a*b*c*.*". Hence, checking with 
            # reaching end of pattern, because reaching end of string but still having some pattern left can still be a success case.
            if j == len(p):
                return i == len(s)
            
            if (i, j) in cache:
                return cache[(i, j)]
            
            # We know a match has occurred for sure if we still have some string left, and the pattern is either the char or .
            # Note that we may have reached end of string, in which case, the rest of the pattern MUST be of the type a* or .* to match
            # This is handled in first case in the if.
            hasMatch = i < len(s) and (s[i] == p[j] or p[j] == '.')
            if j + 1 < len(p) and p[j + 1] == "*":
                # We have a *, so either match none (especially useful if string reached end) OR match one and try to match more
                cache[(i, j)] = dfs(i, j + 2) or (hasMatch and dfs(i + 1, j))
            elif hasMatch:
                # No *, but we did match. So both pattern and string is consumed
                cache[(i, j)] = dfs(i + 1, j + 1)
            else:
                # No matches of any kind, can't even skip due to *. So clearly not matching
                cache[(i, j)] = False
            
            return cache[(i, j)]
        
        return dfs(0, 0)
