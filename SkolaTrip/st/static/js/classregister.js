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

addEventListener('DOMContentLoaded', function () {
    container.style.display = 'block';
    register2.style.display = 'none';
    register3.style.display = 'none';
    stepCircle2.style.background = '#D9D9D9';
    stepCircle3.style.background = '#D9D9D9';
})

btn1.addEventListener('click', function () {
    container.style.display = 'none';
    register2.style.display = 'block';
    register3.style.display = 'none';
    stepCircle.style.background = '#00A2FF';
});

btn2.addEventListener('click', function () {
    register2.style.display = 'none';
    register3.style.display = 'block';
    stepCircle2.style.background = '#00A2FF';
    stepCircle3.style.background = '#00A2FF';
});

lastBtn.addEventListener('click', function () {
    let form = document.createElement('form');
    form.method = 'POST';
    form.action = "{% url 'classregister' %}";

    let csrfToken = document.querySelector('[name=csrfmiddlewaretoken]').value;
    let csrfField = document.createElement('input');
    csrfField.type = 'hidden';
    csrfField.name = 'csrfmiddlewaretoken';
    csrfField.value = csrfToken;
    form.appendChild(csrfField);

    let inputs = document.querySelectorAll('input, textarea');
    inputs.forEach(input => {
        let clone = input.cloneNode(true);
        form.appendChild(clone);
    });

    document.body.appendChild(form);
    form.submit();
});
