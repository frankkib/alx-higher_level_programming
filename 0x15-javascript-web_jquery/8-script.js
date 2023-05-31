$.getJSON('https://swapi-api.alx-tools.com/api/films/?format=json', function (data) {
  const movies = data.results;
  $.each(movies, function (index, movie) {
    $('<li>').text(movie.title).appendTo('#list_movies');
  });
});
