var canvas = document.getElementById('canvas');
var ctx = canvas.getContext('2d');
var dpi = window.devicePixelRatio;

function fix_dpi() {
    function styleValue(attr) {
        return getComputedStyle(canvas).getPropertyValue(attr).slice(0, -2);
    }
    canvas.setAttribute('width', dpi * styleValue('width'));
    canvas.setAttribute('height', dpi * styleValue('height'));
}

var points, angle;
function draw() {
    var w = canvas.width, h = canvas.height;
    ctx.lineWidth = 1;
    ctx.strokeStyle = 'black';
    ctx.clearRect(0, 0, canvas.width, canvas.height);
    var x = w/2, y = h/2;
    ctx.beginPath();
    ctx.moveTo(x, y);
    for (i = 1; i < points; i++) {
        ctx.lineTo(x + i*Math.sin(i*angle), y + i*Math.cos(i*angle));
    }
    ctx.stroke();
}

function init() {
    fix_dpi();
    var a_in = document.getElementById('angle');
    var p_in = document.getElementById('points');
    var a_out = document.getElementById('angle_span');
    var p_out = document.getElementById('points_span');
    f = function () {
        angle = a_in.value/1000;
        points = p_in.value;
        a_out.innerHTML = angle;
        p_out.innerHTML = points;
        draw();
    }
    a_in.oninput = f;
    p_in.oninput = f;
    f();
}

init();
