#!/bin/bash
coverage run --source=.. -m unittest discover -b -v -p "Fixture*.py"
echo -e '\n\n\n\n'
coverage report