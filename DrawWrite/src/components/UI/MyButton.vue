<template>

    <button>
        <slot></slot>
    </button>

</template>

<script>

export default {
    name: 'my-button'
}

</script>

<style>

.btn {
    padding: 10px;
    background: none;
    color: rgb(233, 144, 114);
    font-size: 15pt;
    border: 2px solid rgb(233, 144, 114);
    border-radius: 12px;
}

</style>