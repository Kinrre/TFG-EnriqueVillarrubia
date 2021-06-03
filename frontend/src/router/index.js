import Vue from 'vue'
import VueRouter from 'vue-router'
import CreateRoom from '../views/CreateRoom.vue'
import Home from '../views/Home.vue'
import JoinRoom from '../views/JoinRoom.vue'
import Room from '../views/Room.vue'

Vue.use(VueRouter)

const routes = [
  {
    path: '/',
    name: 'Home',
    component: Home
  },
  {
    path: '/create-room/',
    name: 'CreateRoom',
    component: CreateRoom
  },
  {
    path: '/room/:roomCode',
    name: 'Room',
    component: Room
  },
  {
    path: '/join-room/:roomCode',
    name: 'JoinRoom',
    component: JoinRoom
  }
]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})

export default router
