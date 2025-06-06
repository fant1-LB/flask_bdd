def appliquer_sql (df, liste_colonnes, db, nom_table):
    from sqlalchemy import text
    liste_cles = str(liste_colonnes).replace("[","").replace(']','')
    liste_valeurs =[]
    print(liste_colonnes)
    for z in liste_colonnes:
         valeur= df[f'{z}']
         liste_valeurs.append(str(valeur))
    valeurs=str(liste_valeurs).replace("[","").replace(']','')
    print(liste_cles)
    print(valeurs)
    with db.engine.connect() as connection:
                    connection.execute(text(f"INSERT INTO {nom_table} ({liste_cles}) VALUES ({valeurs})"))


def add_to_database(x, table, db):
    import pandas as pd
    df = pd.read_csv(x)
    liste_colonnes = df.columns.tolist()
    df.apply(appliquer_sql,args=( liste_colonnes, db, table), axis=1)
        
