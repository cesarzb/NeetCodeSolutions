"""
Problem: Car Fleet
Link: https://neetcode.io/problems/car-fleet/question

You have two arrays, one with position of cars, 
the other one with speed.

They cannot overtake each other, so when they catch up to the slower car
in front of them they go behind it (so their positions are equal) all the way to the end.

Count how many fleets will arrive to destination.
"""

class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        fleets = 0
        max_time = 0

        cars = sorted(zip(position, speed), reverse=True)
        for car in cars:
            p, s = car
            distance = target - p
            time = distance / s
            if time > max_time:
                fleets += 1
                max_time = time

        return fleets
