#!/bin/bash
set -e

echo "🎯 SDE Interview Prep Tracker"
echo "=============================="

# Create venv if needed
if [ ! -d "venv" ]; then
    echo "Creating virtual environment..."
    python3 -m venv venv
fi

# Activate venv
source venv/bin/activate

# Install dependencies
echo "Installing dependencies..."
pip install -q -r requirements.txt

# Run server
echo ""
echo "✅ Server starting..."
echo "📍 http://localhost:8000/tools/sde-prep"
echo ""

python3 -m uvicorn sde_prep.main:app --reload --host 0.0.0.0 --port 8000
