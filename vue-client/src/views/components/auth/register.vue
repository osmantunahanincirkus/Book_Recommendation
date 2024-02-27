<template>
    <div class="container">
        <!--        &lt;!&ndash; Button trigger modal &ndash;&gt;-->
        <!--        <button type="button" class="btn btn-secondary mb-2 me-2" data-bs-toggle="modal" data-bs-target="#registerModal">Register</button>-->
        <!-- Register Modal -->
        <div class="modal fade register-modal" id="registerModal" tabindex="-1" role="dialog" aria-labelledby="registerModalLabel" aria-hidden="true">
            <div class="modal-dialog modal-sm" role="document">
                <div class="modal-content">
                    <div class="modal-header" id="registerModalLabel">
                        <h4 class="modal-title">Kayıt Ol</h4>
                        <button type="button" data-dismiss="modal" data-bs-dismiss="modal" aria-label="Close" class="btn-close"></button>
                    </div>
                    <div class="modal-body">
                        <form class="mt-0">
                            <div class="form-group">
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
                                    class="feather feather-at-sign"
                                >
                                    <circle cx="12" cy="12" r="4"></circle>
                                    <path d="M16 8v5a3 3 0 0 0 6 0v-1a10 10 0 1 0-3.92 7.94"></path>
                                </svg>
                                <input v-model="registerPayload.email" type="email" class="form-control mb-2" placeholder="E-posta"/>
                            </div>
                            <div class="form-group">
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
                                    class="feather feather-lock"
                                >
                                    <rect x="3" y="11" width="18" height="11" rx="2" ry="2"></rect>
                                    <path d="M7 11V7a5 5 0 0 1 10 0v4"></path>
                                </svg>
                                <input v-model="registerPayload.password" type="password" class="form-control mb-4" placeholder="Şifre"/>
                            </div>
                            <div class="form-group">
                                <input v-model="registerPayload.user_profile.name" type="text" class="form-control mb-4" placeholder="Ad"/>
                            </div>
                            <div class="form-group">
                                <input v-model="registerPayload.user_profile.surname" type="text" class="form-control mb-4" placeholder="Soyad"/>
                            </div>
                            <div class="form-group">
                                <button @click="register" type="button" class="btn btn-primary w-100" data-dismiss="modal" data-bs-dismiss="modal">Kayıt Ol</button>
                            </div>
                        </form>
                    </div>
                    <div class="modal-footer justify-content-center">
                        <div class="forgot login-footer">
                            <span>Zaten bir hesabım var. <a href="javascript:void(0);" type="button" data-bs-toggle="modal" data-bs-target="#loginModal">Giriş yap</a></span>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </div>
</template>

<script setup>
import "/src/assets/sass/scrollspyNav.scss";
import {ref} from "vue";
import {useStore} from "vuex";
import {toast} from "vue3-toastify";

const store = useStore();
const registerPayload = ref({
    email: null,
    password: null,
    user_profile: {
        name: null,
        surname: null
    }
});

const register = async () => {
    try {
        await store.dispatch('auth/register', registerPayload.value);
        toast.success('Üyelik oluşturma başarılı.');
    } catch (err) {
        toast.error(err.message);
    }
}
</script>
