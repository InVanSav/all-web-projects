<template>

    <div v-show="files.length > 0">
        <h3>Explorer</h3>
        <FileItem 
            v-for="file in files" 
            v-bind:key="file.id" 
            v-bind:file="file" 
            @remove="$emit('remove',file)"
            @save="$emit('save', file)">
        </FileItem>

    </div>

    <h3 v-show="files.length === 0"><center>Nothing to show yet</center></h3>

</template>

<script>
import FileItem from './FileItem.vue';

export default {
    props: {
        files: {
            type: Array,
            required: true
        }
    },
    components: { FileItem }
}

</script>

<style scoped>
</style>
