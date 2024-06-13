from echo import Echo
from echo_rarity import EchoRarity
from echo_mainstats import Mainstats
import csv
from datetime import datetime

from pathlib import Path

import argparse

import random

fields = ["Mainstat", "Substat 1", "Substat 1 Value", "Substat 2", "Substat 2 Value", "Substat 3", "Substat 3 Value", "Substat 4", "Substat 4 Value", "Substat 5", "Substat 5 Value"]

class EchoSim:

    def __init__(self, 
                 output_file='outputs/output.csv', 
                 iterations=1000,
                 mainstat_whitelist=None, 
                 mainstat_blacklist=None) -> None:
        self.output_file = 'outputs/' + output_file + '.csv'
        self.iterations = iterations
        # Technically not necessary but we do this because default argument objects are mutable. This avoids potential funny accidents later.
        self.mainstat_whitelist = mainstat_whitelist if mainstat_whitelist else []
        self.mainstat_blacklist = mainstat_blacklist if mainstat_blacklist else []

    def simulate_n_echoes(self, n : int):
        try: 
            Path("outputs").mkdir(parents=True, exist_ok=True)
            with open(self.output_file, 'w') as csvfile:
                writer = csv.DictWriter(csvfile, fieldnames=fields, lineterminator="\n")
                writer.writeheader()

                for i in range(1, n + 1):
                    row = {}

                    # If mainstat is none, default behavior is to choose a random one (Random determination delegated to Echo class).
                    mainstat = None
                    if self.mainstat_whitelist:
                        mainstat = random.choice(self.mainstat_whitelist)
                    else:
                        possible_echo_mains = set(Mainstats)
                        for main in self.mainstat_blacklist:
                            possible_echo_mains.remove(main)
                        mainstat = random.choice(list(possible_echo_mains))

                    genned = Echo(rarity=EchoRarity.RANK_5, mainstat=mainstat)
                    for j in range(5):
                        genned.roll_substat()
                    row["Mainstat"] = genned.mainstat.value

                    k = 0

                    for substat in genned.substat_values:
                        row[f"Substat {k + 1}"] = substat.value
                        row[f"Substat {k + 1} Value"] = genned.substat_values[substat]
                        k += 1

                    writer.writerow(row)
        except RuntimeError as e:
            print(f"An error occurred while attempting to write to a file: {e}")

            

    def run(self):
        start_time = datetime.now()
        self.simulate_n_echoes(n=self.iterations)
        print(f"Time taken to generate {self.iterations} echoes: {datetime.now() - start_time}")

if __name__ == '__main__':
    # Argparse shit
    parser = argparse.ArgumentParser(prog="Wuwa-Echo-Sim", description="An echo sim for WuWa")
    parser.add_argument('-o', '--output_name', dest='output_name', default='output', help="Name of the output file. Will automatically be outputted to the folder 'outputs', and overwrite any previous files named output. File will automatically have .csv file extension as well. ")
    parser.add_argument('-i', '--iterations', dest="iterations", type=int, help="The number of desired echoes to simulate. Default is 100.", default=100)
    
    group = parser.add_mutually_exclusive_group()
    group.add_argument('-msw', 
                        '--mainstats_whitelist', 
                        dest='mainstats_whitelist', 
                        type=Mainstats, 
                        choices=list(Mainstats), 
                        nargs='*', 
                        help="The subset of mainstats the simulation should be restricted to. Mutually exclusive with -msb/--mainstats_blacklist")
    group.add_argument('-msb', 
                        '--mainstats_blacklist', 
                        dest='mainstats_blacklist', 
                        type=Mainstats, 
                        choices=list(Mainstats), 
                        nargs='*', 
                        help="The subset of mainstats the simulation should NOT use.")
    
    args = parser.parse_args()
    sim = EchoSim(output_file=args.output_name, 
                  iterations=args.iterations, 
                  mainstat_whitelist=args.mainstats_whitelist, 
                  mainstat_blacklist=args.mainstats_blacklist)
    sim.run()