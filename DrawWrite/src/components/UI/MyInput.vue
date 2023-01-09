<template>

    <input :value="modelValue" @input="updateInput" class="input" type="text">

</template>

<script>

export default {
    name: 'my-input',
    props: {
        modelValue: {String, Number}
    },
    methods: {
        updateInput(event) {
            this.$emit('update:modelValue', event.target.value)
        }
    },
}

</script>

<style>

.input {
    width: 100%;
    height: 40px;
    border: 2px solid rgb(233, 144, 114);
    border-radius: 12px;
    padding: 10px;
    margin-top: 15px;
}

</style>