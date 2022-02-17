const signupLabels = document.querySelectorAll(".signup.center-container p label:nth-child(1)");
console.log(signupLabels)

for (var i = 0; i < signupLabels.length; i++) {
    signupLabels[i].remove();
    console.log(signupLabels[i])
};

const loginLabels = document.querySelectorAll(".login.center-container p label:nth-child(1)");
loginLabels[0].remove();
loginLabels[1].remove();
loginLabels[2].innerHTML = `다음번엔 기억해주세요`;