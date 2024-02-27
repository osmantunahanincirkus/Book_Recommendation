<template>
    <div class="layout-px-spacing mt-4">
        <div class="faq container">
            <div class="faq-layouting layout-spacing">
                <div class="fq-article-section">
                    <div class="row col-12 m-0 p-0 mb-3 align-items-center">
                        <div class="row col-sm-6 col-12 m-0 p-0 align-items-center justify-content-start">
                            <h2 class="p-0 m-0">Kitap Listesi</h2>
                        </div>
                        <div class="row col-sm-6 col-12 m-0 p-0 align-items-center justify-content-end">
                            <div class="input-group m-0 p-0">
                                <input v-model="search" type="text" class="form-control" :placeholder="$t('search')" :aria-label="$t('search')"/>
                                <button @click="getBooks(1)" class="btn btn-primary" type="button">
                                    <svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor"
                                         stroke-width="2" stroke-linecap="round" stroke-linejoin="round" class="feather feather-search toggle-search">
                                        <circle cx="11" cy="11" r="8"></circle>
                                        <line x1="21" y1="21" x2="16.65" y2="16.65"></line>
                                    </svg>
                                </button>
                            </div>
                        </div>
                    </div>

                    <div class="row">
                        <div v-for="book in books?.rows" class="col-lg-3 col-md-6 mb-lg-0 mb-4 pb-4" style="cursor: pointer" @click="router.push(`/book/${book.product_code}`)">
                            <div class="card h-100">
                                <div style="min-height: 400px; max-height: 400px">
                                    <img :src="book.img_l" alt="faq-video-tutorials" class="card-img-top w-100 h-100"/>
                                </div>
                                <div class="card-body">
                                    <div class="fq-rating">
                                        <svg
                                            v-for="i in parseInt(book.rate_avg)"
                                            :key="i" xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor"
                                            stroke-width="2" stroke-linecap="round" stroke-linejoin="round" class="feather feather-star checked"
                                        >
                                            <polygon points="12 2 15.09 8.26 22 9.27 17 14.14 18.18 21.02 12 17.77 5.82 21.02 7 14.14 2 9.27 8.91 8.26 12 2"></polygon>
                                        </svg>
                                        <svg
                                            v-for="i in (10 - parseInt(book.rate_avg))"
                                            :key="i" xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor"
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
                            <li v-if="books?.last_page > 1 && books?.page !== 1" @click="getBooks(1)" role="presentation" class="page-item first">
                                <button role="menuitem" type="button" tabindex="-1" aria-label="Go to first page" class="page-link">
                                    <svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                                        <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M11 19l-7-7 7-7m8 14l-7-7 7-7"></path>
                                    </svg>
                                </button>
                            </li>
                            <li v-if="books?.last_page > 1 && books?.page !== 1" @click="getBooks(books?.page - 1)" role="presentation" class="page-item prev">
                                <button role="menuitem" type="button" tabindex="-1" aria-label="Go to previous page" class="page-link">
                                    <svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                                        <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 19l-7-7 7-7"></path>
                                    </svg>
                                </button>
                            </li>
                            <li v-if="books?.last_page > 1 && books?.page !== 1" @click="getBooks(books?.page - 1)" role="presentation" class="page-item">
                                <button role="menuitemradio" type="button" aria-label="Go to page 1" aria-checked="false" aria-posinset="1" aria-setsize="3" tabindex="-1" class="page-link">
                                    {{ books?.page - 1 }}
                                </button>
                            </li>
                            <li role="presentation" class="page-item active">
                                <button role="menuitemradio" type="button" aria-label="Go to page 2" aria-checked="true" aria-posinset="2" aria-setsize="3" tabindex="0" class="page-link">
                                    {{ books?.page }}
                                </button>
                            </li>
                            <li v-if="books?.last_page > 2 && books?.page !== books?.last_page" @click="getBooks(books?.page + 1)" role="presentation" class="page-item">
                                <button role="menuitemradio" type="button" aria-label="Go to page 3" aria-checked="false" aria-posinset="3" aria-setsize="3" tabindex="-1" class="page-link">
                                    {{ books?.page + 1 }}
                                </button>
                            </li>
                            <li v-if="books?.last_page > 2 && books?.page !== books?.last_page" @click="getBooks(books?.page + 1)" role="presentation" class="page-item next">
                                <button role="menuitem" type="button" tabindex="-1" aria-label="Go to next page" class="page-link">
                                    <svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                                        <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 5l7 7-7 7"></path>
                                    </svg>
                                </button>
                            </li>
                            <li v-if="books?.last_page > 2 && books?.page !== books?.last_page" @click="getBooks(books?.last_page)" role="presentation" class="page-item last">
                                <button role="menuitem" type="button" tabindex="-1" aria-label="Go to last page" class="page-link">
                                    <svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                                        <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M13 5l7 7-7 7M5 5l7 7-7 7"></path>
                                    </svg>
                                </button>
                            </li>
                        </ul>
                    </div>
                </div>
            </div>
        </div>
    </div>
</template>

<script setup>
import "/src/assets/sass/pages/faq/faq.scss";
import {useStore} from 'vuex'
import {useMeta} from "/src/composables/use-meta";
import {useRoute, useRouter} from "vue-router";
import {computed, onBeforeMount, ref} from 'vue'
import {toast} from "vue3-toastify";

const store = useStore();
store.commit('setLoading', true);
useMeta({title: "Liste"});
const route = useRoute();
const router = useRouter();
const search = ref(null);

const books = computed(() => {
    return store.getters["book/getBooks"];
});
const getBooks = async (page) => {
    try {
        await store.dispatch('book/getBooks', {page, search: search.value})
        await router.replace({query: {...route.query, page: page}});
    } catch (err) {
        toast.error(err.message);
    }
}
onBeforeMount(async () => {
    await getBooks(route.query.page ?? 1);
    store.commit('setLoading', false);
})
</script>
