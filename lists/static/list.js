window.Superlists = {};
window.Superlists.initialize = function () {
  console.log('initializing javascript')
  $('input[name="text"]').on('keyup', function () {
    console.log('in keyup javascript')
    $('.has-error').hide();
    console.log('finished keyup javascript')
  });
  $('input[name="text"]').on('click', function () {
    console.log('in click javascript')
    $('.has-error').hide();
    console.log('finished click javascript')
  });
};