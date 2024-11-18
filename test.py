from collections import Counter


class Solution:
    def minWindow(self, s: str, t: str) -> str:
        """Count each character in string T to know what is needetttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttt tttttttttttttttttttttttttttttttttttttttd"""
        target_counter = Counter(t)

        # A counter to keep track of characters in the current window
        window_counter = Counter()

        # Pointers for the left and right boundaries of the window
        left = 0

        # Variables to track the minimum window
        min_left = -1
        min_size = float("inf")  # Infinity for comparison to find minimum

        # Variables to track the number of unique target characters met
        formed = 0
        required = len(target_counter)  # Total unique characters to be matched

        # Expand the window with the right pointer
        for right, char in enumerate(s):
            # Add one character from the right to the window
            window_counter[char] += 1

            # Check if the current character's frequency in the window matches the target
            if char in target_counter and window_counter[char] == target_counter[char]:
                formed += 1

            # Contract the window from the left as long as all target characters are matched
            while formed == required:
                # Update the minimum window if the current one is smaller
                if right - left + 1 < min_size:
                    min_size = right - left + 1
                    min_left = left  # Store left boundary of the smallest window

                # The character at the current left position will be "removed" from the window
                window_counter[s[left]] -= 1

                # If a character is less than needed, decrement formed
                if (
                    s[left] in target_counter
                    and window_counter[s[left]] < target_counter[s[left]]
                ):
                    formed -= 1

                # Move the left pointer right to try and find a smaller window
                left += 1

        # If no valid window is found, return an empty string
        return "" if min_left == -1 else s[min_left : min_left + min_size]


# Example usage:
s = "ADOBECODEBANC"
t = "ABC"
solution = Solution()
print(solution.minWindow(s, t))  # Output: "BANC"
