<template>
    <tr>
      <td>{{ name }}</td>
      <td>{{ author }}</td>
      <td>{{ boardSize }}</td>
      <td>{{ maxMovements }}</td>
      <td>{{ is_training }}</td>
      <td>{{ is_trained }}</td>
      <td><button v-on:click="trainGame" type="button" class="transparent" :disabled=!training_available>{{ training_emoji }}</button></td>
      <td><button type="button" class="transparent">▶️</button></td>
    </tr>
</template>

<script>
export default {
  name: 'ProfileGame',
  props: {
    props_style: {
      id: Number,
      name: String,
      author: String,
      boardSize: Number,
      maxMovements: Number,
      is_training: Boolean,
      is_trained: Boolean
    }
  },
  data() {
    return {
      name: this.props_style.name,
      author: this.props_style.username,
      boardSize: this.props_style.board_size + 'x' + this.props_style.board_size,
      maxMovements: this.props_style.maximum_movements,
      is_training: this.props_style.is_training ? "✔️" : "❌",
      is_trained: this.props_style.is_trained ? "✔️" : "❌",
      training_available: !this.props_style.is_training && !this.props_style.is_trained,
      training_emoji: this.getTrainingEmoji()
    }
  },
  methods: {
    getTrainingEmoji() {
      var emoji = "-"

      if (!this.props_style.is_training && !this.props_style.is_trained) {
        emoji = "🏋️"
      }
      
      return emoji
    },
    async trainGame() {
      await this.$store.dispatch('trainGame', this.props_style.id)

      if (this.$store.getters.isTrainingSuccessful) {
        this.is_training = "✔️"
        this.training_available = false
        this.training_emoji = '-'
      }
    }
  }
}
</script>

<style>
.transparent {
  background-color: transparent;
  background-repeat: no-repeat;
  border: none;
  overflow: hidden;
  outline: none;
}
</style>
