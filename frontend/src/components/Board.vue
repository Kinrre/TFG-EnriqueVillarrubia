<template>
  <div :style="div_size">
    <ResponsiveImage name="boards/board_8x8.png"/>
  </div>
</template>

<script>
import ResponsiveImage from './ResponsiveImage.vue'

export default {
  name: 'Board',
  components: {
    ResponsiveImage
  },
  data() {
    return {
      div_size: {
        height: '100%',
        width: '100%'
      }
    }
  }
}
</script>

<style>

</style>
