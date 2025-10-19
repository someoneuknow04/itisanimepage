import requests
import os
from jinja2 import Template

# Create anime folder if not exists
if not os.path.exists("anime"):
    os.makedirs("anime")

# Fetch top 10 anime
url = "https://api.jikan.moe/v4/top/anime"
res = requests.get(url).json()
anime_list = res['data'][:10]

# Index page template
index_template = Template("""
<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<title>It is Anime Page</title>
<link rel="stylesheet" href="styles.css">
</head>
<body>
<header>
<h1>It is Anime Page</h1>
<nav>
<a href="#top-anime">Top Anime</a>
<a href="#affiliate">Support Me</a>
</nav>
</header>
<main>
<section id="top-anime">
<h2>Top Anime Right Now</h2>
<div>
{% for anime in anime_list %}
<div class="anime-card">
<img src="{{ anime.images.jpg.image_url }}" alt="{{ anime.title }}">
<h3>{{ anime.title }}</h3>
<p>Score: {{ anime.score }}</p>
<a href="anime/{{ anime.mal_id }}.html">Read More</a>
</div>
{% endfor %}
</div>
</section>
<section id="affiliate">
<h2>Support This Site</h2>
<p><a href="https://www.buymeacoffee.com/">Buy Me a Coffee</a></p>
<p><a href="YOUR-AFFILIATE-LINK">Shop Anime Merch</a></p>
</section>
</main>
<footer>
&copy; 2025 It is Anime Page
</footer>
</body>
</html>
""")

# Generate index.html
with open("index.html", "w", encoding="utf-8") as f:
    f.write(index_template.render(anime_list=anime_list))

# Anime page template
anime_template = Template("""
<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<title>{{ anime.title }}</title>
<link rel="stylesheet" href="../styles.css">
</head>
<body>
<header>
<h1>{{ anime.title }}</h1>
<a href="../index.html">← Back to Home</a>
</header>
<main>
<img src="{{ anime.images.jpg.image_url }}" alt="{{ anime.title }}">
<p><strong>Score:</strong> {{ anime.score }}</p>
<p><strong>Episodes:</strong> {{ anime.episodes }}</p>
<p><strong>Type:</strong> {{ anime.type }}</p>
<p><strong>Synopsis:</strong> {{ anime.synopsis }}</p>
<p><a href="{{ anime.url }}" target="_blank">Official MyAnimeList Page</a></p>
</main>
<footer>
&copy; 2025 It is Anime Page
</footer>
</body>
</html>
""")

# Generate individual anime pages
for anime in anime_list:
    filename = f"anime/{anime['mal_id']}.html"
    with open(filename, "w", encoding="utf-8") as f:
        f.write(anime_template.render(anime=anime))
