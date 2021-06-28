// // function
// // 기명 함수
// function add(x: number, y: number): number {
//   return x + y;
// }

// // 익명 함수
// let myAdd = function(x: number, y: number): number { return x + y };

// let myAdd: (x: number, y: number) => number =
//   function(x: number, y: number): number { return x + y; };

// let myAdd: (baseValue: number, increment: number) => number =
//   function(x: number, y: number): number { return x + y; };

// // myAdd는 전체 함수 타입을 가집니다
// let myAdd = function(x: number, y: number): number { return  x + y; };

// // 매개변수 x 와 y는 number 타입을 가집니다
// let myAdd: (baseValue: number, increment: number) => number =
//     function(x, y) { return x + y; };

// // 선택적 매개변수와 기본 매개변수
// function buildName(firstName: string, lastName: string) {
//     return firstName + " " + lastName;
// }

// let result1 = buildName("Bob");                  // 오류, 너무 적은 매개변수
// let result2 = buildName("Bob", "Adams", "Sr.");  // 오류, 너무 많은 매개변수
// let result3 = buildName("Bob", "Adams");         // 정확함

// function buildName(firstName: string, lastName?: string) {
//     if (lastName)
//         return firstName + " " + lastName;
//     else
//         return firstName;
// }

// let result1 = buildName("Bob");                  // 지금은 바르게 동작
// let result2 = buildName("Bob", "Adams", "Sr.");  // 오류, 너무 많은 매개변수
// let result3 = buildName("Bob", "Adams");  

// function buildName(firstName: string, lastName = "Smith") {
//     return firstName + " " + lastName;
// }

// let result1 = buildName("Bob");                  // 올바르게 동작, "Bob Smith" 반환
// let result2 = buildName("Bob", undefined);       // 여전히 동작, 역시 "Bob Smith" 반환
// let result3 = buildName("Bob", "Adams", "Sr.");  // 오류, 너무 많은 매개변수
// let result4 = buildName("Bob", "Adams");         // 정확함

// function buildName(firstName = "Will", lastName: string) {
//     return firstName + " " + lastName;
// }

// let result1 = buildName("Bob");                  // 오류, 너무 적은 매개변수
// let result2 = buildName("Bob", "Adams", "Sr.");  // 오류, 너무 많은 매개변수
// let result3 = buildName("Bob", "Adams");         // 성공, "Bob Adams" 반환
// let result4 = buildName(undefined, "Adams");     // 성공, "Will Adams" 반환

// // 나머지 매개변수
// function buildName(firstName: string, ...restOfName: string[]) {
//     return firstName + " " + restOfName.join(" ");
// }

// // employeeName 은 "Joseph Samuel Lucas MacKinzie" 가 될것입니다.
// let employeeName = buildName("Joseph", "Samuel", "Lucas", "MacKinzie");

// function buildName(firstName: string, ...restOfName: string[]) {
//     return firstName + " " + restOfName.join(" ");
// }

// let buildNameFun: (fname: string, ...rest: string[]) => string = buildName;

// let deck = {
//     suits: ["hearts", "spades", "clubs", "diamonds"],
//     cards: Array(52),
//     createCardPicker: function() {
//         return function() {
//             let pickedCard = Math.floor(Math.random() * 52);
//             let pickedSuit = Math.floor(pickedCard / 13);

//             return {suit: this.suits[pickedSuit], card: pickedCard % 13};
//         }
//     }
// }

// let cardPicker = deck.createCardPicker();
// let pickedCard = cardPicker();

// alert("card: " + pickedCard.card + " of " + pickedCard.suit);

// let deck = {
//     suits: ["hearts", "spades", "clubs", "diamonds"],
//     cards: Array(52),
//     createCardPicker: function() {
//         // NOTE: 아랫줄은 화살표 함수로써, 'this'를 이곳에서 캡처할 수 있도록 합니다
//         return () => {
//             let pickedCard = Math.floor(Math.random() * 52);
//             let pickedSuit = Math.floor(pickedCard / 13);

//             return {suit: this.suits[pickedSuit], card: pickedCard % 13};
//         }
//     }
// }

// let cardPicker = deck.createCardPicker();
// let pickedCard = cardPicker();

