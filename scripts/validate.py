#!/usr/bin/env python3
"""
validate.py
A helper script for the emcalc_analyzer skill to programmatically
validate metrics against physical boundaries.
"""

def validate_efficiencies(practical_eff: float, electric_eff: float) -> list:
    warnings = []
    
    if practical_eff > 1.0:
        warnings.append(f"CRITICAL: Practical efficiency > 100% ({practical_eff*100}%). This violates thermodynamics.")
    elif practical_eff > 0.1:
        warnings.append(f"NOTE: Practical efficiency is unusually high ({practical_eff*100}%). For comparison, nuclear fusion is ~0.7%.")
        
    if electric_eff > 1.0:
        warnings.append(f"CRITICAL: Electric efficiency > 100% ({electric_eff*100}%). This violates thermodynamics.")
    elif electric_eff > 0.7:
        warnings.append(f"NOTE: Thermal/Electric efficiency is very high ({electric_eff*100}%). Modern gas turbines max out around 60%.")
        
    return warnings

if __name__ == "__main__":
    import sys
    
    if len(sys.argv) < 3:
        print("Usage: python validate.py <practical_efficiency> <electric_efficiency>")
        sys.exit(1)
        
    p_eff = float(sys.argv[1])
    e_eff = float(sys.argv[2])
    
    issues = validate_efficiencies(p_eff, e_eff)
    if issues:
        for issue in issues:
            print(issue)
    else:
        print("All efficiencies appear to be within physically reasonable bounds.")
