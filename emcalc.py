#!/usr/bin/env python3
"""
emcalc: Energy-mass calculator based on E=mc^2.
Calculates energy from mass and estimates device run time based on generated electricity.
"""

import sys
from typing import Dict, Any

C = 299792458  # Speed of light in m/s

def perform_calculations(
    mass_gram: float,
    practical_efficiency: float,
    j_to_electric: float,
    watt: float
) -> Dict[str, Any]:
    """Calculate energy output and device run time based on mass and system efficiencies."""
    mass_kg = mass_gram / 1000.0
    theoretical_energy = mass_kg * C**2
    practical_energy = theoretical_energy * practical_efficiency
    electric_energy = practical_energy * j_to_electric
    seconds = electric_energy / watt
    
    return {
        "theoretical_energy": theoretical_energy,
        "practical_energy": practical_energy,
        "electric_energy": electric_energy,
        "seconds": seconds,
        "hours": seconds / 3600.0,
        "days": seconds / (3600.0 * 24.0),
        "years": seconds / (3600.0 * 24.0 * 365.0)
    }

def main() -> int:

    print("\nWelcome to the emcalc application")
    try:
        mass_text = input("Enter the mass (grams): ").strip()
        mass_gram = float(mass_text)
        if mass_gram <= 0:
            raise ValueError("Mass must be greater than 0.")

        eff_in = input("Enter the mass-energy conversion efficiency (e.g., 0.90 for 90%). Press Enter for default 0.90: ").strip()
        practical_efficiency = float(eff_in) if eff_in else 0.90

        j_in = input("Please enter the joule-to-electricity efficiency (e.g., 0.35 for 35%). Press Enter for default 0.35: ").strip()
        j_to_electric = float(j_in) if j_in else 0.35

        device_name = input("Enter the device name (e.g. bulb). Press Enter for default 'bulb': ").strip() or "bulb"

        watt_in = input(f"Enter the power consumption of the {device_name} in watts. Press Enter for default 100: ").strip()
        watt = float(watt_in) if watt_in else 100.0
        
        if watt <= 0:
            raise ValueError("Wattage must be greater than 0.")

    except ValueError as exc:
        print(f"Invalid input! {exc} Exiting program.")
        return 1

    results = perform_calculations(mass_gram, practical_efficiency, j_to_electric, watt)

    print("\n--- RESULTS ---")
    print(f"Theoretical energy (at 100% efficiency): {results['theoretical_energy']:.0f} Joules")
    print(f"Practical energy (at {practical_efficiency*100:.2f}% efficiency): {results['practical_energy']:.0f} Joules")
    print("-" * 20)
    print(f"With the electricity generated from this energy, a {watt}-watt {device_name}:")
    print(f"Can run for approximately {results['seconds']:.0f} seconds.")
    print(f"(This is approximately {results['hours']:.0f} hours.)")
    print(f"(This is approximately {results['days']:.2f} days.)")
    print(f"(This is approximately {results['years']:.2f} years.)")
    return 0

if __name__ == "__main__":
    sys.exit(main())