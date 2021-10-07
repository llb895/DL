<template lang="html">
  <el-menu class="df-header" default-active="1" mode="horizontal" :router="true">
    <el-row justify="space-around" type="flex">
      <el-col :span="30">
        <el-menu-item index="1" :route="{ name:'home1' }">Home</el-menu-item>
        <el-menu-item index="2" :route="{ name:'Browse' }">Browse</el-menu-item>
        <el-menu-item index="3" :route="{ name:'ContactUs' }">Contact Us</el-menu-item>
        <el-menu-item index="4" :route="{ name:'Help'}">Help</el-menu-item>
        <el-menu-item index="5" :route="{ name:'AboutUs' }">About Us</el-menu-item>
        <el-menu-item index="6" :route="{ name:'News' }">News</el-menu-item>
        <el-menu-item index="7" :route="{ name:'Download' }">Download</el-menu-item>
      </el-col>
    </el-row>
    <div class="header_font">
    &nbsp;XXXXXXXXX
    </div>
    <el-row justify="space-around" type="flex">
       <el-col :span="30">
          <div class="header_title">
             <el-menu-item index="8" :route="{ name:'weEncodeEH001841' }">weEncodeEH001841</el-menu-item>
             <el-menu-item index="9" :route="{ name:'CTCF' }">CTCF</el-menu-item>
             <el-menu-item index="10" :route="{ name:'POLR2A' }">POLR2A</el-menu-item>
             <el-menu-item index="11" :route="{ name:'K562' }">K562</el-menu-item>
          </div>
       </el-col>
    </el-row>
  </el-menu>


</template>




<style scope lang="stylus">
@import '../../common/stylus/common.styl'
.df-header
  font-weight bold
  background-color #2f3357 !important
  height 10em
  .el-menu-item
    font-size 1.7em
    transition all .3s ease
    color #ffffff
    &:hover
      color #000000
      border-bottom 3px solid #d26101
      bc(rgba(22, 100, 201, 0.01) !important, #c9510f)
      transform translateY(-10px)
    &.is-active
      border-bottom-left-radius 80%
      border-bottom-right-radius 10%
      border-bottom 3px solid #d26101
      color #ffffff
</style>
