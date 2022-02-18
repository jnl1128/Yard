const certificates = document.querySelectorAll('.certificate-container');
const certificateList = document.querySelector('.certificate-list')
const certificate_rightBtn = document.getElementById('certificate-rightBtn')
const certificate_leftBtn = document.getElementById('certificate-leftBtn')

const certificate_btn = document.getElementById('certificate-btn')

function displayMusicInfo(event){
  event.target.childNodes[3].classList.toggle('hidden');
  event.target.childNodes[1].style.filter = 'brightness(50%)'
  
}
function hideMusicInfo(event){
  event.target.childNodes[3].classList.add('hidden')
  event.target.childNodes[1].style.filter = 'brightness(100%)'
}
  


//eventListener
[].forEach.call(certificates, function(certificate){
  certificate.addEventListener('mouseenter', displayMusicInfo)

});
[].forEach.call(certificates, function(certificate){
  certificate.addEventListener('mouseleave', hideMusicInfo);

});


function slideCert(event){
  let direction = 0;
  const certificateLen = certificates.length
  certificates.forEach(function(certificate){
    let temp = Number(certificate.style.left.slice(0,4))
    if (isNaN(temp)) temp = 0

    if(event.target === certificate_rightBtn){
      direction = -170;
      if((temp+direction) < (certificateLen) * direction){
        return 
      }
    }
    else if(event.target === certificate_leftBtn){
      direction = 170;
      if(temp == 0  || isNaN(temp)){
        return 
      }
    }
    else{
      return
    }

    const newLeft  = String(temp + direction)
    certificate.style.left = newLeft + 'px'
  })
  
}

certificate_btn.addEventListener('click', slideCert);