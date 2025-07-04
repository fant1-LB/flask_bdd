
def appliquer_sql (df, liste_colonnes, db, nom_table):
    '''This function contains the SQL formula necessary to the insertion of a column in a database, if a new entry conflicts with a preexisting entry, it will be ignored.
     Remove the OR IGNORE statement in the SQL operation at the end of the function to change that '''
    from sqlalchemy import text
    liste_cles = str(liste_colonnes).replace("[","").replace(']','')
    liste_valeurs =[]
    # print(liste_colonnes)
    for z in liste_colonnes:
         valeur= df[f'{z}']
         liste_valeurs.append(str(valeur))
    valeurs=str(liste_valeurs).replace("[","").replace(']','')
    # print(liste_cles)
    # print(valeurs)
    with db.engine.begin() as connection:
        print("connexion réussie")
        connection.execute(text(f"INSERT OR IGNORE INTO {nom_table} ({liste_cles}) VALUES ({valeurs})"))
        
        

def add_to_database(csv, table, db):
    '''This function applies the previous function, in order to add the csv values, into a table in a definite database (db)'''
    import pandas as pd
    df = pd.read_csv(csv)
    liste_colonnes = df.columns.tolist()
    df.apply(appliquer_sql,args=( liste_colonnes, db, table), axis=1)
        

def mass_add_to_database(csv_list, tables, db):
    '''This function takes as entry a duet of lists, the first one of csv files, the second the tables in which they should be added, it then adds their datas to the db'''
    for i in range (0, len(csv_list)):
        add_to_database(csv_list[i],tables[i],db)
