<template>
    <div class="container">
        <!-- Login Modal -->
        <div class="modal fade login-modal" id="loginModal" tabindex="-1" role="dialog" aria-labelledby="loginModalLabel" aria-hidden="true">
            <div class="modal-dialog modal-sm" role="document">
                <div class="modal-content">
                    <div class="modal-header" id="loginModalLabel">
                        <h4 class="modal-title">Giriş</h4>
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
                                    class="feather feather-user"
                                >
                                    <path d="M20 21v-2a4 4 0 0 0-4-4H8a4 4 0 0 0-4 4v2"></path>
                                    <circle cx="12" cy="7" r="4"></circle>
                                </svg>
                                <input v-model="email" type="email" class="form-control mb-2" placeholder="E-posta" />
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
                                <input v-model="password" type="password" class="form-control mb-4" placeholder="Şifre" />
                            </div>
                            <div class="form-group">
                                <button type="button" block @click="login" class="btn btn-primary w-100" data-dismiss="modal" data-bs-dismiss="modal">Giriş</button>
                            </div>
                        </form>
                    </div>
                    <div class="modal-footer justify-content-center">
                        <div class="forgot login-footer">
                            <span><a href="javascript:void(0);" type="button" data-bs-toggle="modal" data-bs-target="#registerModal">Yeni hesap oluştur</a></span>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </div>
</template>

<script setup>
import "/src/assets/sass/scrollspyNav.scss";
import {useStore} from "vuex";
import {ref} from "vue";
import {toast} from "vue3-toastify";

const store = useStore();
const email = ref(null);
const password = ref(null);

const login = async () => {
    try {
        await store.dispatch('auth/login', {email: email.value, password: password.value});
        toast.success('Giriş Başarılı');
        window.location.reload();
    }catch (err){
        toast.error(err.message);
    }
};
</script>
