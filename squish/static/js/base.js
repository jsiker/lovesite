/**
 * Created by danielsiker on 10/4/14.
 */
$(document).ready( function () {
      $('#register').on('click', function () {
       $.ajax({
           url: '/register/',
           type: 'GET',
           success: function (data) {
               $('#registerBlock').html(data);

           }
       });
        $('form').append('<button>'+"Subscribe"+'</button>')
   });

          $('#pay').on('click', function () {
       $.ajax({
           url: '/payments/',
           type: 'GET',
           success: function (data) {
               $('#payBlock').html(data);

           }
       });
   });
              $('#login').on('click', function () {
       $.ajax({
           url: '/login/',
           type: 'GET',
           success: function (data) {
               $('#loginBlock').html(data);

           }
       });
   });
});