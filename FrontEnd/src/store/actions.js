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

    JSREGISTRATION({ commit }, fd) {
        return new Promise((resolve, reject) => {
            axios({
                url: 'http://127.0.0.1:8000/applicant/registration/', data: fd, method: 'POST',
                headers: {
                    'Content-Type': 'multipart/form-data'
                }
            })
                .then(resp => {
                    commit('register')
                    resolve(resp)
                })
                .catch(err => {
                    console.log('error in jobseeker complete profile');
                    reject(err.response)
                })
        })
    },

    RECREGISTRATION({ commit }, fd) {
        return new Promise((resolve, reject) => {
            axios({
                url: 'http://127.0.0.1:8000/recruiter/registration/', data: fd, method: 'POST',
                headers: {
                    'Content-Type': 'multipart/form-data'
                }
            })
                .then(resp => {
                    commit('register')
                    resolve(resp)
                })
                .catch(err => {
                    console.log('error in recruiter complete profile');
                    reject(err.response)
                })
        })
    },

    JSPROFILE({ commit }) {
        return new Promise((resolve, reject) => {
            axios({
                url: 'http://127.0.0.1:8000/applicant/registration/', method: 'GET',
                headers: {
                    'Content-Type': 'multipart/form-data'
                }
            })
                .then(resp => {
                    // commit('register')
                    resolve(resp.data[0])
                    // console.log("zala success", resp.data[0]);
                })
                .catch(err => {
                    console.log('error in get jobseeker profile : ', err.response);
                    reject(err.response)
                })
        })
    },

    JSPATCH({ commit }, fd) {
        return new Promise((resolve, reject) => {
            axios({
                url: 'http://127.0.0.1:8000/applicant/registrationupdate/', data: fd, method: 'PATCH',
                headers: {
                    'Content-Type': 'multipart/form-data'
                }
            })
                .then(resp => {
                    // commit('register')
                    resolve(resp)
                    // console.log("zala success", resp.data[0]);
                })
                .catch(err => {
                    console.log('error in get jobseeker patch');
                    reject(err.response)
                })
        })
    },

    RECPROFILE({ commit }) {
        return new Promise((resolve, reject) => {
            axios({
                url: 'http://127.0.0.1:8000/recruiter/registration/', method: 'GET',
                headers: {
                    'Content-Type': 'multipart/form-data'
                }
            })
                .then(resp => {
                    // commit('register')
                    resolve(resp.data[0])
                    // console.log("zala success", resp.data[0]);
                })
                .catch(err => {
                    console.log('error in get recruiter profile');
                    reject(err.response)
                })
        })
    },

    RECPATCH({ commit }, fd) {
        return new Promise((resolve, reject) => {
            axios({
                url: 'http://127.0.0.1:8000/recruiter/registrationupdate/', data: fd, method: 'PATCH',
                headers: {
                    'Content-Type': 'multipart/form-data'
                }
            })
                .then(resp => {
                    // commit('register')
                    resolve(resp)
                    // console.log("zala success", resp.data[0]);
                })
                .catch(err => {
                    console.log('error in get recruiter patch');
                    reject(err.response)
                })
        })
    },

    PUBLICJOBS({ commit }) {
        return new Promise((resolve, reject) => {
            axios({
                url: 'http://127.0.0.1:8000/recruiter/joblisting/', method: 'GET',
            })
                .then(resp => {
                    // commit('register')
                    resolve(resp.data)
                    // console.log("zala success", resp.data);
                })
                .catch(err => {
                    console.log('error in GET public jobs : ', err.response);
                    reject(err.response)
                })
        })
    },

    JSJOBS({ commit }) {
        return new Promise((resolve, reject) => {
            axios({
                url: 'http://127.0.0.1:8000/applicant/joblisting/', method: 'GET',
            })
                .then(resp => {
                    // commit('register')
                    resolve(resp.data)
                    // console.log("zala success", resp.data);
                })
                .catch(err => {
                    console.log('error in GET applicant jobs : ', err.response);
                    reject(err.response)
                })
        })
    },

    COMPANYPROFILE({ commit }, name) {
        return new Promise((resolve, reject) => {
            axios({
                url: `http://127.0.0.1:8000/recruiter/company/${name}`, method: 'GET',
            })
                .then(resp => {
                    // commit('register')
                    resolve(resp.data)
                    // console.log("zala success", resp.data);
                })
                .catch(err => {
                    console.log('error in comapny : ', err.response);
                    reject(err.response)
                })
        })
    },

    APPLYJOB({ commit }, jobid) {
        return new Promise((resolve, reject) => {
            axios({
                url: 'http://127.0.0.1:8000/applicant/applyjob/', data: jobid, method: 'POST',
            })
                .then(resp => {
                    resolve(resp.data)
                })
                .catch(err => {
                    console.log('error in job apply');
                    reject(err.response)
                })
        })
    },

    JSDASHBOARD({ commit }) {
        return new Promise((resolve, reject) => {
            axios({
                url: 'http://127.0.0.1:8000/applicant/dashboardapplied/', method: 'GET',
            })
                .then(resp => {
                    // commit('register')
                    resolve(resp.data) // should be list
                    // console.log("zala success", resp.data);
                })
                .catch(err => {
                    console.log('error in applied jobs : ', err.response);
                    reject(err.response)
                })
        })
    },

    JOBCREATE({ commit }, fd) {
        return new Promise((resolve, reject) => {
            axios({
                url: 'http://127.0.0.1:8000/recruiter/jobcreate/', data: fd, method: 'POST',
                headers: {
                    'Content-Type': 'multipart/form-data'
                }
            })
                .then(resp => {
                    resolve(resp.data)
                })
                .catch(err => {
                    console.log('error creating job');
                    reject(err.response)
                })
        })
    },

    // 5 for dashboard recruiter
    // get applicants for a job
    GETAPPLICANTS({ commit }, jobid) {
        return new Promise((resolve, reject) => {
            axios({
                url: `http://127.0.0.1:8000/recruiter/jobapplicant/${jobid}`, method: 'GET',
            })
                .then(resp => {
                    // commit('register')
                    resolve(resp.data)
                    // console.log("zala success", resp.data);
                })
                .catch(err => {
                    console.log('error getting applicants : ', err.response);
                    reject(err.response)
                })
        })
    },

    // sort into 3 tables
    RECDASHBOARD({ commit }) {
        return new Promise((resolve, reject) => {
            axios({
                url: 'http://127.0.0.1:8000/recruiter/jobcreate/', method: 'GET',
            })
                .then(resp => {
                    resolve(resp.data)
                })
                .catch(err => {
                    console.log('error showing dashboard recruiter');
                    reject(err.response)
                })
        })
    },
    // activate draft job
    DRAFTACTIVATE({ commit }, jobId) {
        var fd = new FormData();
        fd.append("activate", true);
        return new Promise((resolve, reject) => {
            axios({
                url: `http://127.0.0.1:8000/recruiter/jobcreate/${jobId}`, data: fd, method: 'PATCH',
            })
                .then(resp => {
                    resolve(resp.data)
                })
                .catch(err => {
                    console.log('error patching status');
                    reject(err.response)
                })
        })
    },
    // patch status
    STATUSUPDATE({ commit }, payload) {
        var snd = {};
        snd.status = payload.status;
        const jobAppliedId = payload.jobAppliedId;
        return new Promise((resolve, reject) => {
            axios({
                url: `http://127.0.0.1:8000/recruiter/jobapplicant/status/${jobAppliedId}`, data: snd, method: 'PATCH',
            })
                .then(resp => {
                    resolve(resp.data)
                })
                .catch(err => {
                    console.log('error patching status');
                    reject(err.response)
                })
        })
    },

    // delete draft job
    DRAFTDELETE({ commit }, jobid) {
        return new Promise((resolve, reject) => {
            axios({
                url: `http://127.0.0.1:8000/recruiter/jobcreate/${jobid}`, method: 'DELETE',
            })
                .then(resp => {
                    // commit('register')
                    resolve(resp.data)
                    // console.log("zala success", resp.data);
                })
                .catch(err => {
                    console.log('error deltiting job : ', err.response);
                    reject(err.response)
                })
        })
    },

    // extract JD
    EXTRACTJD({ commit }, fd) {
        return new Promise((resolve, reject) => {
            axios({
                url: 'http://127.0.0.1:8000/recruiter/jobcreate/jd/', data: fd, method: 'POST',
                headers: {
                    'Content-Type': 'multipart/form-data'
                }
            })
                .then(resp => {
                    resolve(resp.data)
                })
                .catch(err => {
                    console.log('error extracting jd');
                    reject(err.response)
                })
        })
    },

    // password reset work
    //1
    NEWPASSWORDREQUEST({ commit }, payload) {
        return new Promise((resolve, reject) => {
            axios({ url: 'http://127.0.0.1:8000/auth/requestresetemail/', data: payload, method: 'POST' })
                .then(resp => {
                    resolve(resp)
                })
                .catch(err => {
                    console.log("error reset pass request");
                    reject(err.response)
                })
        })
    },

    //2 get
    VALIDATEPASSWORDREQUEST({ commit }, payload) {
        return new Promise((resolve, reject) => {
            axios({ url: `http://127.0.0.1:8000/auth/passwordresetcheck/${payload.uidb}/${payload.token}`, method: 'GET' })
                .then(resp => {
                    resolve(resp.data)
                })
                .catch(err => {
                    console.log("error in VALIDATEPASSWORDREQUEST");
                    reject(err.response)
                })
        })
    },

    //3 post
    RESETPASSWORD({ commit }, payload) {
        return new Promise((resolve, reject) => {
            axios({ url: 'http://127.0.0.1:8000/auth/passwordreset/', data: payload, method: 'PATCH' })
                .then(resp => {
                    resolve(resp.data)
                })
                .catch(err => {
                    console.log("error in RESETPASSWORD");
                    reject(err.response)
                })
        })
    },

    // caleder 3 apis
    GAUTH({ commit }) {
        return new Promise((resolve, reject) => {
            axios({
                url: 'http://127.0.0.1:8000/recruiter/gauth', method: 'GET',
            })
                .then(resp => {
                    resolve(resp.data)
                })
                .catch(err => {
                    console.log('error in guath link');
                    reject(err.response)
                })
        })
    },

    GAUTHTOKEN({ commit }, payload) {
        return new Promise((resolve, reject) => {
            axios({ url: 'http://127.0.0.1:8000/recruiter/gauth/', data: payload, method: 'POST' })
                .then(resp => {
                    resolve(resp.data)
                })
                .catch(err => {
                    console.log("error reset pass request");
                    reject(err.response)
                })
        })
    },

    MEETING({ commit }, payload) {
        return new Promise((resolve, reject) => {
            axios({ url: 'http://127.0.0.1:8000/recruiter/gdateadd/', data: payload, method: 'POST' })
                .then(resp => {
                    resolve(resp.data)
                })
                .catch(err => {
                    console.log("error reset pass request");
                    reject(err.response)
                })
        })
    },

};
