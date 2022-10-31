// /**
//  * 문자열을 받고 왼쪽에 "padding"을 추가합니다.
//  * 만약 'padding'이 문자열이라면, 'padding'은 왼쪽에 더해질 것입니다.
//  * 만약 'padding'이 숫자라면, 그 숫자만큼의 공백이 왼쪽에 더해질 것입니다.
//  */
//  function padLeft(value: string, padding: any) {
//   if (typeof padding === "number") {
//     return Array(padding + 1).join(" ") + value;
//   }
//   if (typeof padding === "string") {
//     return padding + value;
//   }
//   throw new Error(`Expected string or number, got '${padding}'.`);
// }

// padLeft("Hello world", 4); // "Hello world"를 반환합니다.

// declare function padLeft(value: string, padding: any) {
//   if (typeof padding === "number") {
//     return Array(padding + 1).join(" ") + value;
//   }
//   if (typeof padding === "string") {
//     return padding + value;
//   }
//   throw new Error(`Expected string or number, got '${padding}'.`);
// }
// // 컴파일 타임에는 통과하지만, 런타임에는 오류가 발생합니다.
// let indentedString = padLeft("Hello world", true);

// function padLeft(value: string, padding: string | number) {
//   if (typeof padding === "number") {
//     return Array(padding + 1).join(" ") + value;
//   }
//   if (typeof padding === "string") {
//     return padding + value;
//   }
//   throw new Error(`Expected string or number, got '${padding}'.`);
// }
    

// let indentedString = padLeft("Hello world", true);

// interface Bird {
//   fly(): void;
//   layEggs(): void;
// }

// interface Fish {
//   swim(): void;
//   layEggs(): void;
// }

// declare function getSmallPet(): Fish | Bird;

// let pet = getSmallPet();
// pet.layEggs();

// // 두 개의 잠재적인 타입 중 하나에서만 사용할 수 있습니다.
// pet.swim();

// type NetworkLoadingState = {
//   state: "loading";
// };

// type NetworkFailedState = {
//   state: "failed";
//   code: number;
// };

// type NetworkSuccessState = {
//   state: "success";
//   response: {
//     title: string;
//     duration: number;
//     summary: string;
//   };
// };

// // 위 타입들 중 단 하나를 대표하는 타입을 만들었지만,
// // 그것이 무엇에 해당하는지 아직 확실하지 않습니다.
// type NetworkState =
//   | NetworkLoadingState
//   | NetworkFailedState
//   | NetworkSuccessState;

// function networkStatus(state: NetworkState): string {
//   // 현재 TypeScript는 셋 중 어떤 것이
//   // state가 될 수 있는 잠재적인 타입인지 알 수 없습니다.

//   // 모든 타입에 공유되지 않는 프로퍼티에 접근하려는 시도는
//   // 오류를 발생시킵니다.
//   // state.code;

//     // state에 swtich문을 사용하여, TypeScript는 코드 흐름을 분석하면서
//   // 유니언 타입을 좁혀나갈 수 있습니다.
//   switch (state.state) {
//     case "loading":
//       return "Downloading...";
//     case "failed":
//       // 여기서 타입은 NetworkFailedState일 것이며,
//       // 따라서 `code` 필드에 접근할 수 있습니다.
//       return `Error ${state.code} downloading`;
//     case "success":
//       return `Downloaded ${state.response.title} - ${state.response.summary}`;
//   }
// }

// // 교차 타입
// interface ErrorHandling {
//   success: boolean;
//   error?: { message: string };
// }

// interface ArtworksData {
//   artworks: { title: string }[];
// }

// interface ArtistsData {
//   artists: { name: string }[];
// }

// // 이 인터페이스들은
// // 하나의 에러 핸들링과 자체 데이터로 구성됩니다.

// type ArtworksResponse = ArtworksData & ErrorHandling;
// type ArtistsResponse = ArtistsData & ErrorHandling;

// const handleArtistsResponse = (response: ArtistsResponse) => {
//   if (response.error) {
//     console.error(response.error.message);
//     return;
//   }

//   console.log(response.artists);
// };

// class Person {
//   constructor(public name: string) {}
// }

// interface Loggable {
//   log(name: string): void;
// }

// class ConsoleLogger implements Loggable {
//   log(name: string) {
//     console.log(`Hello, I'm ${name}.`);
//   }
// }

// // 두 객체를 받아 하나로 합칩니다.
// function extend<First extends {}, Second extends {}>(
//   first: First,
//   second: Second
// ): First & Second {
//   const result: Partial<First & Second> = {};
//   for (const prop in first) {
//     if (first.hasOwnProperty(prop)) {
//       (result as First)[prop] = first[prop];
//     }
//   }
//   for (const prop in second) {
//     if (second.hasOwnProperty(prop)) {
//       (result as Second)[prop] = second[prop];
//     }
//   }
//   return result as First & Second;
// }

// const jim = extend(new Person("Jim"), ConsoleLogger.prototype);
// jim.log(jim.name);