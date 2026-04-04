def step(p,s,t):
    steps = (t - p)/s
    return steps

class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        pairedInfo = [(position[i], speed[i]) for i in range(len(position))]
        pairedInfo = sorted(pairedInfo, key= lambda x:x[0])
          
        fleets = list()
        fleets.append(step(pairedInfo[-1][0], pairedInfo[-1][1], target))

        for i in range(len(position) - 2, -1, -1):
            steps = step(pairedInfo[i][0], pairedInfo[i][1], target)
            if steps <= fleets[-1]:
                continue
            fleets.append(steps)
        
        return len(fleets)
