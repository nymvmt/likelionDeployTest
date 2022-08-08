// function App() {
//   // 새로고침 떄 마다 시행
//   this.init = () => {
//     console.log(getCookie("modal-closed"));
//     if (getCookie("modal-closed") === "true") {
//       closeModal();
//       return;
//     }
//     openModal();
//   };
  
// const body = document.querySelector("body");
// const modal = document.querySelector(".modal-container");
// const close = document.querySelector(".modal-close");
// const neverSee = document.querySelector(".modal-stop-button");

// neverSee.addEventListener("click", () => {
//   closeModal();
//   setCookie("modal-closed", "true", 1);
// });

// modal.addEventListener("click", (event) => {
//   if (event.target === modal) {
//     closeModal();
//   }
// });

// section.addEventListener("click", openModal);
// close.addEventListener("click", closeModal);

// function openModal() {
//   modal.classList.add("open");
//   body.style.overflow = "hidden";
// }

// function closeModal() {
//   modal.classList.remove("open");
//   body.style.overflow = "auto";
// }

// //   쿠키를 생성
// function setCookie(name, value, expireDate) {
//   let date = new Date();
//   date.setDate(date.getDate() + expireDate);
//   document.cookie = `${name}=${value};expires=${date.toGMTString()}`;
// }

// function getCookie(name) {
//   let cookie = document.cookie;
//   if (cookie) {
//     let cookies = cookie.split("; ");
//     for (let index in cookies) {
//       let cookieName = cookies[index].split("=");
//       if (cookieName[0] === name) {
//         return cookieName[1];
//       }
//     }
//   }
// }
// }

// const app = new App();

// app.init();