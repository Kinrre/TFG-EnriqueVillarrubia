import '@babel/polyfill'
import 'mutationobserver-shim'
import Vue from 'vue'
import './plugins/bootstrap-vue'
//import VueSocketIO from 'vue-socket.io'
import App from './App.vue'
import router from './router'

Vue.config.productionTip = false

//Vue.use(new VueSocketIO({
//  debug: true,
//  connection: 'ws://localhost:8000/'
//}))

new Vue({
  router,
  render: h => h(App)
}).$mount('#app')
