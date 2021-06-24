// Boolean
let isDone: boolean = false;

// Number
let decimal: number = 6; // 10진수
let hex: number = 0xf00d; // 16진수
let binary: number = 0b1010; // 2진수
let octal: number = 0o744; // 8진수

// String
let color: string = "blue";
color = 'red';

let fullName: string = `Bob Bobbington`;
let age: number = 37;
let sentence: string = `Hello, my name is ${ fullName }.
I'll be ${ age + 1 } years old next month.`; // 백쿼크(`)를 이용해서 ${} 가능
// let sentence: string = "Hello, my name is " + fullName + ".\n\n" +
//     "I'll be " + (age + 1) + " years old next month."; // 같은 내용임.

// Array
let list: number[] = [1, 2, 3];
let lst: Array<number> = [1, 2, 3]; // 두가지 방법 모두 가능

// Tuple
let x: [string, number];
x = ["hello", 10];
console.log(x[0].substring(1));
// console.log(x[1].substring(1)); // error x[1]은 number!
// x[3] = "world"; // x[3]은 let x: [string, number] 여기서 정의되지 않았음.
// console.log(x[5].toString()); // x[5]도 없음
let asdf = [1,2,3,4]
asdf[5] = 123
console.log(x[0])

// Enum(열거)
enum Color {Red = 1, Green, Blue}
let colorName: string = Color[2];

console.log(colorName);

// Any
let notSure: any = 4;
notSure = "maybe a string instead";
notSure = false; 

let anylist: any[] = [1, true, "free"];

anylist[1] = 100;

// Void (Any와 반대)
function warnUser(): void {
  console.log("This is my warning message");
}
let unusable: void = undefined;
// unusable = null; // 성공

// null & undefined
let u: undefined = undefined;
let n: null = null;

// Never
function error(message: string): never {
  throw new Error(message);
}

function fail() {
  return error("Something failed");
}

function infiniteLoop(): never {
  while (true) {
  }
}

// object
declare function create(o: object | null): void;

create({ prop: 0 }); // 성공
create(null); // 성공

// create(42); // 오류
// create("string"); // 오류
// create(false); // 오류
// create(undefined); // 오류

// 타입 단언 (Type assertions)
// let someValue: any = "this is a string";
// let strLength: number = (<string>someValue).length;
let someValue: any = "this is a string";
let strLength: number = (someValue as string).length; // 같은 내용이지만 아래로 사용

