<script src="//unpkg.com/vue/dist/vue.js"></script>
<script src="//unpkg.com/element-ui@2.15.6/lib/index.js"></script>
<template lang="html">
  <section class="df-feedback">
    <div class="main-wrapper">
      <div class="main">
        <div class="helpBackground">
          <div class="declaration">

            <div id="app">
            <template>
              <div style="display: flex;">
                <div style="display: flex;">
                  <p style="font-size: large; margin: 0;">show</p>
                  <el-select v-model="value" placeholder="10" size="small" style="width: 70px; padding-right: 2px; padding-left: 2px;">
                     <el-option
                       v-for="item in options"
                       :key="item.value"
                       :label="item.label"
                       :value="item.value">
                     </el-option>
                   </el-select>
                   <p style="font-size: large; margin: 0;">entries</p>
                </div>
                <div style="display: flex;">
                  <p style="font-size: large; margin: 0; padding-right: 5px;margin-left: 500px;">Search:</p>
                  <el-input v-model="search" placeholder="" size="small" style="width: 400px;"></el-input>
                </div>
              </div>
              <br />
              <el-table
                :data="tableData.filter(data => !search || data.Cell_Line.toLowerCase().includes(search.toLowerCase()))"
                height="250"
                border
                style="width: 100%"
                :default-sort = "{prop: 'Cell_Line', order: 'descending'}">
                <el-table-column
                  prop="Factor"
                  label="Factor"
                  sortable
                  width="200">
                </el-table-column>
                <el-table-column
                  prop="Cell_Line"
                  label="Cell-Line"
                  sortable
                  width="450">
                </el-table-column>
                <el-table-column
                  prop="UCSC"
                  label="UCSC"
                  sortable>
                </el-table-column>
              </el-table>
            </template>
            </div>
            <div>
              <el-pagination
                background
                layout="prev, pager, next"
                :total="100">
              </el-pagination>
            </div>


          </div>
        </div>
      </div>
    </div>
  </section>
</template>

<style lang="stylus" scoped>
@import '../../common/stylus/common'

td{
    text-align:center;
  }

.df-feedback
  margin-top 10px

  .main-wrapper
    fj(center)

    .main
      width 80%

      .declaration
        padding 40px
        border 1px solid black
        border-radius 10px
        box-shadow 0 1px 1px rgba(0, 0, 0, .2)
        line-height 1.5em
        color black
</style>


<script>
  export default {
    data () {
      return {
        tableData: [],
        options: [{
          value: '10',
          label: '10'
        }, {
          value: '25',
          label: '25'
        }, {
          value: '50',
          label: '50'
        }, {
          value: '100',
          label: '100'
        }],
        value: '',
        search: ''
      }
    }
  }
</script>
