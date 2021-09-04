<template lang="html">
  <section class="df-feedback">
    <div class="main-wrapper">
      <div class="main">
        <div class="helpBackground">
          <div class="declaration">

            <template>
  <div class="home">
    <el-row>
        <el-table :data="informationList.slice((currentPage-1)*pagesize,currentPage*pagesize)" style="width: 100%" border
                  stripe
                  :default-sort = "{prop: 'date', order: 'descending'}">
          <el-table-column prop="id" label="ID" min-width="100">
            <template slot-scope="scope"> {{ scope.row.pk }} </template>
          </el-table-column>
          <el-table-column prop="factor" label="Factor" min-width="100">
            <template slot-scope="scope"> {{ scope.row.fields.factor }} </template>
          </el-table-column>
          <el-table-column prop="cell_line" label="Cell-line" min-width="100">
            <template slot-scope="scope"> {{ scope.row.fields.cell_line }} </template>
          </el-table-column>
          <el-table-column prop="ucsc" label="UCSC" min-width="100">
            <template slot-scope="scope"> {{ scope.row.fields.ucsc }} </template>
          </el-table-column>
          <el-table-column prop="lab" label="lab" min-width="100">
            <template slot-scope="scope"> {{ scope.row.fields.lab }} </template>
          </el-table-column>
        </el-table>
      <el-pagination class="fy"
                     layout="prev, pager, next"
                     @current-change="current_change"
                     :total="total"
                     background
                    >
                  </el-pagination>
    </el-row>
  </div>
</template>


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
  name: 'information',
  data () {
    return {
      input: '',
      total: 637, // 默认数据总数
      pagesize: 10, // 每页的数据条数
      currentPage: 1, // 默认开始页面
      istag: true,
      value5: [],
      informationList: []
    }
  },
  mounted: function () {
    this.showInformation()
  },
  methods: {
    showInformation () {
      this.$http.get('api/show_information')
        .then((response) => {
          var res = JSON.parse(response.bodyText)
          console.log(res)
          if (res.error_num === 0) {
            this.informationList = res['list']
          } else {
            this.$message.error('失败')
            console.log(res['msg'])
          }
        })
    },
    tableRowClassName({row, rowIndex}) {
      if (rowIndex === 0) {
        return 'th'
      }
      return ''
    },
    switchChange() {
      this.istag = !this.istag
    },

    current_change: function(currentPage) {
      this.currentPage = currentPage
    }
  }
}
</script>
