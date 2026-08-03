#!/usr/bin/env bash

set -euo pipefail

ROOT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
VENV_DIR="$ROOT_DIR/.venv"
PYTHON_BIN="$VENV_DIR/bin/python"
PIP_BIN="$VENV_DIR/bin/pip"
FLASK_BIN="$VENV_DIR/bin/flask"
DB_FILE="$ROOT_DIR/clientes.db"

cd "$ROOT_DIR"

if [ ! -d "$VENV_DIR" ]; then
  echo "Criando ambiente virtual..."
  python3 -m venv "$VENV_DIR"
fi

if [ ! -x "$PYTHON_BIN" ]; then
  echo "Ambiente virtual invalido. Recrie a pasta .venv."
  exit 1
fi

echo "Instalando ou validando dependencias..."
"$PIP_BIN" install -r requirements.txt >/dev/null

if [ ! -f "$DB_FILE" ]; then
  echo "Banco local nao encontrado. Importando CSV..."
  "$PYTHON_BIN" csv_importer.py
fi

echo "Subindo aplicacao em http://127.0.0.1:5000"
exec "$FLASK_BIN" --app app run --debug
