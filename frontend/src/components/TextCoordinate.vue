<template>
  <text :x="x_value" :y="y_value" :style="text_style">{{ text_value }}</text>
</template>

<script>
export default {
  name: 'Coordinates',
  props: {
    props_style: {
      boardSize: Number,
      x: Number,
      y: Number,
      color: String,
      value: String
    }
  },
  data() {
    return {
      x_value: this.props_style.x + '%',
      y_value: this.props_style.y + '%',
      text_style: {
        fontSize: 22.232 / this.props_style.boardSize + 'vmin',
        fontWeight: 600,
        fill: this.props_style.color == 'light' ? '#779952' : '#edeed1',
        userSelect: 'none'
      },
      text_value: this.props_style.value
    }
  }
}
</script>

<style>
</style>
