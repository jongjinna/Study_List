// enum Direction {
//   Up = 1,
//   Down,
//   Left,
//   Right,
// }

// enum Direction {
//   Up,
//   Down,
//   Left,
//   Right,
// }

// enum Response {
//   No = 0,
//   Yes = 1,
// }

// function respond(recipient: string, message: Response): void {
//   // ...
// }

// respond("Princess Caroline", Response.Yes)

// enum E {
//   A = getSomeValue(),
//   B, // 오류! 앞에 나온 A가 계산된 멤버이므로 초기화가 필요합니다.
// }

// enum Direction {
//   Up = "UP",
//   Down = "DOWN",
//   Left = "LEFT",
//   Right = "RIGHT",
// }

// enum BooleanLikeHeterogeneousEnum {
//   No = 0,
//   Yes = "YES",
// }

// // E.X는 상수입니다:
// enum E { X }

// // 'E1' 과 'E2' 의 모든 열거형 멤버는 상수입니다.

// enum E1 { X, Y, Z }

// enum E2 {
//     A = 1, B, C
// }

// enum FileAccess {
//   // 상수 멤버
//   None,
//   Read    = 1 << 1,
//   Write   = 1 << 2,
//   ReadWrite  = Read | Write,
//   // 계산된 멤버
//   G = "123".length
// }

// enum ShapeKind {
//   Circle,
//   Square,
// }

// interface Circle {
//   kind: ShapeKind.Circle;
//   radius: number;
// }

// interface Square {
//   kind: ShapeKind.Square;
//   sideLength: number;
// }

// let c: Circle = {
//   kind: ShapeKind.Square, // 오류! 'ShapeKind.Circle' 타입에 'ShapeKind.Square' 타입을 할당할 수 없습니다.
//   radius: 100,
// }

// enum E {
//   Foo,
//   Bar,
// }

// function f(x: E) {
//   if (x !== E.Foo || x !== E.Bar) {
//       //             ~~~~~~~~~~~
//       // 에러! E 타입은 Foo, Bar 둘 중 하나이기 때문에 이 조건은 항상 true를 반환합니다.
//   }
// }

// enum E {
//   X, Y, Z
// }

// function f(obj: { X: number }) {
//   return obj.X;
// }

// // E가 X라는 숫자 프로퍼티를 가지고 있기 때문에 동작하는 코드입니다.
// f(E);

// enum LogLevel {
//   ERROR, WARN, INFO, DEBUG
// }

// /**
// * 이것은 아래와 동일합니다. :
// * type LogLevelStrings = 'ERROR' | 'WARN' | 'INFO' | 'DEBUG';
// */
// type LogLevelStrings = keyof typeof LogLevel;

// function printImportant(key: LogLevelStrings, message: string) {
//   const num = LogLevel[key];
//   if (num <= LogLevel.WARN) {
//      console.log('Log level key is: ', key);
//      console.log('Log level value is: ', num);
//      console.log('Log level message is: ', message);
//   }
// }
// printImportant('ERROR', 'This is a message');

// enum Enum {
//   A
// }
// let a = Enum.A;
// let nameOfA = Enum[a]; // "A"

// var Enum;
// (function (Enum) {
//     Enum[Enum["A"] = 0] = "A";
// })(Enum || (Enum = {}));
// var a = Enum.A;
// var nameOfA = Enum[a]; // "A"


// const enum Enum {
//   A = 1,
//   B = A * 2
// }

// const enum Directions {
//   Up,
//   Down,
//   Left,
//   Right
// }

// let directions = [Directions.Up, Directions.Down, Directions.Left, Directions.Right]

declare enum Enum {
  A = 1,
  B,
  C = 2
}