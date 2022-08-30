import heapq

# two heaps + sliding window approach

# negative sign for max heap since python has min heap by DEFAULT, so negative
# sign is to simulate the proposed MAX heap!
# basically remember: - Add negative sign before the number when adding to max heap! -
# Put back the negative sign while popping the number! - Keep the sign in while comparing the top element
# of max heap to any number!
desc_smaller = []
asc_larger = []


def medianSlidingWindow(self, nums, k):
    res = []
    for right in range(0, len(nums)):
        add(nums[right])
        if right >= k - 1:
            res.append(getMedian())
            remove(nums[right - k + 1])
    return res


def add(num):
    if num > getMedian():
        heapq.heappush(asc_larger, num)
    else:
        heapq.heappush(desc_smaller, -num)

    re_balance()


def getMedian():
    if len(desc_smaller) == len(asc_larger):
        return (desc_smaller[0] + asc_larger[0]) / 2
    else:
        return desc_smaller[0]


def remove(num):
    if num > asc_larger[0]:
        index = asc_larger.index(num)
        asc_larger.remove(-num)
    else:
        desc_smaller.remove(num)

        re_balance()


def re_balance():
    if len(desc_smaller) < len(asc_larger):
        heapq.heappush(desc_smaller, -asc_larger[0])
    elif len(desc_smaller) - len(asc_larger) > 1:
        heapq.heappush(asc_larger, -desc_smaller[0])


