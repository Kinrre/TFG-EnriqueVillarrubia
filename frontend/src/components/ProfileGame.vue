<template>
    <tr>
      <td>{{ name }}</td>
      <td>{{ author }}</td>
      <td>{{ boardSize }}</td>
      <td>{{ maxMovements }}</td>
      <td>{{ is_training }}</td>
      <td>{{ is_trained }}</td>
      <td><button type="button" :disabled=training_available>Train</button></td>
      <td><button type="button">Play</button></td>
    </tr>
</template>

<script>
export default {
  name: 'ProfileGame',
  props: {
    props_style: {
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
      training_available: this.props_style.is_trained
    }
  }
}
</script>

<style>
</style>
