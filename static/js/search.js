const inputBox = document.querySelector('.nav--inputBox')
const input = document.querySelector('.nav--searchBtn')
const searchBtn = document.getElementById('nav--searchBtn')

function  enterInput(){
  searchBtn.style.zIndex = 100;
}

function leaveInput(){
  input.placeholder = input.value
  searchBtn.style.zIndex = 0;
}


inputBox.addEventListener('mouseenter', enterInput)
inputBox.addEventListener('mouseleave', leaveInput)
