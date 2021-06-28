// function identity(arg: number): number {
//   return arg;
// }

// function identity(arg: any): any {
//   return arg;
// }

// function identity<T>(arg: T): T {
//   return arg;
// }

// let output = identity<string>("myString"); // 출력 타입은 'string'입니다.

// let output = identity("myString"); //출력 타입은 'string'입니다.

// function loggingIdentity<T>(arg: T): T {
//   console.log(arg.length); // 오류: T에는 .length 가 없습니다.
//   return arg;
// }

// function loggingIdentity<T>(arg: T[]): T[] {
//   console.log(arg.length); // 배열은 .length를 가지고 있습니다. 따라서 오류는 없습니다.
//   return arg;
// }

// function loggingIdentity<T>(arg: Array<T>): Array<T> {
//   console.log(arg.length); // 배열은 .length를 가지고 있습니다. 따라서 오류는 없습니다.
//   return arg;
// }

// function identity<T>(arg: T): T {
//   return arg;
// }

// let myIdentity: <T>(arg: T) => T = identity;

// function identity<T>(arg: T): T {
//   return arg;
// }

// let myIdentity: <U>(arg: U) => U = identity;

// function identity<T>(arg: T): T {
//   return arg;
// }

// let myIdentity: { <T>(arg: T): T } = identity;

// interface GenericIdentityFn {
//   <T>(arg: T): T;
// }

// function identity<T>(arg: T): T {
//   return arg;
// }

// let myIdentity: GenericIdentityFn = identity;

// interface GenericIdentityFn<T> {
//   (arg: T): T;
// }

// function identity<T>(arg: T): T {
//   return arg;
// }

// let myIdentity: GenericIdentityFn<number> = identity;

// class GenericNumber<T> {
//   zeroValue: T;
//   add: (x: T, y: T) => T;
// }

// let myGenericNumber = new GenericNumber<number>();
// myGenericNumber.zeroValue = 0;
// myGenericNumber.add = function(x, y) { return x + y; };

// let stringNumeric = new GenericNumber<string>();
// stringNumeric.zeroValue = "";
// stringNumeric.add = function(x, y) { return x + y; };

// console.log(stringNumeric.add(stringNumeric.zeroValue, "test"));

// function loggingIdentity<T>(arg: T): T {
//   console.log(arg.length);  // 오류: T에는 .length가 없습니다.
//   return arg;
// }

// interface Lengthwise {
//   length: number;
// }

// function loggingIdentity<T extends Lengthwise>(arg: T): T {
//   console.log(arg.length);  // 이제 .length 프로퍼티가 있는 것을 알기 때문에 더 이상 오류가 발생하지 않습니다.
//   return arg;
// }

// loggingIdentity(3);  // 오류, number는 .length 프로퍼티가 없습니다.

// loggingIdentity({length: 10, value: 3});

// function getProperty<T, K extends keyof T>(obj: T, key: K) {
//   return obj[key];
// }

// let x = { a: 1, b: 2, c: 3, d: 4 };

// getProperty(x, "a"); // 성공
// getProperty(x, "m"); // 오류: 인수의 타입 'm' 은 'a' | 'b' | 'c' | 'd'에 해당되지 않음.

// function create<T>(c: {new(): T; }): T {
//   return new c();
// }

// class BeeKeeper {
//   hasMask: boolean;
// }

// class ZooKeeper {
//   nametag: string;
// }

// class Animal {
//   numLegs: number;
// }

// class Bee extends Animal {
//   keeper: BeeKeeper;
// }

// class Lion extends Animal {
//   keeper: ZooKeeper;
// }

// function createInstance<A extends Animal>(c: new () => A): A {
//   return new c();
// }

// createInstance(Lion).keeper.nametag;  // 타입검사!
// createInstance(Bee).keeper.hasMask;   // 타입검사!