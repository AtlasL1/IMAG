# IMAG
# A3750-9
# CSV Creation

import csv

planet_data = [
    {
        'Name': 'A3750-9',
        'Right ascension': '12h 10m 37.92303s',
        'Declination': '-33° 47\' 43.7397"',
        'Apparent magnitude (V)': '13.9 - ~16.8',
        'Evolutionary stage': 'pre-main sequence',
        'Spectral type': 'K5 IV(e) Li',
        'Radial velocity': '5.73±3.92 km/s',
        'Parallax': '7.3377 ± 0.0170 mas',
        'Mass': '0.9 solar mass',
        'Radius': '> 0.98 ± 0.032 solar radius',
        'Luminousity': '0.38 solar luminousity',
        'Surface gravity': '4.57 cgs',
        'Temperature': '1203±100 K'
    }
]

csv_path = 'a3750-9.csv'
field_names = ['Name', 'Right ascension', 'Declination', 'Apparent magnitude (V)', 'Evolutionary stage', 'Spectral type', 'Radial velocity', 'Parallax', 'Mass', 'Radius', 'Luminousity', 'Surface gravity', 'Temperature']

with open(csv_path, mode='w', newline='', encoding='utf-8-sig') as file:
    writer = csv.DictWriter(file, fieldnames=field_names)
    writer.writeheader()
    for planet in planet_data:
        writer.writerow(planet)
