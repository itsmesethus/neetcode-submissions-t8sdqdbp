class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
#         Sure. `heapq` is a **built-in Python module** that implements a **Min-Heap (Priority Queue)** using a normal list.

# In a **min-heap**:
# ✅ smallest element is always at index `0`.

# ---

# # ✅ Import Syntax

# ```python
# import heapq
# ```

# ---

# # ✅ Main `heapq` Functions (Most Important)

# ---

# ## 1) `heapq.heapify(list)`

# ### ✅ What it does:

# Converts a normal list into a **heap in-place**.

# ### Syntax:

# ```python
# heapq.heapify(arr)
# ```

# ### Example:

# ```python
# import heapq

# arr = [5, 1, 9, 3]
# heapq.heapify(arr)
# print(arr)
# ```

# After heapify, `arr[0]` will be the smallest element.

# ⏱ Time: **O(n)**

# ---

# ## 2) `heapq.heappush(heap, item)`

# ### ✅ What it does:

# Inserts an element into heap while maintaining heap property.

# ### Syntax:

# ```python
# heapq.heappush(heap, item)
# ```

# ### Example:

# ```python
# import heapq

# heap = [2, 5, 7]
# heapq.heapify(heap)

# heapq.heappush(heap, 1)
# print(heap)
# ```

# ⏱ Time: **O(log n)**

# ---

# ## 3) `heapq.heappop(heap)`

# ### ✅ What it does:

# Removes and returns the **smallest element** from heap.

# ### Syntax:

# ```python
# x = heapq.heappop(heap)
# ```

# ### Example:

# ```python
# import heapq

# heap = [1, 4, 6, 9]
# heapq.heapify(heap)

# x = heapq.heappop(heap)
# print(x)     # 1
# print(heap)
# ```

# ⏱ Time: **O(log n)**

# ---

# ## 4) `heapq.heappushpop(heap, item)`

# ### ✅ What it does:

# Pushes an element first, then pops the smallest element.

# ### Syntax:

# ```python
# x = heapq.heappushpop(heap, item)
# ```

# ### Example:

# ```python
# import heapq

# heap = [2, 3, 5]
# heapq.heapify(heap)

# x = heapq.heappushpop(heap, 1)
# print(x)       # 1 (popped)
# print(heap)    # [2, 3, 5]
# ```

# Useful when maintaining fixed size heap.

# ⏱ Time: **O(log n)**

# ---

# ## 5) `heapq.heapreplace(heap, item)`

# ### ✅ What it does:

# Pops the smallest element first, then pushes the new element.

# ### Syntax:

# ```python
# x = heapq.heapreplace(heap, item)
# ```

# ### Example:

# ```python
# import heapq

# heap = [1, 4, 7]
# heapq.heapify(heap)

# x = heapq.heapreplace(heap, 10)
# print(x)      # 1 (removed)
# print(heap)   # [4, 10, 7]
# ```

# ⏱ Time: **O(log n)**

# ⚠️ Difference:

# * `heappushpop()` → push then pop
# * `heapreplace()` → pop then push

# ---

# ## 6) `heapq.nlargest(k, iterable)`

# ### ✅ What it does:

# Returns **k largest elements**.

# ### Syntax:

# ```python
# heapq.nlargest(k, arr)
# ```

# ### Example:

# ```python
# import heapq

# arr = [10, 40, 5, 70, 20]
# print(heapq.nlargest(3, arr))   # [70, 40, 20]
# ```

# ⏱ Time: **O(n log k)**

# ---

# ## 7) `heapq.nsmallest(k, iterable)`

# ### ✅ What it does:

# Returns **k smallest elements**.

# ### Syntax:

# ```python
# heapq.nsmallest(k, arr)
# ```

# ### Example:

# ```python
# import heapq

# arr = [10, 40, 5, 70, 20]
# print(heapq.nsmallest(2, arr))  # [5, 10]
# ```

# ⏱ Time: **O(n log k)**

# ---

# ## 8) `heapq.merge(*iterables)`

# ### ✅ What it does:

# Merges multiple sorted iterables into a single sorted iterator.

# ### Syntax:

# ```python
# heapq.merge(list1, list2)
# ```

# ### Example:

# ```python
# import heapq

# a = [1, 4, 7]
# b = [2, 3, 9]

# print(list(heapq.merge(a, b)))
# # [1, 2, 3, 4, 7, 9]
# ```

# Used in merging sorted streams.

# ---

# # ✅ Min Heap Example (Complete)

# ```python
# import heapq

# heap = [5, 2, 9, 1]
# heapq.heapify(heap)

# heapq.heappush(heap, 3)

# print(heapq.heappop(heap))  # smallest
# print(heap[0])              # current smallest
# ```

# ---

# # ✅ How to Make Max Heap in Python?

# Python supports only min heap directly.

# To make max heap:
# Store negative values.

# ```python
# import heapq

# arr = [10, 50, 20]
# maxheap = [-x for x in arr]
# heapq.heapify(maxheap)

# print(-heapq.heappop(maxheap))  # 50
# ```

# ---

# # ⭐ Quick Summary Table

# | Function            | What it does           |
# | ------------------- | ---------------------- |
# | `heapify(x)`        | convert list into heap |
# | `heappush(h, x)`    | insert element         |
# | `heappop(h)`        | remove smallest        |
# | `heappushpop(h, x)` | push then pop smallest |
# | `heapreplace(h, x)` | pop smallest then push |
# | `nlargest(k, x)`    | top k largest          |
# | `nsmallest(k, x)`   | top k smallest         |
# | `merge(a,b)`        | merge sorted lists     |

# ---

# If you want, I can also explain **heap property**, and why `heapq` is used in **Top K problems and Dijkstra algorithm** (very common interview topics).


        import heapq

        max_heap=[-s for s in stones]
        heapq.heapify(max_heap)

        while len(max_heap)>1:

            s1=heapq.heappop(max_heap)
            s2=heapq.heappop(max_heap)

            if s1!=s2:
                heapq.heappush(max_heap,s1-s2)

        return -max_heap[0] if max_heap else 0
