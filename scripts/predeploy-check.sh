#!/usr/bin/env bash
set -euo pipefail

ROOT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
cd "$ROOT_DIR"

echo "==> Running backend tests"
PYTHONPATH=backend python3 -m unittest \
  backend.tests.test_main \
  backend.tests.test_content_services \
  backend.tests.test_frontend_contract \
  -v

echo "==> Exporting static knowledge data"
PYTHONPATH=backend python3 -m app.export_cards

echo "==> Validating generated JSON"
python3 -m json.tool frontend/public/cards/today.json >/tmp/public-review-cards-today-check.json
python3 -m json.tool frontend/public/pages/index.json >/tmp/public-review-pages-index-check.json

echo "==> Checking for local path leaks"
if rg -n "/Users/|/var/folders|/private/" frontend/public/cards/today.json frontend/public/pages/index.json; then
  echo "Local path leak found in generated public JSON."
  exit 1
fi

echo "Predeploy check passed."
