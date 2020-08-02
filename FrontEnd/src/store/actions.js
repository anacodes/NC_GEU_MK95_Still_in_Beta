import axios from 'axios'

export default {
    LOGIN({ commit }, user) {
        return new Promise((resolve, reject) => {
            commit('auth_request')
            axios({ url: 'http://127.0.0.1:8000/auth/login/', data: user, method: 'POST' })
                .then(resp => {
                    const token = resp.data.refresh
                    const rtoken = resp.data.refresh
                    const name = resp.data.name
                    const email = resp.data.email
                    const registered = resp.data.registered
                    const is_recruiter = resp.data.is_recruiter
                    // console.log(typeof(registered), "kay yet aahe");
                    commit('auth_success', { token, rtoken, name, email, registered, is_recruiter })
                    resolve(resp)
                })
                .catch(err => {
                    commit('logout')

                    reject(err.response)
                })
        })
    },

    SIGNUP({ commit }, user) {
        commit('logout')
        return new Promise((resolve, reject) => {
            axios({ url: 'http://127.0.0.1:8000/auth/register/', data: user, method: 'POST' })
                .then(resp => {
                    resolve(resp)
                })
                .catch(err => {
                    commit('logout')
                    reject(err.response)
                })
        })
    },

    AUTHENTICATE({ commit }, token) {
        return new Promise((resolve, reject) => {
            axios({ url: 'http://127.0.0.1:8000/auth/emailverify/', data: token, method: 'POST' })
                .then(resp => {
                    resolve(resp)
                })
                .catch(err => {
                    commit('auth_error', err)
                    localStorage.removeItem('token')
                    localStorage.removeItem('rtoken')
                    localStorage.removeItem('registered')
                    localStorage.removeItem('is_recruiter')
                    reject(err.response)
                })
        })
    },

    RESENDMAIL({ commit }, token) {
        return new Promise((resolve, reject) => {
            axios({ url: 'http://127.0.0.1:8000/auth/resendemail/', data: token, method: 'POST' })
                .then(resp => {
                    resolve(resp)
                })
                .catch(err => {
                    commit('logout', err)

                    reject(err.response)
                })
        })
    },

    LOGOUT({ commit }, token) {
        return new Promise((resolve, reject) => {
            axios({ url: 'http://127.0.0.1:8000/auth/logout/', data: token, method: 'POST' })
                .then(resp => {
                    commit('logout')

                    resolve(resp)
                })
                .catch(err => {
                    commit('logout')

                    reject(err.response)
                })

        })
    },
};
