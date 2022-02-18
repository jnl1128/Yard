
const inputMainBox = document.getElementById('search-container')
const inputMain = document.querySelector('.search-input')
const searchBtnMain = document.getElementById('search-btn-main')

inputMainBox.addEventListener('mouseenter',function(){searchBtnMain.style.opacity = 1})
inputMainBox.addEventListener('change', function(){inputMain.placeholder=''})
inputMainBox.addEventListener('change', function(){searchBtnMain.style.opacity = 0.5})