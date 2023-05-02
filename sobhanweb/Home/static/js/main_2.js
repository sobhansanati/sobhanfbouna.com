const images = document.querySelectorAll('.slider img')
let currentImages = 0;




function reset(){
    for(let i=0; i < images.length;i++){
        images[i].classList.remove('active')
    }
}


function startslide(){
    reset()
    images[0].classList.add('active');
}


function slideleft(){
    reset();
    images[currentImages - 1].classList.add('active');
    currentImages--;
}

function slideright(){
    reset();
    images[currentImages + 1].classList.add('active');
    currentImages++;
}


document.querySelector('.left-arrow').addEventListener('click',function(){
    if(currentImages === 0 ){
        currentImages = images.length;
    }
    slideleft();
});

document.querySelector('.right-arrow').addEventListener('click',function(){
    if(currentImages === images.length -1 ){
        currentImages = -1;
    }
    slideright();
});

startslide();