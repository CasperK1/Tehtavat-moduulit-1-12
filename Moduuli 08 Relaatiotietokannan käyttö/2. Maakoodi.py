def yhteys():
    import mysql.connector
    yk = mysql.connector.connect(
        host='127.0.0.1',
        port=3306,
        database='flight_game',
        user='root',
        password='root',
        autocommit=True)
    # Yhteystesti, yhdistetyn tietokannan nimi, kursorin ja tietokannan palautus pääohjelmaan
    if yk.is_connected():
        print(f'Yhdistetty tietokantaan: {yk.database}\n')
        kursori = yk.cursor()
        return yk, kursori


def kentat(maakoodi):
    tulos = []
    yk, kursori = yhteys()

    sql = (f"SELECT type, COUNT(*) FROM airport "
           f"WHERE airport.iso_country = '{maakoodi}' "
           f"GROUP BY type")
    kursori.execute(sql)
    tulos = kursori.fetchall()
    return tulos


kenttatyypit = {
    'closed': 'Suljettuja kenttiä',
    'balloonport': 'Kuumailmapallokenttiä',
    'heliport': 'Helikopterikenttiä',
    'large_airport': 'Isoja lentokenttiä',
    'medium_airport': 'Keskikokoisia kenttiä',
    'seaplane_base': 'Vesitasokenttiä',
    'small_airport': 'Pieniä kenttiä'
}

maakoodi = input('Syötä 2-kirjaiminen maakoodi: ').upper()
tulos = kentat(maakoodi)

if not tulos:
    print(f'Maakoodia {maakoodi} ei ole olemassa')
else:
    print(f'Maassa {maakoodi} on:\n')
    for kentta, tulos in tulos:
        if kentta in kenttatyypit:
            print(f'{kenttatyypit[kentta]}: {tulos} kpl')











# i = 0
# print(f'Maassa {maakoodi} on:\n')
# for _ in tulos:
#     if tulos[i][0] == 'closed':
#         print(f'Suljettuja kenttiä {tulos[i][1]} kpl')
#         i += 1
#     elif tulos[i][0] == 'balloonport':
#         print(f'Kuumailmapallokenttiä {tulos[i][1]} kpl')
#         i += 1
#     elif tulos[i][0] == 'heliport':
#         print(f'Helikopterikenttiä {tulos[i][1]} kpl')
#         i += 1
#     elif tulos[i][0] == 'large_airport':
#         print(f'Isoja lentokenttiä {tulos[i][1]} kpl')
#         i += 1
#     elif tulos[i][0] == 'medium_airport':
#         print(f'Keskikokoisia kenttiä {tulos[i][1]} kpl')
#         i += 1
#     elif tulos[i][0] == 'seaplane_base':
#         print(f'Vesitasokenttiä {tulos[i][1]} kpl')
#         i += 1
#     elif tulos[i][0] == 'small_airport':
#         print(f'Pieniä kenttiä {tulos[i][1]} kpl')
#         i += 1
#     else:
#         i += 1
