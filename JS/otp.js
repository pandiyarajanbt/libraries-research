// const readline = require("readline");
// const rl = readline.createInterface({
//   input: process.stdin,
//   output: process.stdout,
// });
// const askQuestion = (question) => {
//   return new Promise((resolve) => {
//     rl.question(question, (answer) => {
//       resolve(answer);
//     });
//   });
// };
// const main = async () => {
//   const value = await setTimeout(() => (getOtp(), 1000));
//   function getOtp() {
//     let randomNumber = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9];
//     let random = Math.floor(Math.random() * randomNumber.length * 100000);
//     console.log("OTP Random Number", random);
//   }

//   if (value) {
//     const otp = await askQuestion("Enter the otp: ");
//     console.log(otp);
//   }
//   rl.close();
// };
// main();

// const readline = require("readline");
// const rl = readline.createInterface({
//     input: process.stdin,
//     output: process.stdout,
// });

// function generate_secure_number(params) {
//     let randomNumber = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9];
//     let random = Math.floor(Math.random() * randomNumber.length * 100000);
//     // console.log("OTP Random Number", random);
//     return random
// }

// rep = generate_secure_number()
// console.log("OTP Random Number", rep);

// const askQuestion = (question) => {
//     return new Promise((resolve) => {
//         rl.question(question, (answer) => {
//             resolve(answer);
//         });
//     });
// };

// async function vaild_otp(rep) {
//     const user_input = await askQuestion("Enter Number ? ");
//     console.log(user_input == rep)
//     rl.close()
// }

// vaild_otp(rep)

lst = [1, 2, 3, 4, 5, 6, 7, 8, 9]
// console.log(lst[::-1])

