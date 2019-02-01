window.Superlists = {};
window.Superlists.initialize = function () {
  $('input[name="text"]').on('keyup', function () {
    $('.has-error').hide();
  });
};