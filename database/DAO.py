from database.DB_connect import DBConnect
#from model.situazione import Situazione


class MeteoDao():

    @staticmethod
    def get_umidita_media_mese(mese):
        cnx = DBConnect.get_connection()
        result = []
        if cnx is None:
            print("Connessione fallita")
        else:
            cursor = cnx.cursor(dictionary=True)
            query = """select s.Localita, sum(s.Umidita )/count(s.Umidita) as media
                        from situazione s 
                        where month(data)=%s
                        group by s.Localita """
            cursor.execute(query,(mese,))
            for row in cursor:
                #restituisco una lista di tuple
                result.append((row["Localita"], row['media']))
            cursor.close()
            cnx.close()
        return result

