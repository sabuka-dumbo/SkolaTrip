let container = document.querySelector('.container');
let register2 = document.querySelector('.register2');
let form1 = document.querySelector('.container-form');
let form2 = document.querySelector('.register2-form');
let input = document.getElementsByTagName('input');
let register3 = document.querySelector('.register3');
let stepCircle = document.getElementById('step-circle1');
let stepCircle2 = document.getElementById('step-circle2');
let stepCircle3 = document.getElementById('step-circle3');

window.addEventListener('load', () => {
    let form1Completed = localStorage.getItem('form1Completed');
    let form2Completed = localStorage.getItem('form2Completed');

    if (form1Completed === 'true') {
        container.style.display = 'none';
        register2.style.display = 'block';
        stepCircle.style.background = '#00A2FF';
    }

    if (form2Completed === 'true') {
        register2.style.display = 'none';
        register3.style.display = 'block';
        stepCircle2.style.background = '#00A2FF';
        stepCircle3.style.background = '#00A2FF';
    }

    else {
        container.style.display = 'block';
        register2.style.display = 'none';
        register3.style.display = 'none';
    }
});

function handleCheck(){
    if(form1){
        form1.addEventListener('submit', function(e){
            e.preventDefault();
            container.style.display = 'none';
            register2.style.display = 'block';
            stepCircle.style.background = '#00A2FF';
            localStorage.setItem('form1Completed', 'true');
        });
    }
}

function handleCheck2(){
    if(form2){
        form2.addEventListener('submit', function(e){
            e.preventDefault();
            register2.style.display = 'none';
            register3.style.display = 'block';
            stepCircle2.style.background = '#00A2FF';
            stepCircle3.style.background = '#00A2FF';
            localStorage.setItem('form2Completed', 'true');
        });
    }
}

handleCheck();
handleCheck2();
