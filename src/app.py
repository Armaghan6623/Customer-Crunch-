from flask import Flask

from src.app.routes import routes_bp

app = Flask(__name__)
app.register_blueprint(routes_bp)


if __name__ == "__main__":
    # Local dev only
    app.run(host="0.0.0.0", port=7860, debug=True)




