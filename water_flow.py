# water_flow.py

# Constants
EARTH_ACCELERATION_OF_GRAVITY = 9.80665  # m/s²
WATER_DENSITY = 998.2                    # kg/m³
WATER_DYNAMIC_VISCOSITY = 0.0010016      # Pa·s

PVC_SCHED80_INNER_DIAMETER = 0.28687     # meters
PVC_SCHED80_FRICTION_FACTOR = 0.013
SUPPLY_VELOCITY = 1.65                   # m/s
HDPE_SDR11_INNER_DIAMETER = 0.048692     # meters
HDPE_SDR11_FRICTION_FACTOR = 0.018
HOUSEHOLD_VELOCITY = 1.75                # m/s

def water_column_height(tower_height, tank_height):
    return tower_height + (tank_height / 2)

def pressure_gain_from_water_height(height):
    return WATER_DENSITY * EARTH_ACCELERATION_OF_GRAVITY * height / 1000

def pressure_loss_from_pipe(diameter, length, friction_factor, fluid_velocity):
    return -friction_factor * length * WATER_DENSITY * fluid_velocity**2 / (2000 * diameter)

def pressure_loss_from_fittings(fluid_velocity, quantity_fittings):
    return -0.04 * WATER_DENSITY * fluid_velocity**2 * quantity_fittings / 2000

def reynolds_number(hydraulic_diameter, fluid_velocity):
    return WATER_DENSITY * hydraulic_diameter * fluid_velocity / WATER_DYNAMIC_VISCOSITY

def pressure_loss_from_pipe_reduction(larger_diameter, fluid_velocity, reynolds_number, smaller_diameter):
    ratio = larger_diameter / smaller_diameter
    k = 0.1 + (50 / reynolds_number) * (ratio**4 - 1)
    return -k * WATER_DENSITY * fluid_velocity**2 / 2000

def kpa_to_psi(kpa):
    return kpa * 0.1450377

# Bonus function for creativity
def psi_to_kpa(psi):
    return psi / 0.1450377

def main():
    print("Water Flow Pressure Calculator\n")

    tower_height = float(input("Enter the height of the water tower (meters): "))
    tank_height = float(input("Enter the height of the water tank (meters): "))
    length1 = float(input("Enter the length of the supply pipe (meters): "))
    quantity_fittings = int(input("Enter the number of 90° fittings: "))
    length2 = float(input("Enter the length of the house pipe (meters): "))

    height = water_column_height(tower_height, tank_height)
    pressure = pressure_gain_from_water_height(height)

    diameter = PVC_SCHED80_INNER_DIAMETER
    friction = PVC_SCHED80_FRICTION_FACTOR
    velocity = SUPPLY_VELOCITY
    loss = pressure_loss_from_pipe(diameter, length1, friction, velocity)
    pressure += loss

    loss = pressure_loss_from_fittings(velocity, quantity_fittings)
    pressure += loss

    reynolds = reynolds_number(diameter, velocity)
    loss = pressure_loss_from_pipe_reduction(diameter, velocity, reynolds, HDPE_SDR11_INNER_DIAMETER)
    pressure += loss

    diameter = HDPE_SDR11_INNER_DIAMETER
    friction = HDPE_SDR11_FRICTION_FACTOR
    velocity = HOUSEHOLD_VELOCITY
    loss = pressure_loss_from_pipe(diameter, length2, friction, velocity)
    pressure += loss

    print(f"\nPressure at house: {pressure:.1f} kilopascals")
    print(f"Pressure at house: {kpa_to_psi(pressure):.1f} psi")

if __name__ == "__main__":
    main()
