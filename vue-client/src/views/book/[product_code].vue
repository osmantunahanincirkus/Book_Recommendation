<template>
    <div class="layout-px-spacing">
        <div class="fq-header-wrapper pt-4">
            <div class="container">
                <div class="row">
                    <div class="col-md-8 align-self-center order-md-0 order-1">
                        <h4>{{ book?.title }}</h4>
                        <table class="border-bottom">
                            <tbody>
                            <tr>
                                <td>Yayın Evi</td>
                                <td class="ps-1 pe-2">:</td>
                                <td>{{ book?.publisher }}</td>
                            </tr>
                            <tr>
                                <td>Yazar</td>
                                <td class="ps-1 pe-2">:</td>
                                <td>{{ book?.author }}</td>
                            </tr>
                            <tr>
                                <td>Yayın Yılı</td>
                                <td class="ps-1 pe-2">:</td>
                                <td>{{ book?.release_year }}</td>
                            </tr>
                            <tr>
                                <td colspan="3">&nbsp;</td>
                            </tr>
                            <tr v-if="book">
                                <td colspan="3">
                                    <div class="fq-rating">
                                        <svg
                                            v-for="i in parseInt(book?.rate_avg)"
                                            :key="i" xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor"
                                            stroke-width="2" stroke-linecap="round" stroke-linejoin="round" class="feather feather-star checked"
                                        >
                                            <polygon points="12 2 15.09 8.26 22 9.27 17 14.14 18.18 21.02 12 17.77 5.82 21.02 7 14.14 2 9.27 8.91 8.26 12 2"></polygon>
                                        </svg>
                                        <svg
                                            v-for="i in (10 - parseInt(book?.rate_avg))"
                                            :key="i" xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor"
                                            stroke-width="2" stroke-linecap="round" stroke-linejoin="round" class="feather feather-star"
                                        >
                                            <polygon points="12 2 15.09 8.26 22 9.27 17 14.14 18.18 21.02 12 17.77 5.82 21.02 7 14.14 2 9.27 8.91 8.26 12 2"></polygon>
                                        </svg>
                                    </div>
                                </td>
                            </tr>
                            <tr>
                                <td colspan="3">&nbsp;</td>
                            </tr>
                            </tbody>
                        </table>
                        <table class="mt-4">
                            <tbody>
                            <tr v-if="token && !book?.me_rate">
                                <td colspan="3">
                                    <button type="button" class="btn btn-primary" data-bs-toggle="modal" data-bs-target="#bookRateModal">Değerlendir</button>
                                </td>
                            </tr>
                            <tr v-if="token && book?.me_rate">
                                <td>Senin değerlendirmen</td>
                                <td class="ps-1 pe-2">:</td>
                                <td>
                                    <span class="btn btn-outline-info rounded-pill pill-rate">
                                        {{ book?.me_rate?.rate }}
                                    </span>
                                </td>
                            </tr>
                            <tr v-if="token && book?.me_comment">
                                <td>Senin yorumun</td>
                                <td class="ps-1 pe-2">:</td>
                                <td>
                                    {{ book?.me_comment?.comment }}
                                </td>
                            </tr>
                            </tbody>
                        </table>
                    </div>
                    <div class="col-md-4 order-md-0 order-0">
                        <div class="banner-img">
                            <img :src="book?.img_l" class="d-block float-end" alt="header-image" style="width: auto; height: 500px"/>
                        </div>
                    </div>
                </div>
            </div>
        </div>

        <div class="layout-px-spacing">
            <div class="statbox box box-shadow">
                <div class="container">
                    <div class="panel-heading">
                        <div class="col-12 d-flex align-items-center mb-3 mt-3 justify-content-between">
                            <h4 class="m-0 me-2">Yorumlar</h4>
                            <button v-if="token && !book?.me_comment" type="button" class="btn btn-primary" data-bs-toggle="modal" data-bs-target="#bookCommentModal">Yorum yap</button>
                        </div>
                    </div>
                    <div class="panel-body">
                        <div class="col-12 layout-spacing pb-3">
                            <div class="widget widget-visitor-by-browser">
                                <div class="widget-content p-3 rounded-pill">
                                    <div v-if="book && book.book_analysis && book.book_comment_total_count" v-for="book_analysis in book.book_analysis" class="browser-list">
                                        <div :class="`w-icon ${bgColor.icon[book_analysis.id]}`">
                                            <img v-if="book_analysis.id === 1" src="/src/assets/images/book-analysis/1.svg" width="20" class="" alt="...">
                                            <img v-if="book_analysis.id === 2" src="/src/assets/images/book-analysis/2.svg" width="20" class="" alt="...">
                                            <img v-if="book_analysis.id === 3" src="/src/assets/images/book-analysis/3.svg" width="20" class="" alt="...">
                                        </div>
                                        <div class="w-browser-details">
                                            <div class="w-browser-info">
                                                <h6>{{book_analysis.name}}</h6>
                                                <p class="browser-count">{{((book_analysis.count * 100) / book.book_comment_total_count).toFixed(0)}}%</p>
                                            </div>
                                            <div class="w-browser-stats">
                                                <div class="progress">
                                                    <div role="progressbar" aria-valuemin="0" aria-valuemax="100" :aria-valuenow="((book_analysis.count * 100) / book.book_comment_total_count).toFixed(0)" :class="`progress-bar ${bgColor.bar[book_analysis.id]}`" :style="`width: ${((book_analysis.count * 100) / book.book_comment_total_count).toFixed(0)}%`"></div>
                                                </div>
                                            </div>
                                        </div>
                                    </div>
                                </div>
                            </div>
                        </div>
                        <div v-if="book && book.book_comments" v-for="book_comment in book.book_comments" class="card component-card_4 mb-3">
                            <div class="card-body">
                                <div class="user-profile">
                                    <img src="/src/assets/images/avatar.jpg" width="100" class="" alt="..."/>
                                </div>
                                <div class="user-info">
                                    <h5 class="card-user_name">{{ book_comment?.user?.user_profile?.name }} {{ book_comment?.user?.user_profile?.surname }}</h5>
                                    <!--                                    <p class="card-user_occupation">Manager</p>-->
                                    <div class="card-star_rating">
                                        <span v-if="book_comment?.book_analysis_tag?.id === 1" class="badge badge-primary">{{ book_comment?.book_analysis_tag?.name }}</span>
                                        <span v-if="book_comment?.book_analysis_tag?.id === 2" class="badge badge-success">{{ book_comment?.book_analysis_tag?.name }}</span>
                                        <span v-if="book_comment?.book_analysis_tag?.id === 3" class="badge badge-danger">{{ book_comment?.book_analysis_tag?.name }}</span>
                                    </div>
                                    <p class="card-text">{{ book_comment?.comment }}</p>
                                </div>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </div>

        <BookRate v-if="token && !book?.me_rate" v-model:rate="rate" :product_code="productCode"/>
        <BookComment v-if="token && !book?.me_comment" :product_code="productCode"/>
    </div>
