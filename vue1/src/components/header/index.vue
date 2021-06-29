<template lang="html">
  <el-menu class="df-header" default-active="1" mode="horizontal" :router="true">
    <el-row justify="space-around" type="flex">
      <el-col :span="30">
        <el-menu-item index="1" :route="{ name:'home' }">Home</el-menu-item>
        <el-menu-item index="2" :route="{ name:'poem' }">Browse</el-menu-item>
        <el-menu-item index="3" :route="{ name:'ContactUs' }">Contact Us</el-menu-item>
        <el-menu-item index="4" :route="{ name:'Help'}">Help</el-menu-item>
        <el-menu-item index="5" :route="{ name:'AboutUs' }">About Us</el-menu-item>
        <el-menu-item index="6" :route="{ name:'apprec' }">News</el-menu-item>
        <el-menu-item index="7" :route="{ name:'feedback' }">Download</el-menu-item>
      </el-col>
    </el-row>
    <div class="header_font">
    &nbsp;&nbsp;XXXXXXXXX
    </div>
  </el-menu>
</template>

<style lang="stylus">
@import '../../common/stylus/common.styl'
.df-header
  font-weight bold
  background-color #e3e3e3 !important
  height 10em
  .el-menu-item
    font-size 1.7em
    transition all .3s ease
    &:hover
      border-bottom 3px solid #141e9e
      bc(rgba(227, 227, 227, 0.68) !important, #141e9e)
      transform translateY(-10px)
    &.is-active
      border-bottom-left-radius 80%
      border-bottom-right-radius 10%
      border-bottom 3px solid #141e9e
      color #141e9e
</style>
