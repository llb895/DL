import Vue from 'vue'
import Router from 'vue-router'
import store from '../store'
import * as types from '../store/mutation-types'
// K562
import K562 from '@/pages/K562'

// POLR2A
import POLR2A from '@/pages/POLR2A'

// CTCF
import CTCF from '@/pages/CTCF'

// Browse
import Browse from '@/pages/Browse'

// News
import News from '@/pages/News'

// Download
import Download from '@/pages/Download'

// Contact Us
import ContactUs from '@/pages/ContactUs'

// Help
import Help from '@/pages/Help'

// 首页相关
import Home from '@/pages/home'

// 首页相关
import Home1 from '@/pages/home1'

// about us
import AboutUs from '@/pages/AboutUs'

Vue.use(Router)

const router = new Router({
  mode: 'history',
  base: '/',
  scrollBehavior(to, from, savedPosition) {
    if (savedPosition) {
      return savedPosition
    } else {
      return {x: 0, y: 0}
    }
  },
  routes: [
    {
      path: '/',
      name: 'home',
      component: Home
    }, {
      path: '/K562',
      name: 'K562',
      component: K562
    }, {
      path: '/POLR2A',
      name: 'POLR2A',
      component: POLR2A
    }, {
      path: '/CTCF',
      name: 'CTCF',
      component: CTCF
    }, {
      path: '/AboutUs',
      name: 'AboutUs',
      component: AboutUs
    }, {
      path: '/Help',
      name: 'Help',
      component: Help
    }, {
      path: '/ContactUs',
      name: 'ContactUs',
      component: ContactUs
    }, {
      path: '/Download',
      name: 'Download',
      component: Download
    }, {
      path: '/News',
      name: 'News',
      component: News
    }, {
      path: '/home1',
      name: 'home1',
      component: Home1
    }, {
      path: '/Browse',
      name: 'Browse',
      component: Browse,
      headers: {
        'Content-Type': 'application/json',
        'Accept': 'application/json'
      }
    }
  ]
})

// 导航钩子
router.beforeEach((to, from, next) => {
  // 检查登录状态
  store.commit(types.CHECKOUT_LOGIN_STATUS)
  if (to.matched.some(record => record.meta.requiresAuth)) { // 判断该路由是否需要登录权限
    if (window.localStorage.ACCESS_TOKEN) { // 如果本地存在 access_token，则继续导航
      next()
    } else {
      next({
        path: '/user/login',
        query: {
          redirect: to.fullPath
        }
      })
    }
  } else {
    next()
  }
})

export default router

