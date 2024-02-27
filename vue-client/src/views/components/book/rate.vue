<template>
    <div class="container">
        <!-- Login Modal -->
        <div class="modal fade login-modal" id="bookRateModal" tabindex="-1" role="dialog" aria-labelledby="loginModalLabel" aria-hidden="true">
            <div class="modal-dialog modal-sm" role="document">
                <div class="modal-content">
                    <div class="modal-header" id="loginModalLabel">
                        <h4 class="modal-title">Kitabı Değerlendir</h4>
                        <button type="button" data-dismiss="modal" data-bs-dismiss="modal" aria-label="Close" class="btn-close"></button>
                    </div>
                    <div class="modal-body">
                        <div class="col-12 m-0 p-0 d-flex align-items-center justify-content-between mb-5">
                            <div class="fq-rating">
                                <svg
                                    v-for="i in myRate"
                                    :key="i" xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor"
                                    stroke-width="2" stroke-linecap="round" stroke-linejoin="round" class="feather feather-star checked" @mouseover="changeRate(i)"
                                >
                                    <polygon points="12 2 15.09 8.26 22 9.27 17 14.14 18.18 21.02 12 17.77 5.82 21.02 7 14.14 2 9.27 8.91 8.26 12 2"></polygon>
                                </svg>
                                <svg
                                    v-for="i in (10 - myRate)"
                                    :key="i" xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor"
                                    stroke-width="2" stroke-linecap="round" stroke-linejoin="round" class="feather feather-star" @mouseover="changeRate(myRate + i)"
                                >
                                    <polygon points="12 2 15.09 8.26 22 9.27 17 14.14 18.18 21.02 12 17.77 5.82 21.02 7 14.14 2 9.27 8.91 8.26 12 2"></polygon>
                                </svg>
                            </div>
                            <div>
                                <span class="btn btn-outline-info rounded-pill pill-rate">
                                    {{ myRate }}
                                </span>
                            </div>
                        </div>
                        
                        <button type="button" class="btn btn-primary float-end" @click="createRate">Gönder</button>
                    </div>
                </div>
            </div>
        </div>
    </div>
</template>

<style lang="scss" scoped>
.feather-star {
    cursor: pointer;

    &.checked {
        fill: white;
    }
}
.pill-rate{
    width: 37px;
    min-width: 37px;
    max-width: 37px;
}
</style>

<script setup>
import "/src/assets/sass/scrollspyNav.scss";
import {ref, watch} from "vue";
import {toast} from "vue3-toastify";
import {useStore} from "vuex";

const store = useStore();
const props = defineProps({
    rate: Number,
    product_code: String
});
const emit = defineEmits(['update:rate']);
const myRate = ref(props.rate);

watch(myRate, (newRate) => {
    emit('update:rate', newRate);
});
const changeRate = async (rate) => {
    myRate.value = rate;
    emit('update:rate', rate);
}
const createRate = async () => {
    try {
        await store.dispatch('bookRate/create', {rate: myRate.value, book_id: props.product_code});
        toast.success('Kayıt Başarılı');
        window.location.reload();
    }catch (err){
        toast.error(err.message);
    }
}
</script>