// alert("card: " + pickedCard.card + " of " + pickedCard.suit);

// function f(this: void) {
//     // 독립형 함수에서 `this`를 사용할 수 없는 것을 확인함
// }
// interface Card {
//     suit: string;
//     card: number;
// }
// interface Deck {
//     suits: string[];
//     cards: number[];
//     createCardPicker(this: Deck): () => Card;
// }
// let deck: Deck = {
//     suits: ["hearts", "spades", "clubs", "diamonds"],
//     cards: Array(52),
//     // NOTE: 아래 함수는 이제 callee가 반드시 Deck 타입이어야 함을 명시적으로 지정합니다.
//     createCardPicker: function(this: Deck) {
//         return () => {
//             let pickedCard = Math.floor(Math.random() * 52);
//             let pickedSuit = Math.floor(pickedCard / 13);

//             return {suit: this.suits[pickedSuit], card: pickedCard % 13};
//         }
//     }
// }

// let cardPicker = deck.createCardPicker();
// let pickedCard = cardPicker();

// alert("card: " + pickedCard.card + " of " + pickedCard.suit);

// interface UIElement {
//     addClickListener(onclick: (this: void, e: Event) => void): void;
// }

// class Handler {
//     info: string;
//     onClickBad(this: Handler, e: Event) {
//         // 이런, `this`가 여기서 쓰이는군요. 이 콜백을 쓰면 런타임에서 충돌을 일으키겠군요
//         this.info = e.message;
//     }
// }
// let h = new Handler();
// uiElement.addClickListener(h.onClickBad); // 오류!

// class Handler {
//     info: string;
//     onClickGood(this: void, e: Event) {
//         // void 타입이기 때문에 this는 이곳에서 쓸 수 없습니다!
//         console.log('clicked!');
//     }
// }
// let h = new Handler();
// uiElement.addClickListener(h.onClickGood);

// class Handler {
//     info: string;
//     onClickGood = (e: Event) => { this.info = e.message }
// }

// // overloads
// let suits = ["hearts", "spades", "clubs", "diamonds"];

// function pickCard(x:any): any {
//     // 인자가 배열 또는 객체인지 확인
//     // 만약 그렇다면, deck이 주어지고 card를 선택합니다.
//     if (typeof x == "object") {
//         let pickedCard = Math.floor(Math.random() * x.length);
//         return pickedCard;
//     }
//     // 그렇지 않다면 그냥 card를 선택합니다.
//     else if (typeof x == "number") {
//         let pickedSuit = Math.floor(x / 13);
//         return { suit: suits[pickedSuit], card: x % 13 };
//     }
// }

// let myDeck = [{ suit: "diamonds", card: 2 }, { suit: "spades", card: 10 }, { suit: "hearts", card: 4 }];
// let pickedCard1 = myDeck[pickCard(myDeck)];
// alert("card: " + pickedCard1.card + " of " + pickedCard1.suit);

// let pickedCard2 = pickCard(15);
// alert("card: " + pickedCard2.card + " of " + pickedCard2.suit);

let suits = ["hearts", "spades", "clubs", "diamonds"];

function pickCard(x: {suit: string; card: number; }[]): number;
function pickCard(x: number): {suit: string; card: number; };
function pickCard(x: any): any {
    // 인자가 배열 또는 객체인지 확인
    // 만약 그렇다면, deck이 주어지고 card를 선택합니다.
    if (typeof x == "object") {
        let pickedCard = Math.floor(Math.random() * x.length);
        return pickedCard;
    }
    // 그렇지 않다면 그냥 card를 선택합니다.
    else if (typeof x == "number") {
        let pickedSuit = Math.floor(x / 13);
        return { suit: suits[pickedSuit], card: x % 13 };
    }
}

let myDeck = [{ suit: "diamonds", card: 2 }, { suit: "spades", card: 10 }, { suit: "hearts", card: 4 }];
let pickedCard1 = myDeck[pickCard(myDeck)];
alert("card: " + pickedCard1.card + " of " + pickedCard1.suit);

let pickedCard2 = pickCard(15);
alert("card: " + pickedCard2.card + " of " + pickedCard2.suit);