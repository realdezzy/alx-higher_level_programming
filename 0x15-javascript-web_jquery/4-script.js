$(function () {
  $('DIV#toggle_header').bind('click', function () {
    const curAttr = $('header').attr('class');
    if (curAttr == 'red') {
      $('header').attr('class', 'green');
    } else {
      $('header').attr('class', 'red');
    }
  });
});
