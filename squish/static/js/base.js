/**
 * Created by danielsiker on 10/4/14.
 */
$(document).ready( function () {
//   $('#register').click(function() {
//       $('#registerBlock').toggle('fast')
//   })
//});

  $('#register').on('click', function () {
   $.ajax({
       url: '/register/',
       type: 'GET',
       success: function (data) {
           $('#registerBlock').html(data);
            }
//       error: function(request, data) {
//           alert(request.responseText)
//       }
        });
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
              console.log(data);
            }
        });
    });
});













//    $('#login').click(function(){
//        $('#loginBlock').toggle('fast')
//    })




//        $('form').append('<button>'+"Subscribe"+'</button>')
//
//
//        $('form').submit(function(e){
//            e.preventDefault();
//            var form=$(e.target);
//
//            $.ajax({
//                url: '{% profile.html %}',
//                type: 'post',
//                data: account_form.serialize() + '&' + form.serialize(),
//                error: function(xhr, ajaxOptions, thrownError){ alert(thrownError); },
//                success: function(){}
//            })
//        });
