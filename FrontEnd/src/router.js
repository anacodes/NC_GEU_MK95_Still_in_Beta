import Vue from 'vue'
import Router from 'vue-router'
import store from '@/store'
import DashboardLayout from '@/layout/DashboardLayout'
import DashboardLayoutRecruiter from '@/layout/DashboardLayoutRecruiter'
import AuthLayout from '@/layout/AuthLayout'

Vue.use(Router)

const routes = [
  {
    path: '/emailverify/',
    name: 'SignupProcess',
    component: () => import('./views/SignupProcess.vue')
  },
  {
    path: '/resetpassword/',
    name: 'ResetPassword',
    component: () => import('./views/SubForms/ResetPassword.vue')
  },
  {
    path: '/jobseeker',
    component: DashboardLayout,
    children: [
      {
        path: '/',
        redirect: 'dashboard'
      },
      {
        path: 'dashboard',
        name: 'dashboard_jobseeker',
        component: () => import('./views/DashboardJobseeker.vue'),
        meta: {
          requiresAuth: true,
          requiresRegistration: true
        }
      },
      {
        path: 'profile',
        name: 'profile_jobseeker',
        component: () => import('./views/JobseekerProfile.vue'),
        meta: {
          requiresAuth: true,
          requiresRegistration: true
        }
      },
      {
        path: 'complete',
        name: 'complete_jobseeker',
        component: () => import('./views/CompleteJobseeker.vue'),
        meta: {
          requiresAuth: true
        }
      },
      {
        path: 'job',
        name: 'job_jobseeker',
        component: () => import('./views/Job.vue'),
        props: true,
        meta: {
          requiresAuth: true,
          requiresRegistration: true
        }
      },
      {
        path: 'joblistings',
        name: 'joblist_jobseeker',
        component: () => import('./views/JobListings.vue'),
        meta: {
          requiresAuth: true,
          requiresRegistration: true
        }
      }
    ],
    meta: {
      requiresAuth: true,
    }
  },
  {
    path: '/recruiter',
    component: DashboardLayoutRecruiter,
    children: [
      {
        path: '/',
        redirect: 'dashboard'
      },
      {
        path: 'dashboard',
        name: 'dashboard_recruiter',
        component: () => import('./views/DashboardRecruiter.vue'),
        meta: {
          requiresAuth: true,
          requiresRecruiter: true,
          requiresRegistration: true
        }
      },
      {
        path: 'profile',
        name: 'profile_recruiter',
        component: () => import('./views/RecruiterProfile.vue'),
        meta: {
          requiresAuth: true,
          requiresRecruiter: true,
          requiresRegistration: true
        }
      },
      {
        path: 'jobcreate',
        name: 'job_create',
        component: () => import('./views/JobCreate.vue'),
        meta: {
          requiresAuth: true,
          requiresRecruiter: true,
          requiresRegistration: true
        }
      },
      {
        path: 'complete',
        name: 'complete_recruiter',
        component: () => import('./views/CompleteRecruiter.vue'),
        meta: {
          requiresAuth: true,
          requiresRecruiter: true,
        }
      },
      {
        path: 'jobdetails',
        name: 'JobRecruiter',
        props: true,
        component: () => import('./views/JobRecruiter.vue'),
        meta: {
          requiresAuth: true,
          requiresRecruiter: true,
          requiresRegistration: true
        }
      },
      {
        path: 'alljobs',
        name: 'alljobs',
        component: () => import('./views/RecruiterAllJobs.vue'),
        meta: {
          requiresAuth: true,
          requiresRecruiter: true,
          requiresRegistration: true
        }
      }
    ],
    meta: {
      requiresAuth: true,
      requiresRecruiter: true
    }
  },
  {
    path: '/',
    redirect: 'home',

    component: AuthLayout,
    children: [
      {
        path: '/login',
        name: 'login',
        component: () => import('./views/Login.vue')
      },
      {
        path: '/register',
        name: 'register',
        component: () => import('./views/Register.vue')
      },
      {
        path: '/company/:name',
        name: 'company',
        component: () => import('./views/CompanyPage.vue')
      },
      {
        path: '/home',
        name: 'home',
        component: () => import('./views/Home.vue')
      },
      {
        path: '/joblistings',
        name: 'joblist_public',
        component: () => import('./views/JobListingsPublic.vue')
      },
      {
        path: '/forgotpassword',
        name: '/forgotpassword',
        component: () => import('./views/SubForms/ForgotPassword.vue')
      },

      {
        path: '/job',
        name: 'JobPublic',
        props: true,
        component: () => import('./views/JobPublic.vue')
      }
    ]
  }
]

const router = new Router({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})


router.beforeEach((to, from, next) => {

  if (to.matched.some(record => record.meta.requiresAuth)) {
    if (store.getters.isLoggedIn) {
      if (to.meta.requiresRecruiter) {
        // recruiter
        // logged in
        if (store.getters.isRecruiter) {
          if (to.meta.requiresRegistration) {
            if (store.getters.isRegistered) {
              next()
              return
            }
            next('/recruiter/complete')
            return
          }
          next()
          return
        }
        next('/home')
        return
      }
      else {
        // jobseeker
        // logged in
        if (store.getters.isRecruiter) {
          next('/recruiter')
          return
        }
        if (to.meta.requiresRegistration) {

          if (store.getters.isRegistered) {
            next()
            return
          }
          next('/jobseeker/complete')
          return
        }
        next()
        return
      }
    }
    next('/login')
    return
  }
  else {
    next()
  }
})

export default router
