import math as m
import numpy as np

def sin_table(start, end, entry_number):
	e = entry_number

    #calculating the values for the entries
	print(f"{'x'}\t{'sin(x)'}")
	x_entries = np.linspace(0, m.pi * 2, entry_number)
	sin_entries = np.linspace(m.sin(0), m.sin(m.pi * 2), entry_number)

    #printing out the entries
	for i in range(0, entry_number):
		print(f"{x_entries[i]}\t{sin_entries[i]}")

def main():
    sin_table(0.0, m.pi * 2, 1000)

if __name__=="__main__":
    main()