import logging
import azure.functions as func
import mysql.connector
import json

config = {
  'host':'duncangrille.mysql.database.azure.com',
  'user':'grille_admin',
  'password':'Dubbuff$5',
  'database':'duncan_grille',
  'client_flags': [mysql.connector.ClientFlag.SSL],
  'ssl_ca': 'cert.pem'
}


def main(event: func.EventGridEvent):
    logging.info('even grid processed')
    # Connect to MySQL