<template lang="html">
  <footer class="df-footer">
    <span>Copyright 2020 &copy <a href="https://u.osu.edu/bmbl">BMBL</a></span>
 		<div class="beian">
        <span class="footer_font1">Contact us: xxx.xxx</span>
      <br>
      <span class="footer_font1">The recommended browsers are Google Chrome and Firefox.</span>
 		</div>
  </footer>

</template>



<style lang="stylus" scoped>
@import '../../common/stylus/common'

.df-footer
  position absolute
  bottom 0
  width 100%
  padding 20px 0
  border-top 1px solid Light-Grey
  font(.7em,Light-Silver)
  text-align center
  .beian
    margin-top 10px
    a
      text-decoration none
      color Light-Silver
  .admin-login
    position absolute
    bottom 0
    right 0
    wh(40px,40px)
    outline none
    border 0
    background-color inherit
</style>
