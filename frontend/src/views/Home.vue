<template>
  <div id="home">
    <h1 id="header">List of Games</h1>
    <div id="games">
      <table id="table-games">
        <tr>
          <th>Name</th>
          <th>Author</th>
          <th>Board size</th>
          <th>Max movements</th>
          <th>Training</th>
          <th>Play</th>
        </tr>
        <Game v-for="game in games" v-bind:props_style="game" :key="game.id"/>
      </table>
    </div>
    <div v-if="!isGamesLoaded">
      <h3>Loading please wait...</h3>
    </div>
  </div>
</template>

<script>
import Game from '../components/Game.vue'

export default {
  name: 'Home',
  components: {
    Game
  },
  data() {
    return {
      games: this.getGames(),
      isGamesLoaded: false
    }
  },
  methods: {
    async getGames() {
      await this.$store.dispatch('getGames')
      this.games = this.$store.getters.getGames
      this.isGamesLoaded = true
    }
  }
}
</script>

<style>
#home {
  height: 100vh;
  display: flex;
  align-items: center;
  flex-direction: column;
}

#header {
  margin-top: 2%;
  margin-bottom: 2%;
  font-size: 3.5vmin;
}

#games {
  width: 80%;
  overflow-x: auto;
  margin-bottom: 2%;
}

#table-games {
  width: 100%;
  font-size: 1.75vmin;
  text-align: center;
  border-collapse: separate;
  border-spacing: 0 0.5em;
}

#table-games tr:nth-child(even) {
  background-color: #779556;
  color: black;
}

#table-games tr:nth-child(2n+3) {
  background-color: #ebecd0;
  color: black;
}

#table-games tr:nth-child(even):hover {
  color: #ebecd0;
}

#table-games tr:nth-child(2n+3):hover {
  color: #779556;
}
</style>
