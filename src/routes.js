import {createWebHistory, createRouter} from 'vue-router'

import HomeView from './components/HomeView.vue'
import AboutView from './components/AboutView.vue'
import OrderView from './components/OrderView.vue'
import HelpView from './components/HelpView.vue'
import OrderNow from './components/OrderNow.vue'

const routes = [
    {
        name: 'HomeView',
        path: '/',
        component: HomeView
    },
    {
        name: 'AboutView',
        path: '/about',
        component: AboutView
    },
    {
        name: 'OrderView',
        path: '/order',
        component: OrderView
    },
    {
        name: 'HelpView',
        path: '/help',
        component: HelpView
    },
    {
        name: 'OrderNow',
        path: '/ordernow',
        component: OrderNow
    },
];


const router = createRouter({
    history: createWebHistory(),
    routes          
});

export default router;  