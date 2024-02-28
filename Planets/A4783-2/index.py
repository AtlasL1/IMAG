# IMAG
# A4782-2
# CSV Creation

import csv

planet_data = [
    {
        'Name': 'A4783-2',
        'Right ascension': '4h 42m 48.49686s',
        'Declination': '31° 42\' 23.5337"',
        'Apparent magnitude (V)': '18.3 - ~11.9',
        'Evolutionary stage': 'white dwarf',
        'Spectral type': 'B2 Ia',
        'Radial velocity': '5.27±95.40 km/s',
        'Parallax': '1.2341 ± 2.8599 mas',
        'Mass': '6.5 solar mass',
        'Radius': '> 5.35 ± 0.864 solar radius',
        'Luminousity': '498.39 solar luminosity',
        'Surface gravity': '8.49 cgs',
        'Temperature': '3477±89 K'
    }
]

csv_path = 'a4783-2.csv'
field_names = ['Name', 'Right ascension', 'Declination', 'Apparent magnitude (V)', 'Evolutionary stage', 'Spectral type', 'Radial velocity', 'Parallax', 'Mass', 'Radius', 'Luminousity', 'Surface gravity', 'Temperature']

with open(csv_path, mode='w', newline='', encoding='utf-8-sig') as file:
    writer = csv.DictWriter(file, fieldnames=field_names)
    writer.writeheader()
    for planet in planet_data:
        writer.writerow(planet)
