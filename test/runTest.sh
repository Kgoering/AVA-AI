#!/bin/bash
coverage run --source=.. -m unittest -v "FixtureBrain.py"
coverage report