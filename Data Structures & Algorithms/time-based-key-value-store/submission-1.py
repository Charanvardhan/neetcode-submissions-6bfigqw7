class TimeMap:

    def __init__(self):
        self.mapz = dict()

    def set(self, key: str, value: str, timestamp: int) -> None:
        if self.mapz.get(key, False):
            self.mapz[key].append([value, timestamp])
        else:
            self.mapz[key] = [[value, timestamp]]
        

    def get(self, key: str, timestamp: int) -> str:
        if not self.mapz.get(key, False):
            return ""
        
        l = 0
        r = len(self.mapz[key]) - 1\

        s = self.mapz[key]

        while l <= r:
            mid = (l + r) // 2

            if s[mid][1] == timestamp:
                return s[mid][0]

            elif s[mid][1] > timestamp:
                r = mid - 1
            
            else: 
                l = mid + 1
            
        if r != -1:
            return s[r][0]
        else:
            return ""
        
