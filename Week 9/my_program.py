from thursdaylec import Planet
from thursdaylec import PlanetarySystem
from thursdaylec import Star

sun = Star("Sun", 789, 890,"Yellow")
ss = PlanetarySystem(sun)

p = Planet("Mercury", 1, 2, 3)
ss.add_planet(p)

p = Planet("Venus", 2,3,4)
ss.add_planet(p)

p = Planet("Saturn", 5, 6, 7)
ss.add_planet(p)

ss.show_planets()