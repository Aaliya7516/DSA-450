# We are given some website visits: the user with name username[i] visited the website website[i] at time timestamp[i].
# A 3-sequence is a list of websites of length 3 sorted in ascending order by the time of their visits.
# (The websites in a 3-sequence are not necessarily distinct.) 
# Find the 3-sequence visited by the largest number of users. If there is more than one solution, return the lexicographically smallest such 3-sequence.

# Example 1:

# Input: username = ["joe","joe","joe","james","james","james","james","mary","mary","mary"], 
#        timestamp = [1,2,3,4,5,6,7,8,9,10], 
#        website = ["home","about","career","home","cart","maps","home","home","about","career"]
# Output: ["home","about","career"]
# Explanation: 
# The tuples in this example are:
# ["joe", 1, "home"]
# ["joe", 2, "about"]
# ["joe", 3, "career"]
# ["james", 4, "home"]
# ["james", 5, "cart"]
# ["james", 6, "maps"]
# ["james", 7, "home"]
# ["mary", 8, "home"]
# ["mary", 9, "about"]
# ["mary", 10, "career"]
# The 3-sequence ("home", "about", "career") was visited at least once by 2 users.
# The 3-sequence ("home", "cart", "maps") was visited at least once by 1 user.
# The 3-sequence ("home", "cart", "home") was visited at least once by 1 user.
# The 3-sequence ("home", "maps", "home") was visited at least once by 1 user.
# The 3-sequence ("cart", "maps", "home") was visited at least once by 1 user.

# Example 2:
# Input: username = ["ua","ua","ua","ub","ub","ub"], 
#        timestamp = [1,2,3,4,5,6], 
#        website = ["a","b","a","a","b","c"]
# Output: ["a","b","a"]

# Note:
# 1) 3 <= N = username.length = timestamp.length = website.length <= 50
# 2) 1 <= username[i].length <= 10
# 3) 0 <= timestamp[i] <= 10^9
# 4) 1 <= website[i].length <= 10
# 5) Both username[i] and website[i] contain only lowercase characters.
# 6) It is guaranteed that there is at least one user who visited at least 3 websites.
# 7) No user visits two websites at the same time.

#  -------------------------------------- SOLUTION ----------------------------------------------

class Solution:
    def mostVisitedPattern(self, username: List[str], timestamp: List[int], website: List[str]) -> List[str]:

        # zip the time, user and website to one list
        tuw = list(zip(timestamp,username,website))

        # we need to sort them by time --> username --> website
        sorted_tuw = sorted(tuw)

        # We will polulate a user history hashmap of various pages visited. The hashmap is of type {user: [pages]}
        user_history = defaultdict(list)
        for t, u, w in sorted_tuw:
            user_history[u].append(w)

        # get various combinations possible for various users
        patternCount = defaultdict(int)
        for user,pages in user_history.items():
            
            # get various combinations possible for various users in the pair of 3 and add them to set so that they are unique
            userCombinations = set(combinations(pages,3))
            
            # for every pair of userCombination, we will update the count. This count will make sense for second user onwards having the same pattern
            for userCombination in userCombinations:
                patternCount[userCombination] += 1
        
        # We need to sort both the keys(pattern lexographically) from from min to max and values(score) form max to min 
        # If we inverse the values of keys from val to -val, then we can sort both of them in ascending order, using minhea
        # here invertedValues represent the values with -ve sign added to it
        invertedValues = [-x for x in patternCount.values()]
        
        # Zip both the keys and values so that we can sort them. We are placing invertedValues first as we first need to sort by score and then need to sort lexographically in natural order
        c = list(zip(invertedValues, patternCount.keys()))
        
        # Heapify will sort them in the ascending order as this is min heapify operation and will take nlog(n) time
        heapq.heapify(c)

        # Top of the heap will represent the sorted value by -ve score, we can return the second element from this popped element 
        return heapq.heappop(c)[1]
