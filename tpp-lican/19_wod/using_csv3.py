#!/usr/bin/env py

import csv

with open('inputs/exercises.csv') as fh:
    reader = csv.DictReader(fh, delimiter=',')
    exercises = []
    for rec in reader:
        name, reps = rec['exercise'], rec['reps']
        low, high = 0, 0  # what goes here?
        exercises.append((name, low, high))
