// use Jquery
// $(document).ready(function (){
//     console.log("Hello Jquery!!");
// });

// jquery with events
// $(document).ready(function (){
//     $('button').click(function (){
//         $(this).hide();
//         }
//     )
//     }
//
// )

// jquery with effects
// 1- hide
// $(document).ready(function (){
//     $('button').click(function (){
//         $('p').hide();
//     })
// })

// 2- show
// $(document).ready(function (){
//     $('button').click(function (){
//         $('p').show();
//     })
// })

// 3- toggle
// $(document).ready(function (){
//     $('button').click(function (){
//         $('p').toggle();
//     })
// })

// use effects with toggle
// $(document).ready(function (){
//     $('button').click(function (){
//         $('p').toggle(function (){
//             $('span').toggle();
//         });
//     })
// })

// get and set text
// $(document).ready(function(){
//     var div = $('div').text();
//     $('p').text(div);
// })

// get and set html
// $(document).ready(function(){
//     var div = $('div').html();
//     $('p').text(div);
// })

// get and set val
// $(document).ready(function (){
//     $('button').click(function (){
//         $('input').val("Barakat");
//     })
// })

// check input is empty or not use val (check required field)
// $(document).ready(function (){
//     $('#check_btn').click(function (){
//         if ($('#name').val() == ''){
//             $('#name').text('You Must Enter Value');
//         }
//         else{
//             $('div').text('');
//         }
//     })
// })


// check input is empty or not use val (check required field) use append
// $(document).ready(function (){
//     $('#check_btn').click(function (){
//         if($('#name').val() == ''){
//             $('div').append("<span>You Must Enter Value</span>");
//         }
//         else{
//             $('span').hide();
//         }
//     })
// })

// get attr
// $(document).ready(function (){
//     $('button').click(function (){
//         $('input').val($('div').attr('class'));
//     })
// })

// set attr
// $(document).ready(function (){
//     $('button').click(function (){
//         $('div').attr('class', 'new_class');
//     })
// })

// remove
// $(document).ready(function (){
//     $('#check_btn').click(function (){
//         $('span').remove();
//     })
// })

// empty
// $(document).ready(function (){
//     $('#check_btn').click(function (){
//         $('div').empty();
//     })
// })

// add class, remove class , toggle class
// $(document).ready(function (){
//     $('button').click(function (){
//         $('span').addClass('Custom br').toggleClass('BB');
//     })
// })


// bind
// $('#check_btn').bind('click', function () {
//     console.log('clicked');
// });
//
// $('body').append('<button class="btn">New</button>');

// delegate
// $('div').delegate('#check_btn','click', function () {
//     console.log('clicked');
// });
// $('div').append('<button id="check_btn"">New</button>');

// on
// $('.custom').on('click', function (){
//     $(this).hide();
// })

// on with custom event
// $('.custom').on('customEvent', function (e, myHeight){
//     $(this).height(myHeight);
//     // $(this).hide();
// })

// $('button').click(function (){
//     $('.custom').trigger("customEvent", ["300px"]);
// })

// $('a').on('click', function (event){
//     event.preventDefault();
//     $(this).after("<p>HHHHHHHHHHHHHHHHHHHHHHH</p>");
// })

// change events
// $('input').on('change', function (){
//     $('div').after("<span>You change input</span>");
// })

// change with select
// $('select').on('change', function (){
//     $('div').after("<span>Your name is</span>" + $(this).val());
// })

// change with selection
// var selectedBefore = false
// $('#names').on('change', function (){
//     if(selectedBefore){
//         alert("You Select Name Before!");
//         return;
//     }
//     var selectName = $(this).val();
//     if(selectName !== ''){
//         $('#message').text('Your name is '+ selectName);
//         selectedBefore = true
//     }
// })

// sumit event
// $('#custom_form').submit(function (e){
//     if($('#user_name').val() === 'Confirm'){
//         $("span").text("Word is Ok!").show();
//         return;
//     }
//     else{
//         $("span").text("Word not Ok!!");
//         e.preventDefault();
//     }
// })

// prop >> return tree , false use with attribute
// $('button').on('click', function (){
//     console.log($('input').prop('disabled'));
// })

// prop >> to add new attribute to element
// $('button').on('click', function (){
//     console.log($('input').prop({
//         'disabled': false,
//         'name' : 'test',
//         'id': '#HH',
//     }));
// })

// each
// $('li').each(function (){
//     if($(this).hasClass('test')){
//         $(this).css('color', '#00F');
//     }
// })