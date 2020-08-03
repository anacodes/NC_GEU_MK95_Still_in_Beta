import axios from 'axios'

export default {

    auth_request(state) {
        state.auth.status = 'loading'
    },

    auth_success(state, {token, rtoken, name, email, registered, is_recruiter}) {
        state.auth.status = 'success'
        state.auth.token = token
        state.auth.refresh_token = rtoken
        state.auth.name = name
        state.auth.email = email
        state.registered = registered
        state.is_recruiter = is_recruiter
        //local store
        localStorage.setItem('token', token)
        localStorage.setItem('rtoken', rtoken)
        localStorage.setItem('registered', registered)
        localStorage.setItem('is_recruiter', is_recruiter)
        localStorage.setItem('name', name)
        localStorage.setItem('email', email)
        axios.defaults.headers.common['Authorization'] = `Bearer ${token}`
    },

    auth_error(state) {
        state.status = 'error'
    },

    logout(state) {
        state.auth.status = ''
        state.auth.token = ''
        state.auth.refresh_token = ''
        
        // local store
        localStorage.removeItem('token')
        localStorage.removeItem('name')
        localStorage.removeItem('email')
        localStorage.removeItem('rtoken')
        localStorage.removeItem('registered')
        localStorage.removeItem('is_recruiter')
        delete axios.defaults.headers.common['Authorization']

    },

    register(state) {
        state.registered = true
        localStorage.setItem('registered', true)
    }
};
