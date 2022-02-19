const inputBox = document.querySelector('.nav--inputBox')
const input = document.querySelector('.nav--searchBtn')
const searchBtn = document.getElementById('nav--searchBtn')

function  enterInput(){
  searchBtn.style.zIndex = 100;
  console.log(searchBtn.style.zIndex)
}

function leaveInput(){
  input.placeholder = input.value
  searchBtn.style.zIndex = 0;
}


inputBox.addEventListener('mouseenter', enterInput)
inputBox.addEventListener('change', leaveInput)