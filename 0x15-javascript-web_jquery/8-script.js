$.get('https://swapi-api.alx-tools.com/api/films/?format=json', function (data) {
  const movies = data.results;
  const ulElement = $('#list_movies');

  $.each(movies, function (index, movie) {
    const title = movie.title;
    const liElement = $('<li>').text(title);
    ulElement.append(liElement);
  });
});
