import matplotlib.pyplot as plt

euler_times = []
euler_currents = []
backeuler_times = []
backeuler_currents = []

with open("output.txt", "r") as file:
    for line in file:
        line = line.strip()  
        if line.startswith("euler"):
            parts = line.replace("euler: ", "").split(", ")
            if len(parts) > 1:
                try:
                    time = float(parts[0].split("=")[1].strip().replace('s', ''))
                    current = float(parts[1].split("=")[1].strip().replace('A', ''))
                    euler_times.append(time)
                    euler_currents.append(current)
                except ValueError:
                    print(f"Skipping line: {line}")
        elif line.startswith("backeuler"):
            parts = line.replace("backeuler: ", "").split(", ")
            if len(parts) > 1:
                try:
                    time = float(parts[0].split("=")[1].strip())
                    current = float(parts[1].split("=")[1].strip())
                    backeuler_times.append(time)
                    backeuler_currents.append(current)
                except ValueError:
                    print(f"Skipping line: {line}")

plt.plot(euler_times, euler_currents, label="Euler Method", color="blue", linestyle="--")
plt.plot(backeuler_times, backeuler_currents, label="Back Euler Method", color="red", linestyle="-",marker='o')
plt.xlabel('Time (s)')
plt.ylabel('Current (A)')
plt.legend()
plt.show()

