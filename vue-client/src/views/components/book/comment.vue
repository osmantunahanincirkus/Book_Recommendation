<template>
    <div class="container">
        <!-- Login Modal -->
        <div class="modal fade login-modal" id="bookCommentModal" tabindex="-1" role="dialog" aria-labelledby="loginModalLabel" aria-hidden="true">
            <div class="modal-dialog modal-sm" role="document">
                <div class="modal-content">
                    <div class="modal-header" id="loginModalLabel">
                        <h4 class="modal-title">Kitaba Yorum Yap</h4>
                        <button type="button" data-dismiss="modal" data-bs-dismiss="modal" aria-label="Close" class="btn-close"></button>
                    </div>
                    <div class="modal-body">
                        <div class="mb-3">
                            <label for="comment-textarea" class="col-form-label">Yorum yaz</label>
                            <div>
                                <textarea v-model="myComment" id="comment-textarea" class="form-control" rows="5"></textarea>
                            </div>
                        </div>

                        <button type="button" class="btn btn-primary float-end" @click="createComment">Gönder</button>
                    </div>
                </div>
            </div>
        </div>
    </div>
</template>

<script setup>
import "/src/assets/sass/scrollspyNav.scss";
import {ref} from "vue";
import {toast} from "vue3-toastify";
import {useStore} from "vuex";

const store = useStore();
const props = defineProps({
    product_code: String
});
const myComment = ref(null);
const createComment = async () => {
    try {
        await store.dispatch('bookComment/create', {comment: myComment.value, book_id: props.product_code});
        toast.success('Kayıt Başarılı');
        window.location.reload();
    } catch (err) {
        toast.error(err.message);
    }
}
</script>
