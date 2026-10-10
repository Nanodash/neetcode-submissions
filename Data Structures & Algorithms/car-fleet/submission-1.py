class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars =  sorted(zip(position, speed), key=lambda t: t[0], reverse=True)
        # for each we check time to arrival, first car being the first to arrive mechanically (descending pos order)
        tta = []
        for car in cars:
            pos = car[0]
            speed = car[1]
            distance_to_arrival = target - pos
            time_to_arrival = distance_to_arrival / speed
            if len(tta) == 0 or tta[-1] < time_to_arrival:
                tta.append(time_to_arrival)
        return len(tta)
            
            


        