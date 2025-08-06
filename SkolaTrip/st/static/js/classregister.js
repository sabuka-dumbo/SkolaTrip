let container = document.querySelector('.container');
let register2 = document.querySelector('.register2');
let register3 = document.querySelector('.register3');

let stepCircle1 = document.getElementById('step-circle1');
let stepCircle2 = document.getElementById('step-circle2');
let stepCircle3 = document.getElementById('step-circle3');

let btn1 = document.getElementById('submit');
let btn2 = register2.querySelector('button[type="button"]');
let btn3 = document.getElementById('last-btn');

// Load saved progress
window.addEventListener('load', () => {
    let step = localStorage.getItem('currentStep') || '1';

    if (step === '1') {
        showStep(1);
    } else if (step === '2') {
        showStep(2);
    } else if (step === '3') {
        showStep(3);
    }
});

function showStep(step) {
    container.style.display = step === 1 ? 'block' : 'none';
    register2.style.display = step === 2 ? 'block' : 'none';
    register3.style.display = step === 3 ? 'block' : 'none';

    stepCircle1.style.background = step >= 1 ? '#00A2FF' : '';
    stepCircle2.style.background = step >= 2 ? '#00A2FF' : '';
    stepCircle3.style.background = step >= 3 ? '#00A2FF' : '';

    localStorage.setItem('currentStep', step.toString());
}

btn1.addEventListener('click', (e) => {
    e.preventDefault();
    showStep(2);
});

btn2.addEventListener('click', (e) => {
    e.preventDefault();
    showStep(3);
});

btn3.addEventListener('click', () => {
    localStorage.removeItem('currentStep');
});
