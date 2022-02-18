const input = document.querySelector('.nav--inputBox')
const searchBtn = document.getElementById('nav--searchBtn')
console.log(input)
console.log(searchBtn)
function  enterInput(){
  console.log('enter')
  searchBtn.style.zIndex = 200;
}

function leaveInput(){
  searchBtn.style.zIndex = 0;
}
input.addEventListener('mouseenter', enterInput)
input.addEventListener('change', leaveInput)