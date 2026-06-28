import pandas as pd
import matplotlib.pyplot as plt
import os

df = pd.read_csv(r"D:\NETFLIX  DATA ANYLYSIS\netflix_titles.csv")

# print(df)
# print(df.head())
# print(df.shape)
# print(df.columns)
# print(df.describe())
# print(df.info())



# print("\nMovies and TV shows Count:")
# print(df['type'].value_counts())

# df['type'].value_counts().plot(kind='bar')

# plt.title("Movies vs TV Shows")
# plt.xlabel("Type")
# plt.ylabel("Count")
# os.makedirs("charts", exist_ok=True)
# plt.savefig("charts/bar_chart(movies & shows Count).png")
# plt.show()



# top_countries = df['country'].value_counts().head(10)
# print(top_countries)
# top_countries.plot(kind='bar')

# plt.title("Top 10 Countries")
# plt.xlabel("Counttries")
# plt.ylabel("Number of Titles")
# plt.savefig("charts/bar_chart(Top 10 Countries).png")
# plt.show()



# df['date_added'] = pd.to_datetime(df['date_added'], errors='coerce')
# df['years_added'] = df['date_added'].dt.year
# content_year = df['years_added'].value_counts().sort_index()

# print("content added over the years:")
# print(content_year)

# content_year.plot(kind='line',marker='o')

# plt.title("Content Added Over the Years")
# plt.xlabel("Year")
# plt.ylabel("Number Of Titles")
# plt.grid(True)
# plt.savefig("charts/line_chart(titles over the years).png")

# plt.show()



# top_genres = df["listed_in"].value_counts().head(10)
# print(top_genres)

# top_genres.plot(kind='bar')

# plt.title("Top Genres")
# plt.xlabel("Genre")
# plt.ylabel("Number of Titles")
# plt.xticks(rotation=45)
# plt.savefig("charts/bar_chart(Top Generes).png")

# plt.show()



# rating = df["rating"].value_counts()
# print(rating)

# rating.plot(kind='bar')

# plt.title("Rating Distribution")
# plt.xlabel("Rating")
# plt.ylabel("NUmber of Titles")
# plt.xticks(rotation=45)
# plt.savefig("charts/bar_chart(Rating Distribution).png")

# plt.show()



movies = df[df['type'] == 'Movie']

print(movies['duration'].head())

movies_duration = movies['duration'].value_counts().head(10)
print(movies_duration)

movies_duration.plot(kind='bar')

plt.title("Top 10 Movie Durations")
plt.xlabel("Duration")
plt.ylabel("Count")
plt.xticks(rotation=45)
plt.savefig("charts/bar_chart(Movie Duration).png")

plt.show()