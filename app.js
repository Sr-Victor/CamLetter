const seal = document.getElementById("seal");
const overlay = document.getElementById("overlay");
const audio = document.getElementById("audio");

seal.addEventListener("click", () => {
  audio.play().then(() => {
    overlay.style.opacity = "0";
    setTimeout(() => {
      overlay.style.display = "none";
    }, 400);
  });
});
