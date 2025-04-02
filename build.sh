#!/usr/bin/env bash
# Exit on error
set -o errexit

# Modify this line as needed for your package manager (pip, poetry, etc.)
pipenv shell

# Convert static asset files
 python ./conectacaa/manage.py collectstatic --no-input

# Apply any outstanding database migrations
python ./conectacaa/manage.py migrate