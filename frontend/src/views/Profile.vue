<template>
  <div class="home">
    <div v-if="!isAuthenticated" class="login-register">
      <router-link to="/">Home</router-link>
      <router-link to="/register/" class="register">Register</router-link>
      <router-link to="/login/">Login</router-link>
    </div>
    <div v-else class="login-register">
      <router-link to="/">Home</router-link>
      <router-link to="/profile/" class="register">Username - {{ username }}</router-link>
      <router-link to="/log-out/">Log out</router-link>
    </div>
    <h1 class="header">Your Games</h1>
    <div class="games">
      <table class="table-games">
        <tr>
          <th>Name</th>
          <th>Author</th>
          <th>Board size</th>
          <th>Max movements</th>
          <th>Is Training</th>
          <th>Is Trained</th>
          <th>Train</th>
          <th>Play</th>
        </tr>
        <ProfileGame v-for="game in games" v-bind:props_style="game" :key="game.id"/>
      </table>
    </div>
    <div v-if="!isGamesLoaded">
      <h3>Loading please wait...</h3>
    </div>
  </div>
</template>

<script>
import ProfileGame from '../components/ProfileGame.vue'

export default {
  name: 'Profile',
  components: {
    ProfileGame
  },
  data() {
    return {
      games: this.getMeGames(),
      isGamesLoaded: false,
      username: this.$store.getters.getUsername,
      isAuthenticated: this.$store.getters.isAuthenticated
    }
  },
  methods: {
    async getMeGames() {
      await this.$store.dispatch('getMeGames')
      this.games = this.$store.getters.getGames
      this.isGamesLoaded = true
    }
  },
  created() {
    // Change title of page
    document.title = 'Profile'
  }
}
</script>

<style>
.home {
  height: 100vh;
  display: flex;
  align-items: center;
  flex-direction: column;
}

.login-register {
  width: 80%;
  font-size: 1.75vmin;
  margin-top: 0.5%;
  display: flex;
  justify-content: flex-end;
}

.register {
  margin-left: auto;
  margin-right: 2%;
}

.header {
  margin-bottom: 2%;
  font-size: 3.5vmin;
}

.games {
  width: 80%;
  overflow-x: auto;
  margin-bottom: 2%;
}

.table-games {
  width: 100%;
  font-size: 1.75vmin;
  text-align: center;
  border-collapse: separate;
  border-spacing: 0 0.5em;
}

.table-games tr:nth-child(even) {
  background-color: #779556;
  color: black;
}

.table-games tr:nth-child(2n+3) {
  background-color: #ebecd0;
  color: black;
}

.table-games tr:nth-child(even):hover {
  color: #ebecd0;
}

.table-games tr:nth-child(2n+3):hover {
  color: #779556;
}
</style>
