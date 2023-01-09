<template>

    <div class="dialog" v-if="show" @click.stop="hideDialog">
        <div @click.stop class="dialog__content">
            <slot>
            
            </slot>
        </div>
    </div>

</template>

<script>

export default {
    name: 'my-dialog',
    props: {
        show: {
            type: Boolean,
            default: false
        }
    },
    methods: {
        hideDialog() {
            this.$emit('update:show', false)
        }
    }
}

</script>

<style> 

.dialog {
    top: 0;
    bottom: 0;
    right: 0;
    left: 0;
    background: (0, 0, 0, 0.5);
    position: fixed;
    display: flex;
    padding: 20px;
}

.dialog__content {
    margin: auto;
    background: rgb(229, 228, 197);
    border-radius: 12px;
    min-width: 500px;
    min-height: 400px;
    padding: 10px;
}

</style>