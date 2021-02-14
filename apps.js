document.onkeydown = function(e) {
    console.log("key code is:", e.keyCode)
    if (e.keyCode == 37) {
        boy = document.querySelector('.boy')
        boy.classlist.Add('animationboy')
        setTimeout(() => {
            boy.classlist.remove('animateboy')
        }, 700);


    }
}

//practice