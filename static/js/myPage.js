const certificates = document.querySelectorAll('.certificate-container');
const certificateList = document.querySelector('.certificate-list')
const moreCertBtn = document.getElementById('moreCertBtn')


function displayMusicInfo(event){
  event.target.childNodes[3].classList.toggle('hidden');
  event.target.childNodes[1].style.filter = 'brightness(50%)'
}
function hideMusicInfo(event){
  event.target.childNodes[3].classList.add('hidden')
  event.target.childNodes[1].style.filter = 'brightness(100%)'
}

function slideRight(){
  console.log('click')
  const slideX = 170 * -1
  
  certificateList.style.transform = `translateX(${slideX}px)`
  certificateList.style.overflow = 'visible'
  //certificateList.style.transfrom = `translateX(${-100}px)`
}

//eventListener
[].forEach.call(certificates, function(certificate){
  certificate.addEventListener('mouseenter', displayMusicInfo)

});
[].forEach.call(certificates, function(certificate){
  certificate.addEventListener('mouseleave', hideMusicInfo);

});


moreCertBtn.addEventListener('click', slideRight);
