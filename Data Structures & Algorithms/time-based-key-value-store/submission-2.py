class TimeMap:

    def __init__(self):
        self.mapper = dict()
        

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key in self.mapper:
            self.mapper[key].append([value, timestamp])
        else:
            self.mapper[key] = list()
            self.mapper[key].append([value, timestamp])
        print(self.mapper)
        

    def get(self, key: str, timestamp: int) -> str:
        if not key in self.mapper:
            return ''
        
        values = self.mapper[key]

        l = 0
        r = len(values) - 1

        while l <= r:
            mid = (l+r) // 2
            if values[mid][1] == timestamp:
                return values[mid][0]
            elif values[mid][1] > timestamp:
                r = mid - 1
            else:
                l = mid + 1
        if r < 0:
            return ""
        else:
            return values[r][0]
