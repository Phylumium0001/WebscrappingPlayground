#!/bin/bash

# Switch to centralised venvs
cd C:/Users/X/Documents/venvs

# Ask for project name
echo "Enter your project name:"
read project_name

# Ask for folder type (playground or work)
echo "Do you want to create the project in the 'playground' or 'work' folder?"
echo "Type 'playground' or 'work':"
read folder_type

# Validate folder type
if [ "$folder_type" != "Playground" ] && [ "$folder_type" != "Work" ]; then
  echo "Invalid folder type. Please type 'playground' or 'work'."
  exit 1
fi

# Create virtual environment name
venv_name="${project_name}_venv"

# Create virtual environment
python -m venv ${venv_name}

# Activate virtual environment
echo "Virtual environment created"

# Install Scrapy
echo "Do you want to install Scrapy in the virtual environment? (y/n)"
read install_scrapy
if [ "$install_scrapy" = "y" ]; then
  source ${venv_name}/bin/activate
  pip install scrapy
  deactivate
  echo "Scrapy installed successfully."
fi

# Open a new terminal with the virtual environment active

start powershell -WorkingDirectory "`pwd`" -Command "call ${venv_name}\\Scripts\\activate"