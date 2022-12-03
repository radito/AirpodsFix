#!/usr/bin/env zsh

# Setup Script to Install all dependencies

echo "Installing Dependencies ..."

HOMEBREW_NO_AUTO_UPDATE=1

if ! [ -x "$(command -v python3)" ]; then
    brew install python@3.9
fi

brew install switchaudio-osx
brew install --cask blackhole-2ch

pip3 install python-dotenv

echo "Running Interface Configuration"
echo -e "Please connect your bluetooth device !\n"

touch .env

python3 interface.py

echo "Setup Complete !"