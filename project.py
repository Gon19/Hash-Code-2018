# R – number of rows of the grid (1 ≤ R ≤ 10000)
# C – number of columns of the grid (1 ≤ C ≤ 10000)
# F – number of vehicles in the fleet (1 ≤ F ≤ 1000)
# N – number of rides (1 ≤ N ≤ 10000)
# B – per-ride bonus for starting the ride on time (1 ≤ B ≤ 10000)
# T – number of steps in the simulation (1 ≤ T ≤ 10 )

# next N lines

# a – the row of the start intersection (0 ≤ a < R)
# b – the column of the start intersection (0 ≤ b < C)
# x – the row of the finish intersection (0 ≤ x < R)
# y – the column of the finish intersection (0 ≤ y < C)
# s – the earliest start(0 ≤ s < T)
# f – the latest finish (0 ≤ f ≤ T) , (f ≥ s + |x − a| + |y − b|)

# note that f can be equal to T – this makes the latest finish equal to the end of the simulation


class Ride():
    """docstring for Ride"""

    def __init__(self, a, b, x, y, s, f):
        super(Ride, self).__init__()
        self.a = a
        self.b = b
        self.x = x
        self.y = y
        self.s = s
        self.f = f


R, C, F, N, B, T = input().split()

print('R =', R, 'C =', C, 'F =', F, 'N =', N, 'B =', B, 'T =', T)

rides = []

for i in range(N):
    a, b, x, y, s, f = input().split()
    rides += [Ride(a, b, x, y, s, f)]