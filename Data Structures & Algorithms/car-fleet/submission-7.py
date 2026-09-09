class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        position_speeds = {}
        for i in range(0, len(position)):
            position_speeds[position[i]] = speed[i]
        
        position.sort(reverse=True)
        fleet = 0
        reaching = []
        for i in range(0, len(position)):
            if i == 0:
                temp = ((target - position[i])/position_speeds[position[i]])
                reaching.append(temp)
                fleet += 1
            else:
                temp = ((target - position[i])/position_speeds[position[i]])
                if reaching[i-1] >= temp:
                    reaching.append(reaching[i-1])
                else:
                    reaching.append(temp)
                    fleet += 1
        return (fleet)