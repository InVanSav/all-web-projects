<template>

    <div class="app">

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

        <h1>Comments</h1>
        <MyButton class="btn" style="margin: 10px; margin-bottom: 20px" @click="showDialog">
            Add comment
        </MyButton>
        <MyDialog class="dialog" v-model:show="dialogVisible">
            <file-create @create="createBoard" />
        </MyDialog>

        <file-list :files="files" @remove="removeFile" @save="textToFile" />

    </div>

</template>

<script>

import FileList from './components/FileList.vue'
import FileCreate from './components/FileCreate.vue'
import MyDialog from './components/UI/MyDialog.vue'
import MyButton from './components/UI/MyButton.vue'

export default {
    components: {
        FileList,
        FileCreate,
        MyDialog,
        MyButton
    },
    data() {
        return {
            canvas: null,
            context: null,
            isDrawing: false,
            startX: 0,
            startY: 0,
            points: [],
            files: [],
            dialogVisible: false,
            visible: false
        }
    },
    mounted() {
        var vm = this
        vm.canvas = vm.$refs.canvas
        vm.context = vm.canvas.getContext("2d");
        vm.canvas.addEventListener('mousedown', vm.mousedown);
        vm.canvas.addEventListener('mousemove', vm.mousemove)
        document.addEventListener('mouseup', vm.mouseup);
    },
    methods: {
        createBoard(file) {
            this.files.push(file)
            this.dialogVisible = false
        },
        removeFile(file) {
            this.files = this.files.filter(p => p.id !== file.id)
        },
        textToFile(file) {
            const b = new Blob([file.title, file.body], { type: 'text/plain' });
            const url = window.URL.createObjectURL(b);
            const a = document.createElement('a');
            a.href = url;
            a.download = file.title || 'text.txt';
            a.type = 'text/plain';
            a.addEventListener('click', () => {
                setTimeout(() => window.URL.revokeObjectURL(url), 10000);
            })
            a.click()
        },
        showDialog() {
            this.dialogVisible = true
        },
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
                vm.context.strokeStyle = "rgba(93, 83, 82, 1)";
                vm.context.lineWidth = 3;
                vm.context.lineCap = 'round';
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
                vm.context.strokeStyle = "rgba(93, 83, 82, 1)";
                vm.context.lineWidth = 3;
                vm.context.lineCap = 'round';
                vm.context.stroke();
            }
        },
    }
}

</script>

<style>
* {
    margin: 0;
    padding: 0;
    box-sizing: border-box;
    background: rgb(229, 228, 197);
}

::-webkit-scrollbar {
    display: none;
}

.app {
    margin: 20px;
    margin-bottom: 60px;
    overflow: hidden;
    font-family: cursive;
}

canvas {
    cursor: crosshair;
}

h3 {
    margin-bottom: 10px;
}

h1 {
    margin-top: 20px;
    margin-left: 10px;
}

.btns {
    margin: 20px;
    width: 250px;
    display: flex;
    justify-content: space-between;
    float: right;

}

.dialog {
    top: 0;
    bottom: 0;
    right: 0;
    left: 0;
    background: (0, 0, 0, 0.5);
    position: fixed;
    display: flex;
}

.dialog__content {
    margin: auto;
    background: rgb(102, 102, 102);
    border-radius: 12px;
    min-width: 500px;
    min-height: 400px;
    padding: 10px;
}
</style>
