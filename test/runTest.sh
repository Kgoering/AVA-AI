#!/bin/bash
coverage run --source=.. -m unittest -v "FixtureBrain.py"
echo -e '\n\n\n\n'
coverage report