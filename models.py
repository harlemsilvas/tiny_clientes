from __future__ import annotations

from flask_sqlalchemy import SQLAlchemy


db = SQLAlchemy()


class Client(db.Model):
    __tablename__ = "clients"

    id = db.Column(db.Integer, primary_key=True)
    source_id = db.Column(db.String(64), index=True)
    code = db.Column(db.String(64), index=True)
    name = db.Column(db.String(255), nullable=False, index=True)
    fantasy_name = db.Column(db.String(255), index=True)
    address = db.Column(db.String(255))
    number = db.Column(db.String(64))
    complement = db.Column(db.String(255))
    district = db.Column(db.String(255), index=True)
    zip_code = db.Column(db.String(32), index=True)
    city = db.Column(db.String(255), index=True)
    state = db.Column(db.String(16), index=True)
    contact_notes = db.Column(db.Text)
    phone = db.Column(db.String(64), index=True)
    fax = db.Column(db.String(64))
    mobile = db.Column(db.String(64), index=True)
    email = db.Column(db.String(255), index=True)
    website = db.Column(db.String(255))
    person_type = db.Column(db.String(64), index=True)
    document = db.Column(db.String(64), index=True)
    state_registration = db.Column(db.String(64))
    state_registration_exempt = db.Column(db.String(32))
    status = db.Column(db.String(64), index=True)
    notes = db.Column(db.Text)
    marital_status = db.Column(db.String(64))
    profession = db.Column(db.String(128))
    sex = db.Column(db.String(32))
    birth_date = db.Column(db.String(32))
    birthplace = db.Column(db.String(128))
    father_name = db.Column(db.String(255))
    father_cpf = db.Column(db.String(64))
    mother_name = db.Column(db.String(255))
    mother_cpf = db.Column(db.String(64))
    segment = db.Column(db.String(128), index=True)
    salesperson = db.Column(db.String(128))
    invoice_email = db.Column(db.String(255))
    contact_types = db.Column(db.String(255))
    taxpayer = db.Column(db.String(64))
    tax_regime_code = db.Column(db.String(64))

    def full_address(self) -> str:
        parts = [
            self.address,
            self.number,
            self.complement,
            self.district,
            self.city,
            self.state,
            self.zip_code,
        ]
        return ", ".join(part for part in parts if part)
