#!/bin/bash

for test in test*.py
do
    echo Running $test
    python $test
done
