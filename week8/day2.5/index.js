// const names = ["tyler", "olivia", "winnie"];

// const integers = [1, 2, 3, 4, 5, 6, 7, 8];
// const integersDoubled = [];

const owners = [
  {
    firstName: "Olivia",
  },
  {
    firstName: "Tyler",
  },
  {
    firstName: "Winnie",
  },
];

const newArray = owners.map((x) => {
  return x.firstName;
});
console.log(newArray);

// const upperCase = function (name) {
//   const blah = name.toUpperCase();
//   return blah;
// };
// const blahblah = upperCase("olivia");
// console.log(blahblah);

// const test1 = function (num) {
//   return num * 2;
// };
// console.log(test1(5));

// const newArray = integers.map((x) => {
//   return x * 2;
// });

// console.log(newArray);

// const result = integers.filter((num) => num > 3);
// console.log(result);

// integers.forEach((element) => console.log(element));
