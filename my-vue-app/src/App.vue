<template>
    <div id="app" class="flex">
        <div class="sidebar-container">
            <Sidebar />
        </div>
        <div class="content-container flex-1">
            <router-view /> <!-- This will display the dynamic content based on the route -->
        </div>
    </div>
</template>

<script lang="ts">
import { defineComponent } from 'vue';
import Sidebar from "./components/Sidebar.vue";
export default defineComponent({
    name: 'App',
    components: {
        Sidebar
    }
});
</script>

<style scoped>
#app {
    display: flex;
    height: 100vh;
    /* Ensures the layout takes up the full screen height */
}

.sidebar-container {
    width: 85px;
    /* Sidebar width */
}

.content-container {
    flex: 1;
    /* Ensures the content page takes up the remaining space */
    padding: 20px;
    background: #f0f4ff;
}
</style>
