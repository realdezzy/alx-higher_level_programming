#!/usr/bin/env bash
# Script to get content-length
curl "$1" -s | wc -c
