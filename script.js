const animeList = document.getElementById('anime-list');

fetch('https://api.jikan.moe/v4/top/anime')
    .then(response => response.json())
    .then(data => {
        data.data.slice(0,10).forEach(anime => {  // top 10 anime
            const card = document.createElement('div');
            card.className = 'anime-card';
            card.innerHTML = `
                <img src="${anime.images.jpg.image_url}" alt="${anime.title}">
                <h3>${anime.title}</h3>
                <p>Score: ${anime.score}</p>
                <a href="${anime.url}" target="_blank">Read More</a>
            `;
            animeList.appendChild(card);
        });
    })
    .catch(err => {
        animeList.innerHTML = '<p>Failed to load anime data. Try again later.</p>';
        console.error(err);
    });
