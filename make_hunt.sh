#! /bin/bash

# This script is used to copy the hunt files and fill in any templating we are using

# Copy the hunt files

THIS_DIR=$(pwd) || exit 1

mkdir -p "$THIS_DIR"/hunt

cp -r "$THIS_DIR"/hunt_files/* "$THIS_DIR"/hunt/

# Fill in the templating

