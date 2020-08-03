export default {
    isLoggedIn: (state) => {
        return !!state.auth.token;
    },
    authStatus: (state) => {
        return state.auth.status;
    },
    refreshToken: (state) => {
        return state.auth.refresh_token;
    },
    isRecruiter: (state) => {
        return state.is_recruiter == true;
    },
    isRegistered: (state) => {
        return state.registered == true;
    },
    Name: (state) => {
        return state.auth.name;
    },

    Email: (state) => {
        return state.auth.email;
    }

};
