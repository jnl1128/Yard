
const inputMainBox = document.getElementById('search-container')
const inputMain = document.querySelector('.search-input')
const searchBtnMain = document.getElementById('search-btn-main')

inputMainBox.addEventListener('keydown',function(){searchBtnMain.style.opacity = 1})
inputMainBox.addEventListener('mouseenter',function(){searchBtnMain.style.opacity = 1})
inputMainBox.addEventListener('mouseleave',function(){searchBtnMain.style.opacity = 0.5})