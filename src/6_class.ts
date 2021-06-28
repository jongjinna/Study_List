// // Class
// class Greeter {
//   greeting: string;
//   constructor(message: string) {
//       this.greeting = message;
//   }
//   greet() {
//       return "Hello, " + this.greeting;
//   }
// }

// let greeters = new Greeter("world");

// // Inherit
// class Animal {
//   move(distanceInMeters: number = 0) {
//       console.log(`Animal moved ${distanceInMeters}m.`);
//   }
// }

// class Dog extends Animal {
//   bark() {
//       console.log('Woof! Woof!');
//   }
// }

// const dog = new Dog();
// dog.bark();
// dog.move(10);
// dog.bark();

// class Animal {
//   name: string;
//   constructor(theName: string) { this.name = theName; }
//   move(distanceInMeters: number = 0) {
//       console.log(`${this.name} moved ${distanceInMeters}m.`);
//   }
// }

// class Snake extends Animal {
//   constructor(name: string) { super(name); }
//   move(distanceInMeters = 5) {
//       console.log("Slithering...");
//       super.move(distanceInMeters);
//   }
// }

// class Horse extends Animal {
//   constructor(name: string) { super(name); }
//   move(distanceInMeters = 45) {
//       console.log("Galloping...");
//       super.move(distanceInMeters);
//   }
// }

// let sam = new Snake("Sammy the Python");
// let tom: Animal = new Horse("Tommy the Palomino");

// sam.move();
// tom.move(34);

// // Public, private, and protected modifiers
// class Animal {
//   public name: string;
//   public constructor(theName: string) { this.name = theName; }
//   public move(distanceInMeters: number) {
//       console.log(`${this.name} moved ${distanceInMeters}m.`);
//   }
// }

// class Animal {
//   #name: string;
//   constructor(theName: string) { this.#name = theName; }
// }

// new Animal("Cat").#name; // 프로퍼티 '#name'은 비공개 식별자이기 때문에 'Animal' 클래스 외부에선 접근할 수 없습니다.

// class Animal {
//   private name: string;
//   constructor(theName: string) { this.name = theName; }
// }

// new Animal("Cat").name; // 오류: 'name'은 비공개로 선언되어 있습니다

// class Animal {
//   private name: string;
//   constructor(theName: string) { this.name = theName; }
// }

// class Rhino extends Animal {
//   constructor() { super("Rhino"); }
// }

// class Employee {
//   private name: string;
//   constructor(theName: string) { this.name = theName; }
// }

// let animal = new Animal("Goat");
// let rhino = new Rhino();
// let employee = new Employee("Bob");

// animal = rhino;
// animal = employee; // 오류: 'Animal'과 'Employee'은 호환될 수 없음.

// class Person {
//   protected name: string;
//   constructor(name: string) { this.name = name; }
// }

// class Employee extends Person {
//   private department: string;

//   constructor(name: string, department: string) {
//       super(name);
//       this.department = department;
//   }

//   public getElevatorPitch() {
//       return `Hello, my name is ${this.name} and I work in ${this.department}.`;
//   }
// }

// let howard = new Employee("Howard", "Sales");
// console.log(howard.getElevatorPitch());
// console.log(howard.name); // 오류

// class Person {
//   protected name: string;
//   protected constructor(theName: string) { this.name = theName; }
// }

// // Employee는 Person을 확장할 수 있습니다.
// class Employee extends Person {
//   private department: string;

//   constructor(name: string, department: string) {
//       super(name);
//       this.department = department;
//   }

//   public getElevatorPitch() {
//       return `Hello, my name is ${this.name} and I work in ${this.department}.`;
//   }
// }

// let howard = new Employee("Howard", "Sales");
// let john = new Person("John"); // 오류: 'Person'의 생성자는 protected 입니다.

// class Octopus {
//   readonly name: string;
//   readonly numberOfLegs: number = 8;
//   constructor (theName: string) {
//       this.name = theName;
//   }
// }
// let dad = new Octopus("Man with the 8 strong legs");
// dad.name = "Man with the 3-piece suit"; // 오류! name은 읽기전용 입니다.

