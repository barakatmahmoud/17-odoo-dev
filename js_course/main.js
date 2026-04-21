// document >> HTML
// document.write('Hello World!');

// console >> Console
// console.log("Hello World!!");

// window >> Browser
// window.alert("Hello World!!!");

// Concatenation
// let name = 'Mahmoud';
// let age = 28;
// console.log(`My Name Is ${name} and my age is ${age}`);

// Calc Zakah
// let zakah = prompt("Enter Your Money");
// console.log(0.025 * zakah + "جنية");

// If statement
// let  age = prompt("Enter Your Age:")
// let result =  age > 18? console.log("Hello")
//     : age == 18? console.log("You are 18 now!!")
//         : console.log("You are Very young");


// switch statement
// let role = prompt("Enter Your Role:");
// switch (role.toLowerCase())
// {
//     case 'admin':
//         document.write("Create, Update, Delete");
//         break;
//     case 'editor':
//          document.write("Create, Update");
//          break;
//     default:
//         document.write("Hello Normal User");
// }


// Function convert age to days
// function calcAgeByDays(age){
//     let result = age * 365;
//     return result
// }
// let ageToDays = calcAgeByDays(28);
// console.log(`Age By Days ${ageToDays}`);
//
//
// function clacAgeByHours(age){
//     let result = age * 24;
//     return `Age By Hours ${result}`;
// }
// let ageToHours = clacAgeByHours(ageToDays);
// console.log(ageToHours);

// object in js
// let car = {
//     'name' : 'BMW',
//     'price': 50000,
//     'color': ['red', 'blue', 'green'],
//
//     hello:function (){
//         return 'Hello';
//     }
// }
// console.log(car.hello());


// this use with object
// let user = {
//     'name' : 'Mahmoud',
//
//     sayName : function (){
//         return this.name
//     }
// }
// console.log(user.sayName())

// this global >> window
// let x = this;
// console.log(this);

// this use with function >> window
// function hello(){
//     return this;
// }
// console.log(hello());

//// Dom

// get element by Id
// let headId = document.getElementById('head');
// console.log(headId);

// get element by ClassName >> return list
// let headClass = document.getElementsByClassName('header')[0];
// console.log(headClass);

// get element by TagName >> return list
// let headTag = document.getElementsByTagName('h3')[1];
// console.log(headTag)

// get element by query selector >> #id
// let headIdQuery = document.querySelector('#head');
// console.log(headIdQuery);

// get element by query selector >> .class >> return first class has this class
// let headClassQuery = document.querySelector('.header');
// console.log(headClassQuery);

// get element by query selector >> tag >> return first tag has this tag
// let headTagQuery = document.querySelector('h3');
// console.log(headTagQuery);

// get element by query selector all use with class and tag >> return list
// let headClassQueryAll = document.querySelectorAll('.header');
// console.log(headClassQueryAll);

// get html body
// let body = document.body;
// console.log(body);

// get html form
// let form = document.forms;
// console.log(form);


// element = document.getElementById('head');
// get previous element
// console.log(element.previousElementSibling);
// get previous
// console.log(element.previousSibling);
// get parent
// console.log(element.parentElement);


// element = document.getElementById('container');
// inner html
// element.innerHTML = '<h3>Hello By Js</h3>';
// outer html
// element.outerHTML = '<h3>Hello By Js</h3>';
// inner text
// element.innerText = "Hello Jsss";
// outer text
// element.outerText = "Hello Jsss";
