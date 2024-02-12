<script setup lang="ts">
import { onErrorCaptured, ref } from 'vue';
import ErrorMessage from './components/ErrorMessage.vue';
import Navbar from './components/Navbar.vue';

const errorMessage = ref(ErrorMessage)
const navBarRef = ref(Navbar)

function authorizeUser() {
  navBarRef.value.isAuthorized = true
}

onErrorCaptured((e: Error) => {
  errorMessage.value.showErrorMessage(e.message)
  return false
})
</script>

<template>
  <navbar
    ref="navBarRef"
  />
  <router-view
    @authorize="authorizeUser"
  />
  <error-message
    ref="errorMessage"
  />
</template>
