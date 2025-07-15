#!/usr/bin/node
fetch('https://swapi-api.hbtn.io/api/films/?format=json')
  .then(response => response.json())
  .then(data => {
    const list = document.getElementById('list_movies');
    data.results.forEach(film => {
      const item = document.createElement('li');
      item.textContent = film.title;
      list.appendChild(item);
    });
  })
  .catch(error => {
    console.error('Erreur lors de la récupération des films :', error);
  });
