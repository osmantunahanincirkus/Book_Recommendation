<template>
    <div class="loader-div">
        <div>
            <img src="../../assets/images/logo.png" alt="kitaponeri.com">
            <div class="loader multi-loader mx-auto"></div>
        </div>
    </div>
</template>

<style lang="scss" scoped>
.loader-div {
    position: fixed;
    top: 0;
    right: 0;
    bottom: 0;
    left: 0;
    z-index: 3;
    display: flex;
    align-items: center;
    justify-content: center;

    & > div {
        & > img {
            max-width: 331px;
            max-height: 114px;
            margin-bottom: 15px;
        }
    }
}
</style>

<script setup>
import "/src/assets/sass/scrollspyNav.scss";
</script>
