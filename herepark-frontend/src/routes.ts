import Home from "./components/Home.vue"
import Login from "./components/Login.vue"
import Parking from "./components/Parking.vue"
import Register from "./components/Register.vue"

export const routes = [
    { path: '/', component: Home, meta: { requiresAuth: true } },
    { path: '/parking', component: Parking, meta: { requiresAuth: true }},
    { path: '/login', component: Login },
    { path: '/register', component: Register },
]
