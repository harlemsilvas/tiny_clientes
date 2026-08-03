from __future__ import annotations

import csv
from pathlib import Path

from flask import Flask

from config import Config
from models import Client, db


HEADER_MAP = {
    "ID": "source_id",
    "Código": "code",
    "Nome": "name",
    "Fantasia": "fantasy_name",
    "Endereço": "address",
    "Número": "number",
    "Complemento": "complement",
    "Bairro": "district",
    "CEP": "zip_code",
    "Cidade": "city",
    "Estado": "state",
    "Observações do contato": "contact_notes",
    "Fone": "phone",
    "Fax": "fax",
    "Celular": "mobile",
    "E-mail": "email",
    "Web Site": "website",
    "Tipo pessoa": "person_type",
    "CNPJ / CPF": "document",
    "IE / RG": "state_registration",
    "IE isento": "state_registration_exempt",
    "Situação": "status",
    "Observações": "notes",
    "Estado civil": "marital_status",
    "Profissão": "profession",
    "Sexo": "sex",
    "Data nascimento": "birth_date",
    "Naturalidade": "birthplace",
    "Nome pai": "father_name",
    "CPF pai": "father_cpf",
    "Nome mãe": "mother_name",
    "CPF mãe": "mother_cpf",
    "Segmento": "segment",
    "Vendedor": "salesperson",
    "E-mail para envio de notas fiscais": "invoice_email",
    "Tipos de Contatos": "contact_types",
    "Contribuinte": "taxpayer",
    "Código de regime tributário": "tax_regime_code",
}

ENCODINGS = ("utf-8-sig", "utf-8", "cp1252", "latin-1")


def create_app() -> Flask:
    app = Flask(__name__)
    app.config.from_object(Config)
    db.init_app(app)
    return app


def detect_encoding(csv_path: Path) -> str:
    last_error = None
    for encoding in ENCODINGS:
        try:
            with open(csv_path, "r", encoding=encoding, newline="") as handle:
                handle.read(2048)
            return encoding
        except UnicodeError as error:
            last_error = error
    raise RuntimeError(f"Nao foi possivel ler {csv_path}.") from last_error


def parse_embedded_csv_line(value: str) -> list[str]:
    return next(csv.reader([value], delimiter=",", quotechar='"'))


def normalize_row(row: list[str]) -> list[str]:
    cleaned = [value.strip() for value in row]
    if len(cleaned) == 1 and "," in cleaned[0]:
        return [value.strip() for value in parse_embedded_csv_line(cleaned[0])]
    return cleaned


def iter_csv_rows(csv_path: Path):
    encoding = detect_encoding(csv_path)

    with open(csv_path, "r", encoding=encoding, newline="") as handle:
        sample = handle.read(8192)
        handle.seek(0)
        delimiter = ";" if sample.count(";") >= sample.count(",") else ","
        reader = csv.reader(handle, delimiter=delimiter)

        headers = None
        for raw_row in reader:
            if not raw_row or not any(cell.strip() for cell in raw_row):
                continue

            row = normalize_row(raw_row)

            if headers is None:
                headers = row
                continue

            if len(row) < len(headers):
                row = row + [""] * (len(headers) - len(row))
            elif len(row) > len(headers):
                row = row[: len(headers)]

            yield dict(zip(headers, row))


def to_client_payload(raw_row: dict[str, str]) -> dict[str, str]:
    payload = {}
    for source_key, target_key in HEADER_MAP.items():
        payload[target_key] = (raw_row.get(source_key) or "").strip()
    return payload


def import_csv(csv_file: str | Path | None = None) -> int:
    app = create_app()
    csv_path = Path(csv_file or Config.DEFAULT_CSV_FILE)

    if not csv_path.exists():
        raise FileNotFoundError(f"Arquivo CSV nao encontrado: {csv_path}")

    with app.app_context():
        db.create_all()
        Client.query.delete()

        total = 0
        batch = []

        for raw_row in iter_csv_rows(csv_path):
            payload = to_client_payload(raw_row)
            if not payload["name"]:
                continue

            batch.append(Client(**payload))

            if len(batch) >= 500:
                db.session.bulk_save_objects(batch)
                db.session.commit()
                total += len(batch)
                batch = []

        if batch:
            db.session.bulk_save_objects(batch)
            db.session.commit()
            total += len(batch)

        return total


if __name__ == "__main__":
    imported = import_csv()
    print(f"{imported} clientes importados com sucesso.")
