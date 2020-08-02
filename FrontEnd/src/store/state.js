export default {
    auth: {
        token: localStorage.getItem('token') || '',
        refresh_token: localStorage.getItem('rtoken') || '',
        name: localStorage.getItem('name') || '',
        email: '',
        status: '',
    },
    is_recruiter: JSON.parse(localStorage.getItem('is_recruiter')) || false,
    registered: JSON.parse(localStorage.getItem('registered')) || false
};
