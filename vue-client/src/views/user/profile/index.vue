<template>
    <div class="layout-px-spacing">
        <div class="row layout-spacing">
            <!-- Content -->
            <div class="col-xl-4 col-lg-6 col-md-5 col-sm-12 layout-top-spacing">
                <div class="user-profile layout-spacing">
                    <div class="panel">
                        <div class="panel-body">
                            <div class="d-flex justify-content-between">
                                <h3 class="pb-3">Profile</h3>
                            </div>
                            <div class="text-center user-info">
                                <img src="/src/assets/images/avatar.jpg" alt="avatar" width="100" height="100"/>
                                <p class="">{{ token.user.user_profile.name }} {{ token.user.user_profile.surname }}</p>
                            </div>
                            <div class="user-info-list">
                                <div class="">
                                    <ul class="contacts-block list-unstyled">
                                        <li class="contacts-block__item">
                                            <a href="mailto:example@mail.com">
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
                                                    class="feather feather-mail"
                                                >
                                                    <path d="M4 4h16c1.1 0 2 .9 2 2v12c0 1.1-.9 2-2 2H4c-1.1 0-2-.9-2-2V6c0-1.1.9-2 2-2z"></path>
                                                    <polyline points="22,6 12,13 2,6"></polyline>
                                                </svg>
                                                {{ token.user.email }}
                                            </a>
                                        </li>
                                    </ul>
                                </div>
                            </div>
                        </div>
                    </div>
                </div>
            </div>

            <div class="col-xl-8 col-lg-6 col-md-7 col-sm-12 layout-top-spacing">
                <div class="statbox panel box box-shadow">
                    <div class="panel-body animated-underline-content tabs">
                        <ul class="nav nav-tabs mb-3 justify-content-between" id="lineTab" role="tablist">
                            <li class="nav-item col-6 text-center">
                                <a class="nav-link active" id="underline-home-anim-tab" data-bs-toggle="tab" href="#underline-home-anim" role="tab" aria-controls="underline-home" aria-selected="true">
                                    Değerlendirdiğin Kitaplar
                                </a>
                            </li>
                            <li class="nav-item col-6 text-center">
                                <a class="nav-link" id="underline-profile-anim-tab" data-bs-toggle="tab" href="#underline-profile-anim" role="tab" aria-controls="underline-profile" aria-selected="false">
                                    Önerilen Kitaplar
                                </a>
                            </li>
                        </ul>

                        <div class="tab-content" id="lineTabContent-3">
                            <div class="tab-pane fade show active" id="underline-home-anim" role="tabpanel" aria-labelledby="underline-home-anim-tab">
                                <div class="row">
                                    <div v-for="book in rateBooks?.rows" class="col-lg-4 col-md-6 mb-lg-0 mb-4 pb-4" style="cursor: pointer" @click="router.push(`/book/${book.product_code}`)">
                                        <div class="card h-100">
                                            <div style="min-height: 400px; max-height: 400px">
                                                <img :src="book.img_l" alt="faq-video-tutorials" class="card-img-top w-100 h-100"/>
                                            </div>
                                            <div class="card-body">
                                                <div class="fq-rating mb-2">
                                                    <svg
                                                        v-for="i in parseInt(book.rate_avg)"
                                                        :key="i" xmlns="http://www.w3.org/2000/svg" width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor"
                                                        stroke-width="2" stroke-linecap="round" stroke-linejoin="round" class="feather feather-star checked"
                                                    >
                                                        <polygon points="12 2 15.09 8.26 22 9.27 17 14.14 18.18 21.02 12 17.77 5.82 21.02 7 14.14 2 9.27 8.91 8.26 12 2"></polygon>
                                                    </svg>
                                                    <svg
                                                        v-for="i in (10 - parseInt(book.rate_avg))"
                                                        :key="i" xmlns="http://www.w3.org/2000/svg" width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor"
                                                        stroke-width="2" stroke-linecap="round" stroke-linejoin="round" class="feather feather-star"
                                                    >
                                                        <polygon points="12 2 15.09 8.26 22 9.27 17 14.14 18.18 21.02 12 17.77 5.82 21.02 7 14.14 2 9.27 8.91 8.26 12 2"></polygon>
                                                    </svg>
                                                </div>
                                                <div class="row align-content-between" style="height: 85%">
                                                    <h6 class="card-title">{{ book.title }}</h6>
                                                    <div>
                                                        <p class="card-text p-0 m-0" style="font-size: 11px">{{ book.author }}</p>
                                                        <p class="card-text" style="font-size: 11px">{{ book.publisher }}</p>
                                                        <p class="meta-text">
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
                                                                class="feather feather-calendar"
                                                            >
                                                                <rect x="3" y="4" width="18" height="18" rx="2" ry="2"></rect>
                                                                <line x1="16" y1="2" x2="16" y2="6"></line>
                                                                <line x1="8" y1="2" x2="8" y2="6"></line>
                                                                <line x1="3" y1="10" x2="21" y2="10"></line>
                                                            </svg>
                                                            {{ book.release_year }}
                                                        </p>
                                                    </div>
                                                </div>
                                            </div>
                                        </div>
                                    </div>
                                </div>

                                <div class="paginating-container pagination-solid flex-column align-items-center">
                                    <ul role="menubar" aria-disabled="false" aria-label="Pagination" class="pagination b-pagination">
                                        <li v-if="rateBooks?.last_page > 1 && rateBooks?.page !== 1" @click="getRateBooks(1)" role="presentation" class="page-item first">
                                            <button role="menuitem" type="button" tabindex="-1" aria-label="Go to first page" class="page-link">
                                                <svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                                                    <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M11 19l-7-7 7-7m8 14l-7-7 7-7"></path>
                                                </svg>
                                            </button>
                                        </li>
                                        <li v-if="rateBooks?.last_page > 1 && rateBooks?.page !== 1" @click="getRateBooks(rateBooks?.page - 1)" role="presentation" class="page-item prev">
                                            <button role="menuitem" type="button" tabindex="-1" aria-label="Go to previous page" class="page-link">
                                                <svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                                                    <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 19l-7-7 7-7"></path>
                                                </svg>
                                            </button>
                                        </li>
                                        <li v-if="rateBooks?.last_page > 1 && rateBooks?.page !== 1" @click="getRateBooks(rateBooks?.page - 1)" role="presentation" class="page-item">
                                            <button role="menuitemradio" type="button" aria-label="Go to page 1" aria-checked="false" aria-posinset="1" aria-setsize="3" tabindex="-1" class="page-link">
                                                {{ rateBooks?.page - 1 }}
                                            </button>
                                        </li>
                                        <li role="presentation" class="page-item active">
                                            <button role="menuitemradio" type="button" aria-label="Go to page 2" aria-checked="true" aria-posinset="2" aria-setsize="3" tabindex="0" class="page-link">
                                                {{ rateBooks?.page }}
                                            </button>
                                        </li>
                                        <li v-if="rateBooks?.last_page > 2 && rateBooks?.page !== rateBooks?.last_page" @click="getRateBooks(rateBooks?.page + 1)" role="presentation" class="page-item">
                                            <button role="menuitemradio" type="button" aria-label="Go to page 3" aria-checked="false" aria-posinset="3" aria-setsize="3" tabindex="-1" class="page-link">
                                                {{ rateBooks?.page + 1 }}
                                            </button>
                                        </li>
                                        <li v-if="rateBooks?.last_page > 2 && rateBooks?.page !== rateBooks?.last_page" @click="getRateBooks(rateBooks?.page + 1)" role="presentation" class="page-item next">
                                            <button role="menuitem" type="button" tabindex="-1" aria-label="Go to next page" class="page-link">
                                                <svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                                                    <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 5l7 7-7 7"></path>
                                                </svg>
                                            </button>
                                        </li>
                                        <li v-if="rateBooks?.last_page > 2 && rateBooks?.page !== rateBooks?.last_page" @click="getRateBooks(rateBooks?.last_page)" role="presentation" class="page-item last">
                                            <button role="menuitem" type="button" tabindex="-1" aria-label="Go to last page" class="page-link">
                                                <svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                                                    <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M13 5l7 7-7 7M5 5l7 7-7 7"></path>
                                                </svg>
                                            </button>
                                        </li>
                                    </ul>
                                </div>
                            </div>
                            <div class="tab-pane fade" id="underline-profile-anim" role="tabpanel" aria-labelledby="underline-profile-anim-tab">
                                <div v-if="!recommendedBooks" class="row">
                                    <div class="loader-div">
                                        <div>
                                            <div class="loader multi-loader mx-auto"></div>
                                        </div>
                                    </div>
                                </div>
                                <div v-if="recommendedBooks" class="row">
                                    <div v-for="book in recommendedBooks?.rows" class="col-lg-4 col-md-6 mb-lg-0 mb-4 pb-4" style="cursor: pointer" @click="router.push(`/book/${book.product_code}`)">
                                        <div class="card h-100">
                                            <div style="min-height: 400px; max-height: 400px">
                                                <img :src="book.img_l" alt="faq-video-tutorials" class="card-img-top w-100 h-100"/>
                                            </div>
                                            <div class="card-body">
                                                <div class="fq-rating mb-2">
                                                    <svg
                                                        v-for="i in parseInt(book.rate_avg)"
                                                        :key="i" xmlns="http://www.w3.org/2000/svg" width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor"
                                                        stroke-width="2" stroke-linecap="round" stroke-linejoin="round" class="feather feather-star checked"
                                                    >
                                                        <polygon points="12 2 15.09 8.26 22 9.27 17 14.14 18.18 21.02 12 17.77 5.82 21.02 7 14.14 2 9.27 8.91 8.26 12 2"></polygon>
                                                    </svg>
                                                    <svg
                                                        v-for="i in (10 - parseInt(book.rate_avg))"
                                                        :key="i" xmlns="http://www.w3.org/2000/svg" width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor"
                                                        stroke-width="2" stroke-linecap="round" stroke-linejoin="round" class="feather feather-star"
                                                    >
                                                        <polygon points="12 2 15.09 8.26 22 9.27 17 14.14 18.18 21.02 12 17.77 5.82 21.02 7 14.14 2 9.27 8.91 8.26 12 2"></polygon>
                                                    </svg>
                                                </div>
                                                <div class="row align-content-between" style="height: 85%">
                                                    <h6 class="card-title">{{ book.title }}</h6>
                                                    <div>
                                                        <p class="card-text p-0 m-0" style="font-size: 11px">{{ book.author }}</p>
                                                        <p class="card-text" style="font-size: 11px">{{ book.publisher }}</p>
                                                        <p class="meta-text">
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
                                                                class="feather feather-calendar"
                                                            >
                                                                <rect x="3" y="4" width="18" height="18" rx="2" ry="2"></rect>
                                                                <line x1="16" y1="2" x2="16" y2="6"></line>
                                                                <line x1="8" y1="2" x2="8" y2="6"></line>
                                                                <line x1="3" y1="10" x2="21" y2="10"></line>
                                                            </svg>
                                                            {{ book.release_year }}
                                                        </p>
                                                    </div>
                                                </div>
                                            </div>
                                        </div>
                                    </div>
                                </div>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </div>
