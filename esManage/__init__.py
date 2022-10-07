from flask import Flask
import sys
import os
app = Flask(__name__)
import esManage.main

from esManage import db
db.create_books_table()