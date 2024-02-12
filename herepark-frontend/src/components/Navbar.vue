<script setup lang="ts">
import { ref } from 'vue'
import { useRouter } from 'vue-router'

const isAuthorized = ref(false)
const router = useRouter()

function logout () {
    isAuthorized.value = false
    localStorage.removeItem('jwtToken')
    router.push('/login')
}

defineExpose({isAuthorized})
</script>
<template>
<nav class="navbar navbar-expand-lg bg-body-tertiary mb-2" data-bs-theme="dark">
    <div class="container-fluid">
        <router-link class="navbar-brand" to="#">herePark</router-link>
        <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarNavAltMarkup" aria-controls="navbarNavAltMarkup" aria-expanded="false" aria-label="Toggle navigation">
        <span class="navbar-toggler-icon"></span>
        </button>
        <div class="collapse navbar-collapse" id="navbarNavAltMarkup" v-if="isAuthorized">
            <div class="navbar-nav">
                <router-link class="nav-link active" aria-current="page" to="/">Home</router-link>
                <router-link class="nav-link" to="/parking">Parking</router-link>
            </div>
        </div>
        <div class="me-auto">
            <button type="button" class="btn btn-secondary" @click="logout" v-if="isAuthorized">Logout</button>
            <div v-else>
                <router-link class="btn btn-secondary me-1" to="/login">Login</router-link>
                <router-link class="btn btn-secondary" to="/register">Register</router-link>
            </div>
        </div>
    </div>
</nav>
</template>
