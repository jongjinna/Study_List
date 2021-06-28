// const를 사용하여 변수 helloWorld가
// 절대 변경되지 않음을 보장합니다.

// // 문자형 리터럴
// // 따라서, TypeScript는 문자열이 아닌 "Hello World"로 타입을 정합니다.
// const helloWorld = "Hello World";

// // 반면, let은 변경될 수 있으므로 컴파일러는 문자열이라고 선언할 것입니다.
// let hiWorld = "Hi World";

// // @errors: 2345
// type Easing = "ease-in" | "ease-out" | "ease-in-out";

// class UIElement {
//   animate(dx: number, dy: number, easing: Easing) {
//     if (easing === "ease-in") {
//       // ...
//     } else if (easing === "ease-out") {
//     } else if (easing === "ease-in-out") {
//     } else {
//       // 하지만 누군가가 타입을 무시하게 된다면
//       // 이곳에 도달하게 될 수 있습니다.
//     }
//   }
// }

// let button = new UIElement();
// button.animate(0, 0, "ease-in");
// button.animate(0, 0, "uneasy");

// function createElement(tagName: "img"): HTMLImageElement;
// function createElement(tagName: "input"): HTMLInputElement;
// // ... 추가적인 중복 정의들 ...
// function createElement(tagName: string): Element {
//   // ... 여기에 로직 추가 ...
// }

// 숫자형 리터럴
function rollDice(): 1 | 2 | 3 | 4 | 5 | 6 {
  return (Math.floor(Math.random() * 6) + 1) as 1 | 2 | 3 | 4 | 5 | 6;
}

const result = rollDice();

/** loc/lat 좌표에 지도를 생성합니다. */
declare function setupMap(config: MapConfig): void;
// ---생략---
interface MapConfig {
  lng: number;
  lat: number;
  tileSize: 8 | 16 | 32;
}

setupMap({ lng: -73.935242, lat: 40.73061, tileSize: 16 });