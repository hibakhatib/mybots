from parallelHillClimber import PARALLEL_HILL_CLIMBER

phc = PARALLEL_HILL_CLIMBER()

phc.Evolve()
input("Press enter to view body after evolution")
phc.Show_Best()