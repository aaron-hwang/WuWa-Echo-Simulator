from echo import Echo
from echo_rarity import EchoRarity
import csv
from datetime import datetime

fields = ["Mainstat", "Substat 1", "Substat 1 Value", "Substat 2", "Substat 2 Value", "Substat 3", "Substat 3 Value", "Substat 4", "Substat 4 Value", "Substat 5", "Substat 5 Value"]

class EchoSim:

    def __init__(self, output_file='outputs/output.csv') -> None:
        self.iterations = 0
        self.output_file = output_file

    def simulate_n_echoes(self, n : int, output=None):
        try: 
            with open(self.output_file, 'w') as csvfile:
                writer = csv.DictWriter(csvfile, fieldnames=fields, lineterminator="\n")
                writer.writeheader()

                for i in range(1, n + 1):
                    row = {}
                    genned = Echo(rarity=EchoRarity.RANK_5)
                    for j in range(5):
                        genned.roll_substat()
                    row["Mainstat"] = genned.mainstat.value

                    k = 0

                    for substat in genned.substat_values:
                        row[f"Substat {k + 1}"] = substat.value
                        row[f"Substat {k + 1} Value"] = genned.substat_values[substat]
                        k += 1

                    writer.writerow(row)
        except:
            print("An error occurred while attempting to write to a file")

            

    def run(self):
        start_time = datetime.now()
        n = 100000
        self.simulate_n_echoes(n=n)
        print(f"Time taken to generate {n} echoes: {datetime.now() - start_time}")