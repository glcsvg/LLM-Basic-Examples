import pandas as pd
from sqlalchemy import create_engine, MetaData,  Table, select

# # 1. CSV dosyasını okumak
# csv_file = 'spotify.csv'
# df = pd.read_csv(csv_file, index_col=0)

# # 2. Veritabanı bağlantısı kurmak (SQLite kullanarak)
# engine = create_engine('sqlite:///Spotify.db')

# # 3. CSV verilerini veritabanına yazmak
# table_name = 'musics'
# df.to_sql(table_name, engine, index=False, if_exists='replace')

# print("CSV verileri veritabanına başarıyla yazıldı.")

#engine = db.create_engine('dialect+driver://user:pass@host:port/db')

engine = create_engine('sqlite:///Spotify.db')
connection = engine.connect()
metadata = MetaData()
musics = Table('musics', metadata, autoload_with=engine)

query =  select(musics).where(musics.c.artists == 'Ben Woodward')

result = connection.execute(query)

# Sonuçları yazdırmak
for row in result:
    print(row)
