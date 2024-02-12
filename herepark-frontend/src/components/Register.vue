<script setup lang="ts">
import { ref } from 'vue'
import { useRouter } from 'vue-router'

import { registerUser } from '../utils/auth'
import { UserRegister } from '../schemas/auth'

const router = useRouter()
const emit = defineEmits(['authorize'])

const username = ref('')
const password = ref('')
const confirmPassword = ref('')
const firstName = ref('')
const lastName = ref('')

async function register() {
    if (!username.value || !password.value || !confirmPassword.value || !firstName.value || !lastName.value) {
        return
    }
    if (password.value != confirmPassword.value) {
        throw new Error('Passwords must match!')
    }
    const userData: UserRegister = {
        username: username.value,
        password: password.value,
        first_name: firstName.value,
        last_name: lastName.value
    }
    let token = await registerUser(userData)
    localStorage.setItem('jwtToken', token)
    emit('authorize')
    router.push('/')
}
</script>
<template>
<div class="card mx-auto w-50">
  <div class="card-body">
    <form>
        <div class="mb-3">
            <label for="inputUsername" class="form-label">Username</label>
            <input type="text" class="form-control" id="inputUsername" v-model="username" required>
        </div>
        <div class="mb-3">
            <div class="row">
                <div class="col">
                    <label for="inputPassword" class="form-label">Password</label>
                    <input type="password" class="form-control" id="inputPassword" v-model="password" required>
                </div>
                <div class="col">
                    <label for="inputConfirmPassword" class="form-label"> Confirm Password</label>
                    <input type="password" class="form-control" id="inputConfirmPassword" v-model="confirmPassword" required>
                </div>
            </div>
        </div>
        <div class="mb-3">
            <div class="row">
                <div class="col">
                    <label for="inputFirstName" class="form-label">First Name</label>
                    <input type="text" class="form-control" id="inputFirstName" v-model="firstName" required>
                </div>
                <div class="col">
                    <label for="inputLastName" class="form-label">Last Name</label>
                    <input type="text" class="form-control" id="inputLastName" v-model="lastName" required>
                </div>
            </div>
        </div>
        <button type="submit" class="btn btn-secondary" @click="register">Register</button>
    </form>
  </div>
</div>
</template>
