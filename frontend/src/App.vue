<template>
  <div id="app" :style="div_size">
    <Board :boardSize="8" :fen="'rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR'"/>
  </div>
</template>

<script>
import Board from './components/Board.vue'

export default {
  name: 'App',
  components: {
    Board
  },
  data() {
    return {
      div_size: {
        height: 'auto',
        width: '100%'
      }
    }
  },
  methods: {
    onResize() {
      this.div_size.height = innerHeight + 'px'
      this.div_size.width = innerWidth + 'px'
    }
  },
  mounted() {
    window.addEventListener('resize', this.onResize)

    // Resize first time
    this.onResize()
  },
  beforeDestroy() {
    window.removeEventListener('resize', this.onResize)
  }
}
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  color: white;
  background-color: rgb(49, 46, 43);
}
</style>
