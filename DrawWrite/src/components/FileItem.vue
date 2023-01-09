<template>

    <div class="file">

        <div>
            <div><strong>{{ file.title }}</strong></div>
            <div><strong>{{ file.body }}</strong></div>
        </div>
        <div class="file__btns">
            <MyButton class="btn" @click="$emit('save', file)">Save</MyButton>
            <MyButton class="btn" @click="$emit('remove', file)">Delete</MyButton>
        </div>

    </div>

</template>

<script>

export default {
    props: {
        file: {
            type: Object,
            required: true
        }
    },
}

</script>

<style scoped>
.file {
    padding: 15px;
    border: 2px solid rgb(233, 144, 114);
    border-radius: 12px;
    margin-top: 15px;
    display: flex;
    align-items: center;
    justify-content: space-between;
}

.file__btns {
    width: 170px;
    display: flex;
    justify-content: space-between;
}
</style>