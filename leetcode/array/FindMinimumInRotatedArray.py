class FindMin(object):
    def solution(self, array):
        left, right = 0, len(array)
        while left < right:
            mid = left + (right - left) / 2
            if array[mid] > array[right]:
                left = mid + 1
            elif array[mid] < array[right]:
                right = mid;
            else:
                if array[right - 1] < array[right]:
                    left = right
                    break
                right-=1
        return array[left]

