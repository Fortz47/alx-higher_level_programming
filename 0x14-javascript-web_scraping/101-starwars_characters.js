#!/usr/bin/node

const request = require('request');

const getCharacterDetails = async (characterUrl) => {
  return new Promise((resolve, reject) => {
    request(characterUrl, (error, response, body) => {
      if (!error && response.statusCode === 200) {
        const character = JSON.parse(body);
        resolve(character.name);
      } else {
        reject(error);
      }
    });
  });
};

const getMovieDetails = async (movieId) => {
  return new Promise((resolve, reject) => {
    const apiUrl = `https://swapi-api.alx-tools.com/api/films/${movieId}`;
    request(apiUrl, (error, response, body) => {
      if (!error && response.statusCode === 200) {
        const film = JSON.parse(body);
        resolve(film.characters);
      } else {
        reject(error);
      }
    });
  });
};

const printCharacterNames = async (movieId) => {
  try {
    const characterUrls = await getMovieDetails(movieId);

    for (const characterUrl of characterUrls) {
      const characterName = await getCharacterDetails(characterUrl);
      console.log(characterName);
    }
  } catch (error) {
    console.error(error);
  }
};

const movieId = process.argv[2];
printCharacterNames(movieId);
