"use strict";
// Boolean
var isDone = false;
// Number
var decimal = 6; // 10진수
var hex = 0xf00d; // 16진수
var binary = 10; // 2진수
var octal = 484; // 8진수
// String
var color = "blue";
color = 'red';
var fullName = "Bob Bobbington";
var age = 37;
var sentence = "Hello, my name is " + fullName + ".\nI'll be " + (age + 1) + " years old next month."; // 백쿼크(`)를 이용해서 ${} 가능
// let sentence: string = "Hello, my name is " + fullName + ".\n\n" +
//     "I'll be " + (age + 1) + " years old next month."; // 같은 내용임.
// Array
var list = [1, 2, 3];
var lst = [1, 2, 3]; // 두가지 방법 모두 가능
// Tuple
var x;
x = ["hello", 10];
console.log(x[0].substring(1));
// console.log(x[1].substring(1)); // error x[1]은 number!
// x[3] = "world"; // x[3]은 let x: [string, number] 여기서 정의되지 않았음.
// console.log(x[5].toString()); // x[5]도 없음
var asdf = [1, 2, 3, 4];
asdf[5] = 123;
console.log(x[0]);
// Enum(열거)
var Color;
(function (Color) {
    Color[Color["Red"] = 1] = "Red";
    Color[Color["Green"] = 2] = "Green";
    Color[Color["Blue"] = 3] = "Blue";
})(Color || (Color = {}));
var colorName = Color[2];
console.log(colorName);
// Any
var notSure = 4;
notSure = "maybe a string instead";
notSure = false;
var anylist = [1, true, "free"];
anylist[1] = 100;
// Void (Any와 반대)
function warnUser() {
    console.log("This is my warning message");
}
var unusable = undefined;
// unusable = null; // 성공
// null & undefined
var u = undefined;
var n = null;
// Never
function error(message) {
    throw new Error(message);
}
function fail() {
    return error("Something failed");
}
function infiniteLoop() {
    while (true) {
    }
}
create({ prop: 0 }); // 성공
create(null); // 성공
// create(42); // 오류
// create("string"); // 오류
// create(false); // 오류
// create(undefined); // 오류
// 타입 단언 (Type assertions)
// let someValue: any = "this is a string";
// let strLength: number = (<string>someValue).length;
var someValue = "this is a string";
var strLength = someValue.length; // 같은 내용이지만 아래로 사용
