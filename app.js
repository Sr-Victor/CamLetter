const audio = document.getElementById("audio");

document.addEventListener("click", () => {
  audio.muted = false;
}, { once: true });

alert("Click anywhere to enable audio");