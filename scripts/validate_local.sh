#!/usr/bin/env bash
set -euo pipefail

echo "Validating container health..."

# Expected to be run after starting the container locally
curl -sSf http://localhost:8080/health

echo "OK"

