let container = document.querySelector('.container');
let register2 = document.querySelector('.register2');
let register3 = document.querySelector('.register3');

let form1 = document.querySelector('.container-form');
let form2 = document.querySelector('.register2-form');
let form3 = document.querySelector('.register3-form');

let stepCircle = document.getElementById('step-circle1');
let stepCircle2 = document.getElementById('step-circle2');
let stepCircle3 = document.getElementById('step-circle3');

let btn1 = document.querySelector('.container-form button');
let btn2 = document.querySelector('.register2-form button');
let lastBtn = document.getElementById('last-btn');

// Prevent form submit on Enter key except in textarea
document.querySelector('form').addEventListener('keydown', function (e) {
    if (e.key === 'Enter' && e.target.tagName.toLowerCase() !== 'textarea') {
        e.preventDefault();
    }
});

// Validate all inputs inside a step container (div)
function validateStep(stepContainer) {
    let inputs = stepContainer.querySelectorAll('input, select, textarea');
    for (let input of inputs) {
        if (!input.checkValidity()) {
            input.reportValidity();
            return false;
        }
    }
    return true;
}

addEventListener('DOMContentLoaded', function () {
    container.style.display = 'block';
    register2.style.display = 'none';
    register3.style.display = 'none';
    stepCircle.style.background = '#00A2FF';
    stepCircle2.style.background = '#D9D9D9';
    stepCircle3.style.background = '#D9D9D9';
});

btn1.addEventListener('click', function () {
    if (validateStep(form1)) {
        container.style.display = 'none';
        register2.style.display = 'block';
        register3.style.display = 'none';
        stepCircle.style.background = '#00A2FF';
        stepCircle2.style.background = '#00A2FF';
    }
});

btn2.addEventListener('click', function () {
    if (validateStep(form2)) {
        register2.style.display = 'none';
        register3.style.display = 'block';
        stepCircle2.style.background = '#00A2FF';
        stepCircle3.style.background = '#00A2FF';
    }
});

lastBtn.addEventListener('click', function (e) {
    e.preventDefault();
    if (validateStep(form3)) {
        // Submit the whole big form
        document.querySelector('form').submit();
    }
});
