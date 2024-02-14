import { createApp } from 'vue'
import { createRouter, createWebHashHistory } from 'vue-router'

import VueGoogleMaps from 'vue-google-maps-community-fork'
import VueDatePicker from '@vuepic/vue-datepicker'
import '@vuepic/vue-datepicker/dist/main.css'
import 'bootstrap'

import App from './App.vue'

import { checkAuthentication } from './utils/auth'
import { routes } from './routes'

import './style.scss'

const vueGoogleMapsSettings = {
    load: {
        key: import.meta.env.VITE_MAPS_API_KEY
    }
}

const router = createRouter({
    history: createWebHashHistory(),
    routes
})
router.beforeEach((to, _, next) => {
    if (to.meta.requiresAuth) {
        if (checkAuthentication()) {
            next()
        } else {
            next('/login')
        }
    } else {
        next()
    }
})

const app = createApp(App)

app.use(router)
app.use(VueGoogleMaps, vueGoogleMapsSettings)
app.component('VueDatePicker', VueDatePicker)
app.mount('#app')
