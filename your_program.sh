#!/bin/sh
#
# Use this script to run your program LOCALLY.

set -e # Exit early if any commands fail

# Copied from .codecrafters/run.sh
#
# - Edit this to change how your program runs locally
exec python3 -m app.main "$@"
