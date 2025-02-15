<template>
    <div id="app" class="flex">
        <div class="sidebar-container">
            <Sidebar />
        </div>
        <div class="content-container flex-1">
            <router-view />
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
}

.sidebar-container {
    width: 85px;
}

.content-container {
    flex: 1;
    padding: 20px;
    background: #f0f4ff;
}
</style>
