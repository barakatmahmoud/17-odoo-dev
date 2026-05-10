// primitive data type (string, number, boolean, undefined, null)
// non-primitive data type (object, function, array)

// object data type
// var car = {
//     brand : 'Toyota',
//     price : 100000,
//     model : '2020'
// }
// to access element
// console.log(car['brand']);
// console.log(car.brand);

// function data type (1- void function , 2- returning function)
// 1- void function
// function hello(){
//     console.log('Hello');
// }
// hello();
// *another way
// hello = function (){
//     console.log('Hello');
// }
// hello();

// 2- returning function
// function addNum(x, y){
//     return x + y;
// }
// console.log(addNum(3,4));

// array
// var emps = ['ali', 'sayed', 'mahmoud'];
// console.log(emps);

// *another way
// emps = new Array(2);
// console.log(emps);
// emps[0] = 'Ali';
// console.log(emps);

// flow control 1-[(conditional statement) *if else *switch ,, (exception handling) *throw *try , catch, finally]
// if else
// var name = 'Ali'
// if(name == 'Ali'){
//     console.log('Name Equal Ali');
// }
// else if(name == 'Ahmed'){
//     console.log('Name Equal Ahmed');
// }
// else{
//     console.log('Name Not Equal Ahmed or Ali');
// }

// switch
// var name = 'Ali';
// switch (name){
//     case 'Ali':
//         {console.log('Hello Ali')}
//         break;
//     case 'Ahmed':
//         {console.log('Hello Ahmed')}
//         break;
//     default:
//         {console.log('Name Not Ahmed or Ali')}
//         break;
// }

// try, catch, finally
// var x = 'ahmed';
// try{
//     console.log(`My name is ${name} and age is ${age}`);
// }
// catch (error){
//     console.log("You can't Concatenation", error.message);
// }


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

// use it to call this function in html, and use as external function
// function hello(){
//     console.log('Hello');
// }

// let btn = document.getElementById('btn');
// first way to use event
// btn.onclick = function (){
//     console.log("Clicked!!!!");
// }

// second way to use event call external function
// btn.onclick = hello;

// addEventListener
// btn.addEventListener('click', function (){
//     console.log("Clicked by AddEventListener!!");
// })


// difference between onclick , addEventListener
// btn.onclick = function (){
//     console.log("firest!!!!");
// }
// // only second will execute
// btn.onclick = function (){
//     console.log("second!!!!");
// }

// when use addEventListener first function and second function will execute
// btn.addEventListener('click', function (){
//     console.log("First!!!");
// })
//
// btn.addEventListener('click', function (){
//     console.log("Second!!!");
// })

// event with mouse
// btn.addEventListener("click", () => console.log("Clicked!!"));
// btn.addEventListener("dblclick", () => console.log("DblClicked!!"));
// btn.addEventListener("mouseover", () => console.log("MouseOver!!"));

// event with keyboard
// input = document.getElementById('input')
// input.addEventListener("keydown", (e) => {
//   console.log(e.key);
//   console.log(e.code);
//   console.log(e.ctrlKey);
// });

// event object
// btn.addEventListener("click", function (event) {
//   console.log('Event : ',event);
//   console.log('Event Target : ',event.target);
// });

// check value in input
// var nameInput = document.getElementById('name');
// var submitBtn = document.getElementById('submit');
// submitBtn.addEventListener('click', function (ev){
//     ev.preventDefault();
//     console.log("Name:", nameInput.value);
//     if(!nameInput.value){
//         alert("Enter Name.");
//     }
//     else{
//         console.log('Okay');
//     }
// })


//  e.preventDefault(); >> use to block default behavior
// document.getElementById("myForm").addEventListener("submit", function (e) {
//       e.preventDefault();
//       console.log("Form prevented");
// });

// Program to convert dollar to pound
// var dollar = document.getElementById('dollar');
// var pound = document.getElementById('pound');
// dollar.onkeyup = function (){
//     pound.value = dollar.value * 50;
// }
// pound.onkeyup = function (){
//     dollar.value = pound.value / 50;
// }


//after , before, inside
// let after = document.getElementById('after');
// let before = document.getElementById('before');
// let inside = document.getElementById('inside');
// let content = document.getElementById('content');
// let container = document.getElementById('container');
//
// container.style.background = '#ffa';
// container.style.height = '50px';
//
// after.onclick = function (){
//     container.after(content);
// }
// before.onclick = function (){
//     container.before(content);
// }
// inside.onclick = function (){
//     container.append(content);
// }


//toggle >> add and remove class
// let hello = document.getElementById('hello');
// hello.onclick = function (){
//     hello.classList.toggle('name');
// }

// setTimeout , clearTimeout >> Execution for one time
// let hello = setTimeout(function (){
//     console.log('Hello');
// },2000)
//
// clearTimeout(hello);

// setInternal , clearInternal >>  Execution for many time
// let i = 0;
// let hello = setInterval(function(){
//     console.log(i++);
//     if(i == 4){
//         clearInterval(hello);
//     }
// }, 3000)