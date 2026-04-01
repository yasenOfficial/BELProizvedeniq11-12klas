from flask import Flask, render_template
from data import WORKS, ERA_COLORS, CONNECTIONS

app = Flask(__name__)
app.jinja_env.globals["enumerate"] = enumerate

WORK_BY_ID = {w["id"]: w for w in WORKS}

CONN_MAP = {}
for c in CONNECTIONS:
    CONN_MAP[(c["from_id"], c["to_id"])] = c
    CONN_MAP[(c["to_id"], c["from_id"])] = c


@app.route("/")
def index():
    grid = []
    for w in WORKS:
        row = []
        for other in WORKS:
            if w["id"] == other["id"]:
                row.append(None)
            else:
                row.append(CONN_MAP.get((w["id"], other["id"])))
        grid.append(row)

    return render_template(
        "matrix.html",
        works=WORKS,
        grid=grid,
        era_colors=ERA_COLORS,
    )


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0")