// class Octopus {
//   readonly numberOfLegs: number = 8;
//   constructor(readonly name: string) {
//   }
// }

// class Employee {
//   fullName: string;
// }

// let employee = new Employee();
// employee.fullName = "Bob Smith";
// if (employee.fullName) {
//   console.log(employee.fullName);
// }

// const fullNameMaxLength = 10;

// class Employee {
//     private _fullName: string;

//     get fullName(): string {
//         return this._fullName;
//     }

//     set fullName(newName: string) {
//         if (newName && newName.length > fullNameMaxLength) {
//             throw new Error("fullName has a max length of " + fullNameMaxLength);
//         }

//         this._fullName = newName;
//     }
// }

// let employee = new Employee();
// employee.fullName = "Bob Smith";
// if (employee.fullName) {
//     console.log(employee.fullName);
// }

// class Grid {
//   static origin = {x: 0, y: 0};
//   calculateDistanceFromOrigin(point: {x: number; y: number;}) {
//       let xDist = (point.x - Grid.origin.x);
//       let yDist = (point.y - Grid.origin.y);
//       return Math.sqrt(xDist * xDist + yDist * yDist) / this.scale;
//   }
//   constructor (public scale: number) { }
// }

// let grid1 = new Grid(1.0);  // 1x scale
// let grid2 = new Grid(5.0);  // 5x scale

// console.log(grid1.calculateDistanceFromOrigin({x: 10, y: 10}));
// console.log(grid2.calculateDistanceFromOrigin({x: 10, y: 10}));

// abstract class Animal {
//   abstract makeSound(): void;
//   move(): void {
//       console.log("roaming the earth...");
//   }
// }

// abstract class Department {

//   constructor(public name: string) {
//   }

//   printName(): void {
//       console.log("Department name: " + this.name);
//   }

//   abstract printMeeting(): void; // 반드시 파생된 클래스에서 구현되어야 합니다.
// }

// class AccountingDepartment extends Department {

//   constructor() {
//       super("Accounting and Auditing"); // 파생된 클래스의 생성자는 반드시 super()를 호출해야 합니다.
//   }

//   printMeeting(): void {
//       console.log("The Accounting Department meets each Monday at 10am.");
//   }

//   generateReports(): void {
//       console.log("Generating accounting reports...");
//   }
// }

// let department: Department; // 추상 타입의 레퍼런스를 생성합니다
// department = new Department(); // 오류: 추상 클래스는 인스턴스화 할 수 없습니다
// department = new AccountingDepartment(); // 추상이 아닌 하위 클래스를 생성하고 할당합니다
// department.printName();
// department.printMeeting();
// department.generateReports(); // 오류: 선언된 추상 타입에 메서드가 존재하지 않습니다

// class Greeter {
//   greeting: string;
//   constructor(message: string) {
//       this.greeting = message;
//   }
//   greet() {
//       return "Hello, " + this.greeting;
//   }
// }

// let greeter: Greeter;
// greeter = new Greeter("world");
// console.log(greeter.greet()); // "Hello, world""

// let Greeter = (function () {
//   function Greeter(message) {
//       this.greeting = message;
//   }
//   Greeter.prototype.greet = function () {
//       return "Hello, " + this.greeting;
//   };
//   return Greeter;
// })();

// let greeter;
// greeter = new Greeter("world");
// console.log(greeter.greet()); // "Hello, world"

// class Greeter {
//   static standardGreeting = "Hello, there";
//   greeting: string;
//   greet() {
//       if (this.greeting) {
//           return "Hello, " + this.greeting;
//       }
//       else {
//           return Greeter.standardGreeting;
//       }
//   }
// }

// let greeter1: Greeter;
// greeter1 = new Greeter();
// console.log(greeter1.greet()); // "Hello, there"

// let greeterMaker: typeof Greeter = Greeter;
// greeterMaker.standardGreeting = "Hey there!";

// let greeter2: Greeter = new greeterMaker();
// console.log(greeter2.greet()); // "Hey there!"

// class Point {
//   x: number;
//   y: number;
// }

// interface Point3d extends Point {
//   z: number;
// }

// let point3d: Point3d = {x: 1, y: 2, z: 3};