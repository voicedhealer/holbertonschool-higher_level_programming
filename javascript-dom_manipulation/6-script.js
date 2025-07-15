#!/usr/bin/node
fetch('https://swapi-api.hbtn.io/api/people/5/?format=json')
  .then(response => response.json())
  .then(data => {
    document.getElementById('character').textContent = data.name;
  })
  .catch(error => {
    document.getElementById('character').textContent = 'Erreur de chargement';
    console.error(error);
  });
