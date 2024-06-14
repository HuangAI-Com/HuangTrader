#!/bin/bash

echo "Running Unit tests"

pytest --random-order --cov=HuangTrader --cov-config=.coveragerc tests/
