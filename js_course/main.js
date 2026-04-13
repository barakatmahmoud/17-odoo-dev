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


// Function
function calcAgeByDays(age){
    let result = age * 365;
    return result
}
let ageToDays = calcAgeByDays(28);
console.log(`Age By Days ${ageToDays}`);


function clacAgeByHours(age){
    let result = age * 24;
    return `Age By Hours ${result}`;
}
let ageToHours = clacAgeByHours(ageToDays);
console.log(ageToHours);
