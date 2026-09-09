class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars = sorted(zip(position, speed), reverse=True)
        
        fleets = 0
        max_time_ahead = 0.0  # Time of the fleet leader ahead
        
        for pos, spd in cars:
            time_to_target = (target - pos) / spd
            
            # If this car takes longer than the fleet ahead, it creates a new fleet
            if time_to_target > max_time_ahead:
                fleets += 1
                max_time_ahead = time_to_target  # Update the new fleet's bottleneck time
                
        return fleets