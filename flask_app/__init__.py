from flask import Flask
DATABASE = "upkeep_schema"
app = Flask(__name__)
app.secret_key = "secretsecret"