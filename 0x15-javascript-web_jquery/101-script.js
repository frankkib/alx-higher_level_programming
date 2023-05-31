$(document).ready(function () {
  $('#add_item').click(function () {
    const newElement = $('<li>').text('Item');
    $('ul.my_list').append(newElement);
  });

  $('#remove_item').click(function () {
    $('ul.my_list li:last-child').remove();
  });

  $('#clear_list').click(function () {
    $('ul.my_list').empty();
  });
});
