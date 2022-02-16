const scrollBtn = document.getElementById('main-scrollBtn')
console.log(scrollBtn.href)
let rotated = false;

function upsideDownBtn(){
  let deg = rotated ? 90 : 270
  scrollBtn.style.transform = `rotate(${deg}deg)`;
  scrollBtn.href = rotated ?   '#': '#main-scrollBtn'
  rotated = !rotated;
}
scrollBtn.addEventListener('click', upsideDownBtn)
