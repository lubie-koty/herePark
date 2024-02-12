import { createApp } from 'vue'
import { createRouter, createWebHashHistory } from 'vue-router'

import App from './App.vue'

import { checkAuthentication } from './utils/auth'
import { routes } from './routes'

import './style.scss'
import 'bootstrap'


const router = createRouter({
    history: createWebHashHistory(),
    routes
})
router.beforeEach((to, from, next) => {
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
app.mount('#app')
