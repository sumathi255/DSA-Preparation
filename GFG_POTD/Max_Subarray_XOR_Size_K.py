class Solution:
    def maxSubarrayXOR(self, arr, k):
        # XOR of the first window of size k
        current_window_xor = 0
        for i in range(k):
            current_window_xor ^= arr[i]

        # Store the maximum XOR found so far
        max_window_xor = current_window_xor

        # Slide the window
        for i in range(k, len(arr)):
            # Remove element going out and add new element coming in
            next_window_xor = current_window_xor ^ arr[i] ^ arr[i - k]

            # Update current window XOR
            current_window_xor = next_window_xor

            # Update maximum XOR
            max_window_xor = max(max_window_xor, next_window_xor)

        return max_window_xor
