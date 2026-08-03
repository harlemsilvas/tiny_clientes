from __future__ import annotations

from math import ceil

from flask import Flask, redirect, render_template, request, url_for
from sqlalchemy import func, or_

from config import Config
from models import Client, db


FORM_FIELDS = [
    "source_id",
    "code",
    "name",
    "fantasy_name",
    "person_type",
    "document",
    "state_registration",
    "state_registration_exempt",
    "status",
    "taxpayer",
    "tax_regime_code",
    "segment",
    "salesperson",
    "birth_date",
    "birthplace",
    "marital_status",
    "profession",
    "sex",
    "address",
    "number",
    "complement",
    "district",
    "zip_code",
    "city",
    "state",
    "contact_notes",
    "phone",
    "fax",
    "mobile",
    "email",
    "invoice_email",
    "website",
    "contact_types",
    "notes",
    "father_name",
    "father_cpf",
    "mother_name",
    "mother_cpf",
]


def fill_client_from_form(client: Client) -> Client:
    for field in FORM_FIELDS:
        setattr(client, field, request.form.get(field, "").strip())
    return client


def create_app() -> Flask:
    app = Flask(__name__)
    app.config.from_object(Config)
    db.init_app(app)

    @app.route("/")
    def index():
        page = request.args.get("page", default=1, type=int)
        query_text = request.args.get("q", default="", type=str).strip()
        state = request.args.get("state", default="", type=str).strip()
        city = request.args.get("city", default="", type=str).strip()

        query = Client.query

        if query_text:
            like_term = f"%{query_text}%"
            query = query.filter(
                or_(
                    Client.name.ilike(like_term),
                    Client.fantasy_name.ilike(like_term),
                    Client.document.ilike(like_term),
                    Client.email.ilike(like_term),
                    Client.phone.ilike(like_term),
                    Client.mobile.ilike(like_term),
                )
            )

        if state:
            query = query.filter(Client.state == state)

        if city:
            query = query.filter(Client.city.ilike(f"%{city}%"))

        per_page = 25
        total = query.count()
        clients = (
            query.order_by(Client.name.asc())
            .offset((page - 1) * per_page)
            .limit(per_page)
            .all()
        )

        stats = {
            "total_clients": db.session.query(func.count(Client.id)).scalar() or 0,
            "total_states": db.session.query(func.count(func.distinct(Client.state))).scalar() or 0,
            "total_cities": db.session.query(func.count(func.distinct(Client.city))).scalar() or 0,
            "with_email": db.session.query(func.count(Client.id)).filter(Client.email != "").scalar() or 0,
        }

        top_states = (
            db.session.query(Client.state, func.count(Client.id))
            .filter(Client.state != "")
            .group_by(Client.state)
            .order_by(func.count(Client.id).desc(), Client.state.asc())
            .limit(5)
            .all()
        )

        states = [
            row[0]
            for row in db.session.query(Client.state)
            .filter(Client.state != "")
            .distinct()
            .order_by(Client.state.asc())
            .all()
        ]

        return render_template(
            "index.html",
            clients=clients,
            filters={"q": query_text, "state": state, "city": city},
            page=page,
            total_pages=max(1, ceil(total / per_page)) if total else 1,
            total_results=total,
            stats=stats,
            top_states=top_states,
            states=states,
        )

    @app.route("/clients/new", methods=["GET", "POST"])
    def create_client():
        client = Client(
            person_type="Pessoa Fisica",
            status="Ativo",
            taxpayer="Nao informado",
        )

        if request.method == "POST":
            fill_client_from_form(client)
            if client.name:
                db.session.add(client)
                db.session.commit()
                return redirect(url_for("view_client", client_id=client.id))

        return render_template(
            "client_form.html",
            client=client,
            page_title="Novo cliente ou fornecedor",
            submit_label="Salvar cadastro",
            is_new=True,
        )

    @app.route("/clients/<int:client_id>")
    def view_client(client_id: int):
        client = Client.query.get_or_404(client_id)
        return render_template("client_detail.html", client=client)

    @app.route("/clients/<int:client_id>/edit", methods=["GET", "POST"])
    def edit_client(client_id: int):
        client = Client.query.get_or_404(client_id)

        if request.method == "POST":
            fill_client_from_form(client)
            if client.name:
                db.session.commit()
                return redirect(url_for("view_client", client_id=client.id))

        return render_template(
            "client_form.html",
            client=client,
            page_title="Editar cliente ou fornecedor",
            submit_label="Salvar alteracoes",
            is_new=False,
        )

    @app.post("/clients/<int:client_id>/delete")
    def delete_client(client_id: int):
        client = Client.query.get_or_404(client_id)
        db.session.delete(client)
        db.session.commit()
        return redirect(url_for("index"))

    return app


app = create_app()


if __name__ == "__main__":
    with app.app_context():
        db.create_all()
    app.run(debug=True)
