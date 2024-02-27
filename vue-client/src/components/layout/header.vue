<template>
    <div>
        <!--  BEGIN NAVBAR  -->
        <div class="header-container fixed-top">
            <header class="header navbar navbar-expand-sm">
                <ul class="navbar-item theme-brand flex-row text-center">
                    <li class="nav-item theme-logo">
                        <router-link to="/">
                            <img src="/src/assets/images/logo.png" class="navbar-logo" alt="logo"/>
                        </router-link>
                    </li>
                    <!--                    <li class="nav-item theme-text">-->
                    <!--                        <router-link to="/" class="nav-link"> CORK </router-link>-->
                    <!--                    </li>-->
                </ul>
                <div class="d-none horizontal-menu">
                    <a href="javascript:void(0);" class="sidebarCollapse" data-placement="bottom" @click="$store.commit('toggleSideBar', !$store.state.is_show_sidebar)">
                        <svg
                            xmlns="http://www.w3.org/2000/svg"
                            width="24"
                            height="24"
                            viewBox="0 0 24 24"
                            fill="none"
                            stroke="currentColor"
                            stroke-width="2"
                            stroke-linecap="round"
                            stroke-linejoin="round"
                            class="feather feather-menu"
                        >
                            <line x1="3" y1="12" x2="21" y2="12"></line>
                            <line x1="3" y1="6" x2="21" y2="6"></line>
                            <line x1="3" y1="18" x2="21" y2="18"></line>
                        </svg>
                    </a>
                </div>
                <div class="navbar-item flex-row ms-md-auto">
                    <!-- Button trigger modal -->
                    <button v-if="!token" type="button" class="btn btn-dark me-2" data-bs-toggle="modal" data-bs-target="#registerModal">Kayıt Ol</button>
                    <button v-if="!token" type="button" class="btn btn-info" data-bs-toggle="modal" data-bs-target="#loginModal">Giriş</button>
                    <div v-if="token" class="dropdown nav-item user-profile-dropdown btn-group">
                        <a href="javascript:;" id="ddluser" data-bs-toggle="dropdown" aria-expanded="false" class="btn dropdown-toggle btn-icon-only user nav-link">
                            <img src="/src/assets/images/avatar.jpg" alt="avatar" class="header-avatar"/>
                        </a>
                        <ul class="dropdown-menu dropdown-menu-right m-0" aria-labelledby="ddluser">
                            <li role="presentation">
                                <router-link to="/user/profile" class="dropdown-item">
                                    <svg
                                        xmlns="http://www.w3.org/2000/svg"
                                        width="24"
                                        height="24"
                                        viewBox="0 0 24 24"
                                        fill="none"
                                        stroke="currentColor"
                                        stroke-width="2"
                                        stroke-linecap="round"
                                        stroke-linejoin="round"
                                        class="feather feather-user"
                                    >
                                        <path d="M20 21v-2a4 4 0 0 0-4-4H8a4 4 0 0 0-4 4v2"></path>
                                        <circle cx="12" cy="7" r="4"></circle>
                                    </svg>
                                    Profile
                                </router-link>
                            </li>
                            <li role="presentation">
                                <router-link to="" class="dropdown-item" @click="logout">
                                    <svg
                                        xmlns="http://www.w3.org/2000/svg"
                                        width="24"
                                        height="24"
                                        viewBox="0 0 24 24"
                                        fill="none"
                                        stroke="currentColor"
                                        stroke-width="2"
                                        stroke-linecap="round"
                                        stroke-linejoin="round"
                                        class="feather feather-log-out"
                                    >
                                        <path d="M9 21H5a2 2 0 0 1-2-2V5a2 2 0 0 1 2-2h4"></path>
                                        <polyline points="16 17 21 12 16 7"></polyline>
                                        <line x1="21" y1="12" x2="9" y2="12"></line>
                                    </svg>
                                    Sign Out
                                </router-link>
                            </li>
                        </ul>
                    </div>
                </div>
            </header>
        </div>
        <!--  END NAVBAR  -->
        <!--  BEGIN NAVBAR  -->
        <div class="sub-header-container">
            <header class="header navbar navbar-expand-sm">
                <a href="javascript:void(0);" class="sidebarCollapse" data-placement="bottom" @click="$store.commit('toggleSideBar', !$store.state.is_show_sidebar)">
                    <svg
                        xmlns="http://www.w3.org/2000/svg"
                        width="24"
                        height="24"
                        viewBox="0 0 24 24"
                        fill="none"
                        stroke="currentColor"
                        stroke-width="2"
                        stroke-linecap="round"
                        stroke-linejoin="round"
                        class="feather feather-menu"
                    >
                        <line x1="3" y1="12" x2="21" y2="12"></line>
                        <line x1="3" y1="6" x2="21" y2="6"></line>
                        <line x1="3" y1="18" x2="21" y2="18"></line>
                    </svg>
                </a>

                <!-- Portal vue/Teleport for Breadcrumb -->
                <div id="breadcrumb" class="vue-portal-target"></div>
            </header>
        </div>
        <!--  END NAVBAR  -->
        <!--  BEGIN TOPBAR  -->
        <div class="topbar-nav header navbar" role="banner">
            <nav class="topbar">
                <ul class="list-unstyled menu-categories" id="topAccordion">
                    <li class="menu single-menu">
                        <router-link to="/">
                            <div class="">
                                <svg
                                    xmlns="http://www.w3.org/2000/svg"
                                    width="24"
                                    height="24"
                                    viewBox="0 0 24 24"
                                    fill="none"
                                    stroke="currentColor"
                                    stroke-width="2"
                                    stroke-linecap="round"
                                    stroke-linejoin="round"
                                    class="feather feather-home"
                                >
                                    <path d="M3 9l9-7 9 7v11a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2z"></path>
                                    <polyline points="9 22 9 12 15 12 15 22"></polyline>
                                </svg>
                                <span>{{ $t('home') }}</span>
                            </div>
                        </router-link>
                    </li>

                    <!--                    <li class="menu single-menu">-->
                    <!--                        <a href="javascript:;" class="dropdown-toggle autodroprown">-->
                    <!--                            <div class="">-->
                    <!--                                <svg-->
                    <!--                                    xmlns="http://www.w3.org/2000/svg"-->
                    <!--                                    width="24"-->
                    <!--                                    height="24"-->
                    <!--                                    viewBox="0 0 24 24"-->
                    <!--                                    fill="none"-->
                    <!--                                    stroke="currentColor"-->
                    <!--                                    stroke-width="2"-->
                    <!--                                    stroke-linecap="round"-->
                    <!--                                    stroke-linejoin="round"-->
                    <!--                                    class="feather feather-home"-->
                    <!--                                >-->
                    <!--                                    <path d="M3 9l9-7 9 7v11a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2z"></path>-->
                    <!--                                    <polyline points="9 22 9 12 15 12 15 22"></polyline>-->
                    <!--                                </svg>-->
                    <!--                                <span>{{ $t('dashboard') }}</span>-->
                    <!--                            </div>-->
                    <!--                            <svg-->
                    <!--                                xmlns="http://www.w3.org/2000/svg"-->
                    <!--                                width="24"-->
                    <!--                                height="24"-->
                    <!--                                viewBox="0 0 24 24"-->
                    <!--                                fill="none"-->
                    <!--                                stroke="currentColor"-->
                    <!--                                stroke-width="2"-->
                    <!--                                stroke-linecap="round"-->
                    <!--                                stroke-linejoin="round"-->
                    <!--                                class="feather feather-chevron-down"-->
                    <!--                            >-->
                    <!--                                <polyline points="6 9 12 15 18 9"></polyline>-->
                    <!--                            </svg>-->
                    <!--                        </a>-->
                    <!--                        <ul class="collapse submenu list-unstyled">-->
                    <!--                            <li>-->
                    <!--                                <router-link to="/"> {{ $t('sales') }} </router-link>-->
                    <!--                            </li>-->
                    <!--                            <li>-->
                    <!--                                <router-link to="/index2">{{ $t('analytics') }}</router-link>-->
                    <!--                            </li>-->
                    <!--                        </ul>-->
                    <!--                    </li>-->
                </ul>
            </nav>
        </div>
        <!--  END TOPBAR  -->
    </div>
    <Login/>
    <Register/>
</template>

<style lang="scss" scoped>
.navbar {
    .theme-brand {
        li.theme-logo {
            img {
                width: auto;
                height: 50px;
                padding: 5px 0;
            }
        }
    }
}

.header-avatar {
    width: 50px !important;
    height: 50px !important;
}
</style>

<script setup>
import {onMounted, ref, computed} from 'vue';
import {useStore} from 'vuex';
import {toast} from "vue3-toastify";
import Login from '../../../src/views/components/auth/login.vue'
import Register from '../../../src/views/components/auth/register.vue'

const store = useStore();
const selectedLang = ref(null);

const token = computed(() => {
    return store.getters.getToken;
});
onMounted(() => {
    selectedLang.value = window.$appSetting.toggleLanguage();
    toggleMode();
});
const toggleMode = (mode) => {
    window.$appSetting.toggleMode(mode);
};
const logout = async () => {
    try {
        await store.dispatch('auth/logout');
        toast.success('Çıkış Başarılı');
        window.location.reload();
    } catch (err) {
        toast.error(err.message);
    }
};
</script>
