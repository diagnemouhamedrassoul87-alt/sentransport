import json
from flask import Flask, jsonify, request
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

# Charger les données depuis le fichier JSON
with open("lignes_ddd.json", "r") as f:
    lignes = json.load(f)


# ── Endpoint d'accueil ──────────────────────────────────────────────────────
@app.route("/")
def accueil():
    return jsonify({
        "message": "Bienvenue sur l'API SenTransport !",
        "endpoints": ["/lignes", "/lignes/<id>", "/arrets", "/stats", "/lignes/recherche?q=..."]
    })


# ── GET /lignes  →  toutes les lignes ───────────────────────────────────────
@app.route("/lignes")
def get_lignes():
    return jsonify(lignes)


# ── GET /lignes/<id>  →  une ligne par son id ────────────────────────────────
@app.route("/lignes/<int:ligne_id>")
def get_ligne(ligne_id):
    ligne = next(
        (l for l in lignes if l["id"] == ligne_id),
        None
    )
    if ligne is None:
        return jsonify({"erreur": "Ligne non trouvee"}), 404
    return jsonify(ligne)


# ── Exercice 1 : GET /arrets  →  tous les arrêts sans doublons ───────────────
@app.route("/arrets")
def get_arrets():
    tous_arrets = set()
    for ligne in lignes:
        for arret in ligne["listeArrets"]:
            tous_arrets.add(arret)
    return jsonify(sorted(list(tous_arrets)))


# ── Exercice 2 : GET /stats  →  statistiques du réseau ──────────────────────
@app.route("/stats")
def get_stats():
    total_lignes = len(lignes)
    total_arrets = sum(l["arrets"] for l in lignes)
    ligne_max = max(lignes, key=lambda l: l["arrets"])
    return jsonify({
        "total_lignes": total_lignes,
        "total_arrets": total_arrets,
        "ligne_plus_arrets": {
            "numero": ligne_max["numero"],
            "arrets": ligne_max["arrets"]
        }
    })


# ── Exercice 3 : GET /lignes/recherche?q=Pikine  →  recherche par texte ──────
@app.route("/lignes/recherche")
def recherche_lignes():
    q = request.args.get("q", "").lower()
    if not q:
        return jsonify(lignes)
    resultats = [
        l for l in lignes
        if q in l["depart"].lower() or q in l["arrivee"].lower()
    ]
    return jsonify(resultats)


# ── Lancer le serveur ────────────────────────────────────────────────────────
if __name__ == "__main__":
    app.run(debug=True, port=5000)
