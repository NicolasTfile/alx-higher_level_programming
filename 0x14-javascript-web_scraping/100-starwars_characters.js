#!/usr/bin/node

const request = require('request');
const id = process.argv[2];
const url = 'https://swapi-api.hbtn.io/api/films/';
request.get(url + id, function (error, response, body) {
  if (error) {
    console.error(error);
  }
  const data = JSON.parse(body);
  const characterUrls = data.characters;
  for (const i of characterUrls) {
    request.get(i, function (error, response, body) {
      if (error) {
        console.error(error);
      }
      const data = JSON.parse(body);
      console.log(data.name);
    });
  }
});