</template>

<style lang="scss" scoped>
.tab-content{
    border: none !important;
}
</style>

<script setup>
import "/src/assets/sass/scrollspyNav.scss";
import "/src/assets/sass/users/user-profile.scss";
import "/src/assets/sass/components/tabs-accordian/custom-tabs.scss";
import {useMeta} from "/src/composables/use-meta";
import {computed, onBeforeMount, ref} from "vue";
import {useStore} from "vuex";
import {toast} from "vue3-toastify";
import {useRoute, useRouter} from "vue-router";

const store = useStore();
store.commit('setLoading', true);
useMeta({title: "Kullanıcı Profili"});
const route = useRoute();
const router = useRouter();
const search = ref(null);
const token = computed(() => {
    return store.getters.getToken;
});
const rateBooks = computed(() => {
    return store.getters["book/getRateBooks"];
});
const getRateBooks = async (rate_page) => {
    try {
        await store.dispatch('book/getRateBooks', {page: rate_page, search: search.value, limit: 9})
        await router.replace({query: {...route.query, rate_page}});
    } catch (err) {
        toast.error(err.message);
    }
};
const recommendedBooks = computed(() => {
    return store.getters["book/getRecommendedBooks"];
});
const getRecommendedBooks = async () => {
    try {
        await store.dispatch('book/getRecommendedBooks', {})
    } catch (err) {
        toast.error(err.message);
    }
};
onBeforeMount(async () => {
    await getRateBooks(route.query.rate_page ?? 1);
    getRecommendedBooks();
    store.commit('setLoading', false);
});
</script>
