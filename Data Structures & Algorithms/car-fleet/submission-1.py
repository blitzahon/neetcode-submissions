class Solution:
    def carFleet(self, target: int, position: list[int], speed: list[int]) -> int:
    # Pair each car's position with its speed
        cars = zip(position, speed)

        # Sort by position, descending (closest to target first)
        cars = sorted(cars, key=lambda c: c[0], reverse=True)

        stack = []

        for pos, spd in cars:
            # Time this car would take to reach target if unobstructed
            time = (target - pos) / spd

            # If it takes longer than the fleet ahead (top of stack),
            # it can never catch up -> it's a new fleet
            if not stack or time > stack[-1]:
                stack.append(time)
            # Otherwise it merges into the fleet ahead -> do nothing

        return len(stack)