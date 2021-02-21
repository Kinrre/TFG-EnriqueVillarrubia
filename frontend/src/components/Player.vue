<template>
  <b-container fluid>
    <b-row align-v="center" :style="{height: row_height + 'px'}">
      <b-col :style="{height: row_height + 'px'}">
        <b-img src="../assets/avatar.png" class="player-img"></b-img>
      </b-col>
      <b-col :style="{height: row_height + 'px'}">
        <p>{{ player_name }}</p>
      </b-col>
    </b-row>
  </b-container>
</template>

<script>
export default {
  name: 'Player',
  data() {
    return {
      row_height: innerHeight * 0.05
    }
  },
  props: {
    player_name: String
  },
  methods: {
    onResize() {
      this.row_height = innerHeight * 0.05
    }
  },
  mounted() {
    // Register an event listener when the Vue component is ready
    window.addEventListener('resize', this.onResize)
  },
  beforeDestroy() {
    // Unregister the event listener before destroying this Vue instance
    window.removeEventListener('resize', this.onResize)
  }
}
</script>

<style>
.player-img {
  height: 100%;
}
</style>
