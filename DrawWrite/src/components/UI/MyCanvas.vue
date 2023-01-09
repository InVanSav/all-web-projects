<template>

    <div>

        <center>
            <center>
                <h3>Welcome to the field for your work</h3>
            </center>
            <canvas ref="canvas" width="1300" height="600" id='drawing-pad'></canvas>
            <div class="btns">
                <MyButton class="btn" @click='resetCanvas'>Reset</MyButton>
                <MyButton class="btn" @click='getImage'>Save</MyButton>
                <MyButton class="btn" @click='replay'>Replay</MyButton>
            </div>
        </center>

    </div>

</template>


<script>

export default {
    name: 'my-canvas',

    mounted() {
        var vm = this
        vm.canvas = vm.$refs.canvas
        vm.context = vm.canvas.getContext("2d");
        vm.canvas.addEventListener('mousedown', vm.mousedown);
        vm.canvas.addEventListener('mousemove', vm.mousemove)
        document.addEventListener('mouseup', vm.mouseup);
    },

    methods: {
        mousedown(e) {
            var vm = this
            var rect = vm.canvas.getBoundingClientRect();
            var x = e.clientX - rect.left;
            var y = e.clientY - rect.top;

            vm.isDrawing = true;
            vm.startX = x;
            vm.startY = y;
            vm.points.push({
                x: x,
                y: y
            });
        },
        mousemove(e) {
            var vm = this
            var rect = vm.canvas.getBoundingClientRect();
            var x = e.clientX - rect.left;
            var y = e.clientY - rect.top;

            if (vm.isDrawing) {
                vm.context.beginPath();
                vm.context.moveTo(vm.startX, vm.startY);
                vm.context.lineTo(x, y);
                vm.context.lineWidth = 1;
                vm.context.lineCap = 'round';
                vm.context.strokeStyle = "rgba(0,0,0,1)";
                vm.context.stroke();

                vm.startX = x;
                vm.startY = y;

                vm.points.push({
                    x: x,
                    y: y
                });
            }
        },
        mouseup() {
            var vm = this
            vm.isDrawing = false;
            if (vm.points.length > 0) {
                localStorage['points'] = JSON.stringify(vm.points);
            }
            this.points.push('mouseup')
        },
        resetCanvas() {
            var vm = this
            vm.canvas.width = this.canvas.width;
            vm.points.length = 0;
        },
        getImage() {
            var dataURL = this.canvas.toDataURL("image/jpeg");
            var link = document.createElement("a");
            link.href = dataURL;
            link.download = "my-image-name.jpg";
            link.click();

        },
        replay() {
            var vm = this
            vm.canvas.width = this.canvas.width;

            if (vm.points.length === 0) {
                if (localStorage["points"] !== undefined) {
                    vm.points = JSON.parse(localStorage["points"]);
                }
            }

            var point = 1;
            setInterval(function () {
                drawNextPoint(point);
                point += 1;
            }, 10);

            function drawNextPoint(index) {
                if (index >= vm.points.length) {
                    return;
                }
                var startX = vm.points[index - 1].x;
                var startY = vm.points[index - 1].y;

                var x = vm.points[index].x;
                var y = vm.points[index].y;

                vm.context.beginPath();
                vm.context.moveTo(startX, startY);
                vm.context.lineTo(x, y);
                vm.context.lineWidth = 1;
                vm.context.lineCap = 'round';
                vm.context.strokeStyle = "rgba(0,0,0,1)";
                vm.context.stroke();
            }
        },
    }
}
</script>

<style>


h3 {
    margin-bottom: 10px;
}

canvas {
    border: 1px solid darkgoldenrod;
    cursor: crosshair;
    display: block;
}

</style>