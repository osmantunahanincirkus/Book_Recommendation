<template>
    <Loader v-if="loading"/>
    <div :class="[$store.state.layout_style, $store.state.menu_style]">
        <component v-show="!loading" v-bind:is="layout"></component>
    </div>
</template>
<script setup>
import "./assets/sass/app.scss";
import {computed} from "vue";
import Loader from "../src/components/layout/loader.vue";
import {useMeta} from "./composables/use-meta";
import {useStore} from "vuex";

const store = useStore();
useMeta({title: "Liste"});

const layout = computed(() => {
    return store.getters.layout;
});
const loading = computed(() => {
    return store.getters.getLoading;
});
</script>
<script>
// layouts
import appLayout from "./layouts/app-layout.vue";
import authLayout from "./layouts/auth-layout.vue";

export default {
    components: {
        app: appLayout,
        auth: authLayout,
    },
};
</script>
