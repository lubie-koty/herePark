<script setup lang="ts">
import { onMounted, ref } from 'vue'
import { Toast } from 'bootstrap'

const errorMessage = ref('')
const toastBootstrap = ref(Toast)

onMounted(() => {
    toastBootstrap.value = new Toast(
        document.getElementById('liveToast')
    )
})

function showErrorMessage(message: string) {
    errorMessage.value = message
    toastBootstrap.value.show()
}

defineExpose({showErrorMessage})
</script>
<template>
<div class="toast-container position-fixed bottom-0 end-0 p-3">
  <div id="liveToast" class="toast" role="alert" aria-live="assertive" aria-atomic="true">
    <div class="toast-header text-bg-danger">
      <strong class="me-auto">Error</strong>
      <button type="button" class="btn-close" data-bs-dismiss="toast" aria-label="Close"></button>
    </div>
    <div class="toast-body">
      {{ errorMessage }}
    </div>
  </div>
</div>
</template>
