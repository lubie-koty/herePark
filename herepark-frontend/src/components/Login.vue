<script setup lang="ts">
import { ref } from 'vue'
import { useRouter } from 'vue-router';

import { loginUser } from '../utils/auth'
import { UserLogin } from '../schemas/auth'

const emit = defineEmits(['authorize'])
const router = useRouter()
const username = ref('')
const password = ref('')

async function login() {
    if (!username.value || !password.value) {
        return
    }
    const user_data: UserLogin = {
        'username': username.value,
        'password': password.value
    }
    let token = await loginUser(user_data)
    localStorage.setItem('jwtToken', token)
    emit('authorize')
    router.push('/')
}
</script>
<template>
<div class="card mx-auto w-25">
  <div class="card-body">
    <form @submit.prevent="login">
        <div class="mb-3">
            <label for="inputUsername" class="form-label">Username</label>
            <input type="text" class="form-control" id="inputUsername" aria-describedby="usernameHelp" v-model="username" required>
        </div>
        <div class="mb-3">
            <label for="inputPassword" class="form-label">Password</label>
            <input type="password" class="form-control" id="inputPassword" v-model="password" required>
        </div>
        <button type="submit" class="btn btn-secondary">Login</button>
    </form>
  </div>
</div>
</template>
