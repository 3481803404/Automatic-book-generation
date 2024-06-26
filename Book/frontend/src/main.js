import './assets/main.css'

import { createApp } from 'vue'
import App from './App.vue'
import ElementPlus from 'element-plus'

const app = createApp(App)
app.use(ElementPlus, { size: 'small', zIndex: 3000 })
app.mount('#app')
