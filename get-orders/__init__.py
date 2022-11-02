import logging
import azure.functions as func
import mysql.connector

config = {
  'host':'duncangrille.mysql.database.azure.com',
  'user':'grille_admin',
  'password':'Dubbuff$5',
  'database':'duncan_grille',
  'client_flags': [mysql.connector.ClientFlag.SSL],
  'ssl_ca': 'cert.pem'
}

def main(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')
    # Connect to MySQL
    try:
        logging.info(req.get_json()['sql'])
        q = req.get_json()['sql']
    except:
        logging.info("No json data")
    cnx = mysql.connector.connect(**config  
    )
    logging.info(cnx)
    # Show databases
    cursor = cnx.cursor()
    cursor.execute(q)
    result_list = cursor.fetchall()
    # Build result response text
    result_str_list = []
    for row in result_list:
        row_str = ', '.join([str(v) for v in row])
        result_str_list.append(row_str)
    result_str = '\n'.join(result_str_list)
    return func.HttpResponse(
        result_str,
        status_code=200
    )