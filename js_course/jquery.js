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
//             $('div').text('You Must Enter Value');
//         }
//         else{
//             $('div').text('');
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