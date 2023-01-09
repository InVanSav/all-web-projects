<template>

    <form @submit.prevent>
        <h4>Make comment</h4>
        <MyInput v-model="file.title" type="text" placeholder="Title"></MyInput>
        <MyInput v-model="file.body" type="text" placeholder="Description"></MyInput>
        <MyButton class="btn" style="align-self: flex-end; margin-top: 15px" @click="createBoard">Enter comment
        </MyButton>
    </form>

</template>

<script>
import MyInput from './UI/MyInput.vue';

export default {
    data() {
        return {
            file: {
                title: "",
                body: ""
            }
        };
    },
    methods: {
        createBoard() {
            this.file.id = Date.now();
            this.$emit("create", this.file);
            this.file = {
                title: "",
                body: ""
            };
        }
    },
    components: { MyInput }
}

</script>

<style scoped>
form {
    display: flex;
    flex-direction: column;
    border-radius: 12px;
    background: rgb(229, 228, 197);
    padding: 20px;
}
</style>