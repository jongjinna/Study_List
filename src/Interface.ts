// // function printLabel(labeledObj: { label: string }) {
// //   console.log(labeledObj.label);
// // }
// // let myObj = {size: 10, label: "Size 10 Object"};
// // printLabel(myObj);

// interface LabeledValue {
//   label: string;
// }
// function printLabel(labeledObj: LabeledValue) {
//   console.log(labeledObj.label);
// }
// let myObj = {size: 10, label: "Size 10 Object"};
// printLabel(myObj); 

// // 선택적 프로퍼티
// // interface SquareConfig {
// //   color?: string;
// //   width?: number;
// // }
// function createSquare(config: SquareConfig): {color: string; area: number} {
//   let newSquare = {color: "white", area: 100};
//   if (config.color) {
//       newSquare.color = config.color;
//   }
//   if (config.width) {
//       newSquare.area = config.width * config.width;
//   }
//   return newSquare;
// }
// // let mySquare = createSquare({color: "black"});

// // 읽기전용 프로퍼티
// interface Point {
//   readonly x: number;
//   readonly y: number;
// }
// let p1: Point = { x: 10, y: 20 };
// // p1.x = 5; // 오류!
// let a: number[] = [1, 2, 3, 4];
// let ro: ReadonlyArray<number> = a;
// // ro[0] = 12; // 오류!
// // ro.push(5); // 오류!
// // ro.length = 100; // 오류!
// // a = ro; // 오류!
// a = ro as number[];

// // 초과 프로퍼티 검사
// interface SquareConfig {
//   color?: string;
//   width?: number;
//   [propName: string]: any; // 검사를 피하기 위한 any 사용을 지양
// } 
// // let mySquare = createSquare({ width: 100, opacity: 0.5 } as SquareConfig);
// let squareOptions = { colour: "red", width: 100 };
// let mySquare = createSquare(squareOptions);

// // 함수 타입
// interface SearchFunc {
//   (source: string, subString: string): boolean;
// }
// let mySearch: SearchFunc;
// mySearch = function(src, sub) {
//     let result = src.search(sub);
//     return result > -1;
// }

// // 인덱서블 타입
// interface StringArray {
//   [index: number]: string;
// }
// let myArray: StringArray;
// myArray = ["Bob", "Fred"];
// let myStr: string = myArray[0];

// class Animal {
//   name: string;
// }
// class Dog extends Animal {
//   breed: string;
// }

// // 오류: 숫자형 문자열로 인덱싱을 하면 완전히 다른 타입의 Animal을 얻게 될 것입니다!
// interface NotOkay {
//   [x: number]: Animal;
//   [x: string]: Dog;
// }
// interface NumberOrStringDictionary {
//   [index: string]: number | string;
//   length: number;    // 성공, length는 숫자입니다
//   name: string;      // 성공, name은 문자열입니다
// }
// interface ReadonlyStringArray {
//   readonly [index: number]: string;
// }
// let myArray: ReadonlyStringArray = ["Alice", "Bob"];
// myArray[2] = "Mallory"; // 오류!

// 클래스 타입
// interface ClockInterface {
//   currentTime: Date;
//   setTime(d: Date): void;
// }

// class Clock implements ClockInterface {
//   currentTime: Date = new Date();
//   setTime(d: Date) {
//       this.currentTime = d;
//   }
//   constructor(h: number, m: number) { }
// }

// interface ClockConstructor {
//   new (hour: number, minute: number): ClockInterface;
// }
// interface ClockInterface {
//   tick(): void;
// }

// function createClock(ctor: ClockConstructor, hour: number, minute: number): ClockInterface {
//   return new ctor(hour, minute);
// }

// class DigitalClock implements ClockInterface {
//   constructor(h: number, m: number) { }
//   tick() {
//       console.log("beep beep");
//   }
// }
// class AnalogClock implements ClockInterface {
//   constructor(h: number, m: number) { }
//   tick() {
//       console.log("tick tock");
//   }
// }

// let digital = createClock(DigitalClock, 12, 17);
// let analog = createClock(AnalogClock, 7, 32);

// interface ClockConstructor {
//   new (hour: number, minute: number);
// }

// interface ClockInterface {
//   tick();
// }

// const Clock: ClockConstructor = class Clock implements ClockInterface {
//   constructor(h: number, m: number) {}
//   tick() {
//       console.log("beep beep");
//   }
// }