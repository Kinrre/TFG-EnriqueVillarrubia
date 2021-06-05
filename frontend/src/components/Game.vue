<template>
    <tr>
      <td>{{ name }}</td>
      <td>{{ author }}</td>
      <td>{{ boardSize }}</td>
      <td>{{ maxMovements }}</td>
      <td>{{ is_trained }}</td>
      <td><button type="button" class="transparent">▶️</button></td>
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
      is_trained: Boolean
    }
  },
  data() {
    return {
      name: this.props_style.name,
      author: this.props_style.username,
      boardSize: this.props_style.board_size + 'x' + this.props_style.board_size,
      maxMovements: this.props_style.maximum_movements,
      is_trained: this.props_style.is_trained ? "✔️" : "❌"
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
