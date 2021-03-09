<template>
  <div></div>
</template>

<script>
export default {
  name: 'Game',
  sockets: {
    connect() {
      console.log('socket connected')
    },
    hello(data) {
      console.log(data)
      this.$socket.emit('ack', "Yes :D")
    }
  }
}
</script>

<style>
</style>
