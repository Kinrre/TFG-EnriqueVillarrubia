<template>
    <tr>
      <td>{{ name }}</td>
      <td>{{ author }}</td>
      <td>{{ boardSize }}</td>
      <td>{{ maxMovements }}</td>
      <td>{{ training }}</td>
      <button type="button">Play</button>
    </tr>
</template>

<script>
export default {
  name: 'Game',
  props: {
    props_style: {
      name: String,
      author: String,
      boardSize: Number,
      maxMovements: Number,
      training: Boolean
    }
  },
  data() {
    return {
      name: this.props_style.name,
      author: this.props_style.username,
      boardSize: this.props_style.board_size + 'x' + this.props_style.board_size,
      maxMovements: this.props_style.maximum_movements,
      training: this.props_style.is_training
    }
  }
}
</script>

<style>
</style>
