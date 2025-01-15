class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        # Initialize a dictionary to store the prefix sums and their counts
        prefix_sum_counts = {0: 1}
        running_sum = 0
        count = 0

        # Iterate through the array
        for num in nums:
            # Update the running sum
            running_sum += num

            # Check if the difference (running_sum - k) exists in the prefix_sum_counts
            if running_sum - k in prefix_sum_counts:
                count += prefix_sum_counts[running_sum - k]

            # Update the prefix_sum_counts dictionary
            if running_sum in prefix_sum_counts:
                prefix_sum_counts[running_sum] += 1
            else:
                prefix_sum_counts[running_sum] = 1

        return count
