import sqlite3

def leer_datos():
  conn = sqlite3.connect("censo.db")
  cursor