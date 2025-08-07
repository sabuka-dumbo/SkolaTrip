let container = document.querySelector('.container');
let register2 = document.querySelector('.register2');
let register3 = document.querySelector('.register3');

let form1 = document.querySelector('.container-form');
let form2 = document.querySelector('.register2-form');

let stepCircle = document.getElementById('step-circle1');
let stepCircle2 = document.getElementById('step-circle2');
let stepCircle3 = document.getElementById('step-circle3');

let btn1 = document.querySelector('.container-form button');
let btn2 = document.querySelector('.register2-form button');
let lastBtn = document.getElementById('last-btn');

window.addEventListener('load', () => {
    let form1Completed = localStorage.getItem('form1Completed');
    let form2Completed = localStorage.getItem('form2Completed');

    if (form2Completed === 'true') {
        container.style.display = 'none';
        register2.style.display = 'none';
        register3.style.display = 'block';
        stepCircle.style.background = '#00A2FF';
        stepCircle2.style.background = '#00A2FF';
        stepCircle3.style.background = '#00A2FF';
    } else if (form1Completed === 'true') {
        container.style.display = 'none';
        register2.style.display = 'block';
        register3.style.display = 'none';
        stepCircle.style.background = '#00A2FF';
    } else {
        container.style.display = 'block';
        register2.style.display = 'none';
        register3.style.display = 'none';
    }
});

// Step 1 → Step 2
btn1.addEventListener('click', function () {
    container.style.display = 'none';
    register2.style.display = 'block';
    register3.style.display = 'none';
    stepCircle.style.background = '#00A2FF';
    localStorage.setItem('form1Completed', 'true');
});

// Step 2 → Step 3
btn2.addEventListener('click', function () {
    register2.style.display = 'none';
    register3.style.display = 'block';
    stepCircle2.style.background = '#00A2FF';
    stepCircle3.style.background = '#00A2FF';
    localStorage.setItem('form2Completed', 'true');
});

// Final submit
lastBtn.addEventListener('click', function () {
    // Collect data manually into hidden form for Django
    let form = document.createElement('form');
    form.method = 'POST';
    form.action = "{% url 'classregister' %}";

    // Add CSRF token
    let csrfToken = document.querySelector('[name=csrfmiddlewaretoken]').value;
    let csrfField = document.createElement('input');
    csrfField.type = 'hidden';
    csrfField.name = 'csrfmiddlewaretoken';
    csrfField.value = csrfToken;
    form.appendChild(csrfField);

    // Collect all inputs
    let inputs = document.querySelectorAll('input, textarea');
    inputs.forEach(input => {
        let clone = input.cloneNode(true);
        form.appendChild(clone);
    });

    document.body.appendChild(form);
    form.submit();
});