</template>

<style lang="scss" scoped>
.component-card_4 {
    width: 100%
}

.feather-star.checked {
    fill: white;
}

.pill-rate {
    width: 25px;
    height: 25px;
}
</style>

<script setup>
import "/src/assets/sass/components/cards/card.scss";
import "/src/assets/sass/widgets/widgets.scss";
import {useStore} from "vuex";
import {useMeta} from "/src/composables/use-meta";
import {useRoute} from "vue-router";
import {computed, onBeforeMount, ref} from 'vue'
import BookRate from '../components/book/rate.vue'
import BookComment from '../components/book/comment.vue'

const store = useStore();
store.commit('setLoading', true);
useMeta({title: "Kitap detayı"});
const route = useRoute();
const search = ref(null);
const rate = ref(1);
const productCode = ref(route.params.product_code);
const bgColor = ref({
    icon: {
        1: 'bg-primary',
        2: 'bg-success',
        3: 'bg-danger'
    },
    bar: {
        1: 'bg-gradient-primary',
        2: 'bg-gradient-success',
        3: 'bg-gradient-danger'
    }
})

const token = computed(() => {
    return store.getters.getToken;
});
const book = computed(() => {
    return store.getters["book/getBook"];
});
const getBook = async (product_code) => {
    await store.dispatch('book/getBook', {product_code});
}
onBeforeMount(async () => {
    await getBook(productCode.value);
    store.commit('setLoading', false);
});
</script>
