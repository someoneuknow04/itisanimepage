const newsDiv = document.getElementById('news');
fetch('https://api.jikan.moe/v4/top/anime')  // free anime API
    .then(response => response.json())
    .then(data => {
        data.data.slice(0,5).forEach(anime => {
            const div = document.createElement('div');
            div.innerHTML = `<h3>${anime.title}</h3><img src="${anime.images.jpg.image_url}" width="200"><p>Score: ${anime.score}</p>`;
            newsDiv.appendChild(div);
        });
    });
