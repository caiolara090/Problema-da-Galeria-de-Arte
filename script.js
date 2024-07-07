document.addEventListener('DOMContentLoaded', () => {
    const canvas = document.getElementById('canvas');
    const ctx = canvas.getContext('2d');
    canvas.width = 800;
    canvas.height = 600;

    let points = [
        { x: 100, y: 100 },
        { x: 700, y: 100 },
        { x: 700, y: 500 },
        { x: 100, y: 500 }
    ];

    function drawPolygon(points) {
        ctx.clearRect(0, 0, canvas.width, canvas.height);
        ctx.beginPath();
        ctx.moveTo(points[0].x, points[0].y);
        for (let i = 1; i < points.length; i++) {
            ctx.lineTo(points[i].x, points[i].y);
        }
        ctx.closePath();
        ctx.stroke();
    }

    function handleDrag(e) {
        const rect = canvas.getBoundingClientRect();
        const mouseX = e.clientX - rect.left;
        const mouseY = e.clientY - rect.top;

        points.forEach(point => {
            const dx = mouseX - point.x;
            const dy = mouseY - point.y;
            if (Math.sqrt(dx * dx + dy * dy) < 10) {
                point.x = mouseX;
                point.y = mouseY;
            }
        });

        drawPolygon(points);
    }

    canvas.addEventListener('mousedown', () => {
        canvas.addEventListener('mousemove', handleDrag);
    });

    canvas.addEventListener('mouseup', () => {
        canvas.removeEventListener('mousemove', handleDrag);
    });

    drawPolygon(points);
});
